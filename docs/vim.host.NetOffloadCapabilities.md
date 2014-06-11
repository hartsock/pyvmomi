vim.host.NetOffloadCapabilities
===============================
inherits from [vmodl.DynamicData](docs/vmodl.DynamicData.md)
### DEPRECATED



Offload capabilities are used to optimize virtual machine network   performance.  When a virtual machine is transmitting on a network,   some operations can be offloaded either to the host or to physical   hardware.  This data object type defines the set of offload capabilities   that may be available on a host.   <p>   This data object type is used both to publish the list of offload capabilities   and to contain offload capability policy settings.  The network   policy logic is built on a two-level inheritance scheme which   requires that all settings be optional.  As a result, all properties   on the NetOffloadCapabilities object must be optional.<br>See <a href="vim.host.NetworkPolicy.md">HostNetworkPolicy</a><br>

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| csumOffload | bool | true | None | (Optional) The flag to indicate whether or not checksum    offloading is supported. |
| tcpSegmentation | bool | true | None | (Optional) The flag to indicate whether or not TCP segmentation    offloading (TSO) is supported. |
| zeroCopyXmit | bool | true | None | (Optional) The flag to indicate whether or not zero copy    transmits are supported. |

