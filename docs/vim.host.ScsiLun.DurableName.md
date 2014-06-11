vim.host.ScsiLun.DurableName
============================
inherits from [vmodl.DynamicData](docs/vmodl.DynamicData.md)


This data object type represents an SMI-S "Correlatable and    Durable Name" which is an   identifier for a logical unit number (LUN) that is generated using    a common algorithm.  The algorithm divides the identifier into    multiple namespaces where each   namespace uses a different set of properties of the LUN to generate   the identifier.  The namespace itself is encoded in the identifier.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| namespace | string | None | None | The string describing the namespace used for the durable name. |
| namespaceId | int | None | None | The byte used by the ESX Server product to represent the namespace. |
| data | int | true | None | The variable length byte array containing the namespace-specific data.    For a SCSI-3 compliant device this field is the descriptor header   along with the payload for data obtained from page 83h, and is the   payload for data obtained from page 80h of the Vital Product Data   (VPD). |

