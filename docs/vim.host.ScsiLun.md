vim.host.ScsiLun
================
inherits from [vim.host.Device](docs/vim.host.Device.md)


The <a href="vim.host.ScsiLun.md">ScsiLun</a> data object describes a SCSI logical unit.   A SCSI logical unit is a host device that an ESX Server or virtual machine   can use for I/O operations.   <p>   An ESX Server creates SCSI logical unit objects to represent   devices in the host configuration. (See the definition of   <a href="vim.host.ScsiLun.ScsiLunType.md">ScsiLunType</a> for a list of the supported device types.)   The vSphere API uses one of two object types to represent a SCSI   logical unit, depending on the device type.   <ul>     <li>Disks containing file system volumes or parts of volumes for hosts         or raw disks for virtual machines. To represent disks, the ESX Server         creates a <a href="vim.host.ScsiDisk.md">HostScsiDisk</a> object, which inherits properties from         the <a href="vim.host.ScsiLun.md">ScsiLun</a> base class.     </li>     <li>Other SCSI devices, for example SCSI passthrough devices         for virtual machines. To represent one of these devices,         the ESX Server creates a <a href="vim.host.ScsiLun.md">ScsiLun</a> object.     </li>   </ul>   <p>   When the Server creates a <a href="vim.host.ScsiDisk.md">HostScsiDisk</a> or <a href="vim.host.ScsiLun.md">ScsiLun</a> object,   it specifies a valid device name and type:   <ul>     <li><a href="vim.host.Device.md#deviceName">deviceName</a> - A string representing the name of the device         that is meaningful to the host. The following are some examples of         device names. <br />         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>/dev/cdrom</code><br />         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>/vmkdev/vmhba0:0:1:0</code><br />         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>PhysicalDrive0</code><br />     </li>     <li><a href="vim.host.Device.md#deviceType">deviceType</a> - A string describing the type of device.         The following are some examples of device types. <br />         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-cdrom</code> <br />         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-tape</code> <br />         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-disk</code> <br />         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-processor</code> <br />         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<code>scsi-unknown</code>     </li>   </ul>

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| key | string | true | None | Linkable identifier |
| uuid | string | None | None | Universally unique identifier for the LUN used to identify ScsiLun across   multiple servers.   <p>   This identifier can be used to identify analogous objects in other views   such as <a href="vim.host.MultipathInfo.LogicalUnit.md">HostMultipathInfoLogicalUnit</a> and <a href="vim.host.ScsiTopology.Lun.md">HostScsiTopologyLun</a>.   <p><br>See <a href="vim.host.MultipathInfo.LogicalUnit.md">HostMultipathInfoLogicalUnit</a><br>See <a href="vim.host.ScsiTopology.Lun.md">HostScsiTopologyLun</a><br> |
| descriptor | [vim.host.ScsiLun.Descriptor](vim.host.ScsiLun.Descriptor.md "vim.host.ScsiLun.Descriptor") | true | None | List of descriptors that can be used to identify the LUN object.  The   uuid will also appear as a descriptor.   <p>   The id field in the descriptor is a string that can be used to correlate   the ScsiLun across multiple servers.  A ScsiLun may have multiple   descriptors.  The choice and order of these descriptors may be different   on different servers.   <p>   Not all descriptors are suitable for correlation.  Some descriptors are   only sufficient to identify the ScsiLun within a single host.  Each   descriptor contains a quality property that indicates whether or not   the descriptor is suitable for correlation. |
| canonicalName | string | true | None | Canonical name of the SCSI logical unit.   <p>   Disk partition or extent identifiers refer to this name when   referring to a disk.  Use this property to correlate a partition   or extent to a specific SCSI disk.   <p><br>See <a href="vim.host.ScsiDisk.Partition.md#diskName">diskName</a><br> |
| displayName | string | true | None | User configurable display name of the SCSI logical unit.  A default   display name will be used if available.  If the display name is not   supported, it will be unset.  The display name does not have to be   unique but it is recommended that it be unique. |
| lunType | string | None | None | The type of SCSI device.  Must be one of the values of   <a href="vim.host.ScsiLun.ScsiLunType.md">ScsiLunType</a>. |
| vendor | string | true | None | The vendor of the SCSI device. |
| model | string | true | None | The model number of the SCSI device. |
| revision | string | true | None | The revision of the SCSI device. |
| scsiLevel | int | true | None | The SCSI level of the SCSI device. |
| serialNumber | string | true | None | The serial number of the SCSI device.   For a device that is SCSI-3 compliant, this property is derived   from page 80h of the Vital Product Data (VPD), as defined by the   SCSI-3 Primary Commands (SPC-3) spec.  Not all SCSI-3 compliant   devices provide this information.  For devices that are not   SCSI-3 compliant, this property is not defined. |
| durableName | [vim.host.ScsiLun.DurableName](vim.host.ScsiLun.DurableName.md "vim.host.ScsiLun.DurableName") | true | None | The durable name of the SCSI device.    For a SCSI-3 compliant device this property is derived from the    payloads of pages 80h and 83h of the Vital Product Data (VPD) as    defined by the T10 and SMI standards. For devices that do not provide   this information, this property is not defined. |
| alternateName | [vim.host.ScsiLun.DurableName](vim.host.ScsiLun.DurableName.md "vim.host.ScsiLun.DurableName") | true | None | Alternate durable names.   Records all available durable names derived from page 80h of the Vital   Product Data (VPD) and the Identification Vital Product Data (VPD) page   83h as defined by the SCSI-3 Primary Commands. For devices that are not   SCSI-3 compliant this property is not defined. |
| standardInquiry | int | true | None | Standard Inquiry payload.   For a SCSI-3 compliant device this property is derived from the    standard inquiry data. For devices that are not SCSI-3 compliant this    property is not defined. |
| queueDepth | int | true | None | The queue depth of SCSI device. |
| operationalState | string | None | None | The operational states of the LUN.   When more than one item is present in the array, the first state   should be considered the primary state.  For example, a LUN may   be "ok" and "degraded" indicating I/O is still possible to the LUN, but   it is operating in a degraded mode.<br>See <a href="vim.host.ScsiLun.State.md">ScsiLunState</a><br> |
| capabilities | [vim.host.ScsiLun.Capabilities](vim.host.ScsiLun.Capabilities.md "vim.host.ScsiLun.Capabilities") | true | None | Capabilities of SCSI device. |
| vStorageSupport | string | true | None | vStorage hardware acceleration support status. This property   represents storage acceleration provided by the SCSI logical unit.   See <a href="vim.host.ScsiLun.VStorageSupportStatus.md">ScsiLunVStorageSupportStatus</a> for valid values.   <p>   If a storage device supports hardware acceleration,   the ESX host can offload specific virtual machine management   operations to the storage device. With hardware assistance,   the host performs storage operations faster and consumes   less CPU, memory, and storage fabric bandwidth.   <p>   For vSphere 4.0 or earlier hosts, this value will be unset. |

