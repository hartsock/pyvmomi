# VMware vSphere Python SDK
# Copyright (c) 2008-2014 VMware, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from lxml import etree

from pyVmomi.SoapAdapter import SOAP_NSMAP


# inverted map from the soap adapter for use with lxml etree
NSMAP = dict(zip(SOAP_NSMAP.values(), SOAP_NSMAP.keys()))


# derive a list of all attributes in both nodes
def _extract_attribute_names(expected, observed):
    names = set()
    for name in expected.attrib.keys():
        names.add(name)
    for name in observed.attrib.keys():
        names.add(name)
    return names


# returns without exception if both nodes have identical attribute lists
def _check_attribute_names(expected, observed, names):
    for name in names:
        if name not in expected.attrib.keys():
            return False
        if name not in observed.attrib.keys():
            return False
    return True


# returns without exception only if the attributes on both nodes match
def _check_attribute_values(expected, observed, names):
    for name in names:
        e_val = expected.attrib[name]
        o_val = observed.attrib[name]
        if not e_val == o_val:
            return False
    return True


# returns only if the attributes on both nodes check out
def _attribute_compare(expected, observed):
    names = _extract_attribute_names(expected, observed)
    if not _check_attribute_names(expected, observed, names):
        return False
    if not _check_attribute_values(expected, observed, names):
        return False
    return True


# returns only if the current nodes match tag, text, and attributes
def _node_compare(expected, observed):
    if not expected.tag == observed.tag:
        return False
    if not str(expected.text).strip() == str(observed.text).strip():
        return False
    return _attribute_compare(expected, observed)


# returns True only if both trees match completely
def _compare_node_lists(expected_nodes, observed_nodes, comparison, finder):
    if not len(expected_nodes) == len(observed_nodes):
        return False
    for e, o in zip(expected_nodes, observed_nodes):
        if not _attribute_compare(e, o):
            return False
        if not _compare(e, o, comparison, finder):
            return False
    else:
        return True


# compares trees based on comparison method passed in
def collect_all_tags(node, tags):
    for child in node:
        collect_all_tags(child, tags)
        tags.add(child.tag)
    return tags


def _compare(expected, observed, comparison, finder):
    tags = set()
    collect_all_tags(expected, tags)
    collect_all_tags(observed, tags)

    for tag in tags:
        elist = finder(expected, tag)
        olist = finder(observed, tag)
        if not _compare_node_lists(elist, olist, comparison, finder):
            return False

    if not comparison(expected, observed):
        return False
    return True


def full_compare(expected, observed, compare=None, finder=None):
    """Performs a logical comparison of two XML documents.

    The first document is used to confirm the second.

    NOTE (hartsock):
        List and set based comparisons are not supported. The comparisons
        only work properly on tree-type documents without repeating elements
        This currently runs deep enough comparisons for our current work but
        comparing inventory lists or other types of long result sets could
        pose a challenge based solely on the XML document.

    Args:
        expected (str): The expected XML document as a string.
        observed (str): The observed XML document as a string.

    Returns:
        bool. If the documents match or do not.
    """
    if compare is None:
        compare = _node_compare

    if finder is None:
        finder = _search_for_tag

    exp = etree.XML(expected)
    obs = etree.XML(observed)

    return _compare(exp, obs, compare, finder)


# trims off the <?xml version="1.0" encoding="UTF-8"?> tag and whitespace
def _trim_encoding_declaration(source):
    index = source.index('?>')
    return source[index+3:].strip()


def soap_compare(expected, observed):
    """Compares two soap documents based on their XML trees.

    Returns true only if both trees are logically equivalent.
    """
    etrimmed = _trim_encoding_declaration(expected)
    otrimmed = _trim_encoding_declaration(observed)
    return full_compare(etrimmed, otrimmed, _node_compare,
                        _soap_search_for_tag)


# searching in SOAP documents requires knowledge of the XML namespace
def _soap_search_for_tag(doc, tag):
    search = './/{0}'.format(tag)
    return doc.findall(search, namespaces=NSMAP)


# searching in non-soap documents does not require namespace knowledge
def _search_for_tag(doc, tag):
    search = './/{0}'.format(tag)
    return doc.findall(search)


def _node_comparator(list_a, list_b, comparator, finder):
    return _compare_node_lists(list_a, list_b, comparator, finder)


def node_wise(expected, observed, tag_name, finder=None):
    """Performs a logical comparison of two XML documents restricted by node.

    NOTE: only top-level nodes under root node can be used because of a
    limitation in Python 2.6 which prevents us from searching for tags deeper
    than the top level.

    The first document confirms the second but only as far as the named
    nodes in the document with the name `tag_name` are concerned.

    Args:
        expected (str): The expected XML document as a string.
        observed (str): The observed XML document as a string.
        tag_name (str): The name of the tag(s) you want to assert are the same.

    Returns:
        bool. If the documents match or do not.
    """
    if finder is None:
        finder = _search_for_tag

    exp = etree.XML(expected)
    obs = etree.XML(observed)

    expected_nodes = finder(exp, tag_name)
    observed_nodes = finder(obs, tag_name)

    return _node_comparator(expected_nodes, observed_nodes, _node_compare,
                            finder)


def soap_node_wise(expected, observed, tag_name):
    """Performs a logical comparison of two SOAP documents restricted by node.

    Slightly different internal details handle namespace related issues with
    searching within a SOAP envelope.

    Args:
        expected (str): The expected XML document as a string.
        observed (str): The observed XML document as a string.
        tag_name (str): The name of the tag(s) you want to assert are the same.

    Returns:
        bool. If the documents match or do not.
    """
    etrimmed = _trim_encoding_declaration(expected)
    otrimmed = _trim_encoding_declaration(observed)

    return node_wise(etrimmed, otrimmed, tag_name, _soap_search_for_tag)
