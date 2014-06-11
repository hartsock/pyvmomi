vim.dvs.DistributedVirtualPort.TrafficFilterConfigSpec
======================================================
inherits from [vim.dvs.DistributedVirtualPort.TrafficFilterConfig](docs/vim.dvs.DistributedVirtualPort.TrafficFilterConfig.md)
as of [vSphere API 5.5](vim.version.md#vim.version.version9)


The specification to reconfigure Traffic Filter.   This specification allows the user to do fine-grained updates for the   Traffic Filter in the port settings.   If the operation is <a href="vim.ConfigSpecOperation.md#remove">remove</a>, only the   TrafficFilterConfigSpec#key needs to be specified.   If other fields are specified, they will be ignored. We cannot remove   an inherited element. Only when the inherited flag is set to false and   parent does not have an element with same key this operation succeeds.   If the operation is <a href="vim.ConfigSpecOperation.md#add">add</a>, then   TrafficFilterConfigSpec#key should not be specified and   other fields need to be specified. The inherited flag should be set to   false.   If the operation is <a href="vim.ConfigSpecOperation.md#edit">edit</a>, then   TrafficFilterConfigSpec#key needs be specified and   specify the other properties that need modification. If the inherited   flag is set to true, a TrafficFilterConfig object of same   key must exist at the parent's level. The property values in the spec   object will be ignored and use the values from the parent's   TrafficFilterConfig object instead. If inherited   flag is set to false, then the new modifications will be applied.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| operation | string | None | None | Operation type. See <a href="vim.ConfigSpecOperation.md">ConfigSpecOperation</a> for valid values. |

