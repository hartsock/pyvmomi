vim.host.NetworkPolicy
======================
inherits from [vmodl.DynamicData](docs/vmodl.DynamicData.md)


This data object type describes network policies that can be configured for    both virtual switches and port groups.  The policy settings on the    port group can inherit policy settings from their containing virtual    switch.  These policy settings are inherited if   the settings on the port group are not set.  Since every policy   setting on a port group is optional, every individual policy setting    can be inherited.   <p>   By contrast, if a host is capable of implementing a policy setting, every   virtual switch has some value assigned to the policy setting.  In this   case, although all of the policy settings are optional,    they always have some value either by inheritance or by direct   setting.   <p>   Policy settings are organized into policy groups such as SecurityPolicy.    Policy groups are optional since it is possible that a host may not implement   such policies.  If a host does not support a policy group, the policy group   is not set on both the virtual switches and the port groups.<br>See <a href="vim.host.NetCapabilities.md">HostNetCapabilities</a><br>

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| security | [vim.host.NetworkPolicy.SecurityPolicy](vim.host.NetworkPolicy.SecurityPolicy.md "vim.host.NetworkPolicy.SecurityPolicy") | true | None | The security policy governing ports on this virtual switch. |
| nicTeaming | [vim.host.NetworkPolicy.NicTeamingPolicy](vim.host.NetworkPolicy.NicTeamingPolicy.md "vim.host.NetworkPolicy.NicTeamingPolicy") | true | None | The network adapter teaming policy. The bridge must be BondBridge    for this property to be valid. |
| offloadPolicy | [vim.host.NetOffloadCapabilities](vim.host.NetOffloadCapabilities.md "vim.host.NetOffloadCapabilities") | true | None | Offload capabilities are used to optimize virtual machine network   performance.  When a virtual machine is transmitting on a network,   some operations can be offloaded to either the host or the physical   hardware.  This policy indicates what networking related operations   should be offloaded.   <p>   All virtual machines using this PortGroup are subject to this   policy.  There is no setting for an individual virtual machine    to determine if an operation should be offloaded. |
| shapingPolicy | [vim.host.NetworkPolicy.TrafficShapingPolicy](vim.host.NetworkPolicy.TrafficShapingPolicy.md "vim.host.NetworkPolicy.TrafficShapingPolicy") | true | None | The traffic shaping policy. |


