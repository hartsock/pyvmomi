vim.net.DnsConfigSpec
=====================
inherits from [vmodl.DynamicData](docs/vmodl.DynamicData.md)
as of [vSphere API 4.1](vim.version.md#vim.version.version6)


Domain Name Server (DNS) Configuration Specification -   a data object for configuring the RFC 1034 client side DNS settings.   TBD: remove this section, only for discussing what goes into this object.   Place properties here that are specific to the RFC/common to all systems.   Properties that are platform specific should go into a separate config spec.       http://technet.microsoft.com/en-us/library/cc778792.aspx      http://en.wikipedia.org/wiki/Microsoft_DNS

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| dhcp | bool | true | None | The flag to indicate whether or not dynamic host control   protocol (DHCP) will be used to set DNS configuration automatically.   See vim.net.DhcpConfigSpec |
| hostName | string | true | None | The host name portion of DNS name. For example,   "esx01" part of esx01.example.com. The rules for forming a hostname   are specified in RFC 1034. |
| domainName | string | true | None | The domain name portion of the DNS name. This would be the   "example.com" part of  esx01.example.com. The rules for forming   a domain name are defined in RFC 1034. |
| ipAddress | string | true | None | Unicast IP address(s) of one or more DNS servers in order of use.   IPv4 addresses are specified using   dotted decimal notation.  For example, "192.0.2.1".   IPv6 addresses are 128-bit addresses represented as   eight fields of up to four hexadecimal digits.   A colon separates each field (:). For example,   2001:DB8:101::230:6eff:fe04:d9ff. The address can also consist of the   symbol '::' to represent multiple 16-bit groups of   contiguous 0's only once in an address as described in RFC 2373. |
| searchDomain | string | true | None | The domain in which to search for hosts in order of preference. |


