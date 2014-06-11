vim.DistributedVirtualSwitch.NameArrayUplinkPortPolicy
======================================================
inherits from [vim.DistributedVirtualSwitch.UplinkPortPolicy](docs/vim.DistributedVirtualSwitch.UplinkPortPolicy.md)
as of [vSphere API 4.0](vim.version.md#vim.version.version5)


The uplink port policy specifies an array of uniform names   for the uplink ports across the hosts. The size of the array indicates   the number of uplink ports that will be created for each host in the   switch.   <p>   When the names in this array change, the uplink ports on all the   hosts are automatically renamed accordingly. Increasing the number   of names in the array automatically creates additional uplink ports   bearing the added name on each host. Decreasing the number of name   automatically deletes the unused uplink ports on each host. Decreasing   beyond the number of unused uplink port raises a fault.   <p>   This policy overrides the portgroup port naming format   (<a href="vim.dvs.DistributedVirtualPortgroup.ConfigSpec.md">DVPortgroupConfigSpec</a>.<a href="vim.dvs.DistributedVirtualPortgroup.ConfigSpec.md#portNameFormat">portNameFormat</a>),   if both are defined and the uplink ports are created in a uplink portgroup.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| uplinkPortName | string | None | None | The uniform name of uplink ports on each host. |

