vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo
=======================================================
inherits from [vim.vm.device.VirtualDevice.FileBackingInfo](docs/vim.vm.device.VirtualDevice.FileBackingInfo.md)


This data object type contains information about backing a virtual disk using a   raw device mapping. Supported for ESX Server 2.5 and 3.x.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| lunUuid | string | true | None | Unique identifier of the LUN accessed by the raw disk mapping. |
| deviceName | string | true | None | The host-specific device the LUN is being accessed through. If the   target LUN is not available on the host then it is empty. For example, this   could happen if it has accidentally been masked out. |
| compatibilityMode | string | true | None | The compatibility mode of the raw disk mapping (RDM). This must be specified   when a new virtual disk with an RDM backing is created. On subsequent virtual   machine reconfigurations, this property should be handled as follows,   depending on the version of the host:   <p>   On ESX Server 2.5, the compatibility mode of an RDM backing is a   characteristic of the virtual machine's configuration. When reconfiguring   a virtual machine that currently uses a virtual disk backed by an RDM,   the compatibility mode of that backing may be modified. When reconfiguring a   virtual machine to add an existing virtual disk backed by an RDM, the   compatibility mode of that backing may be specified. If left unspecified it   defaults to "physicalMode".   <p>   On ESX Server 3.x, the compatibility mode of an RDM backing is a   characteristic of the RDM itself. Once the RDM is created, its compatibility   mode cannot be changed by reconfiguring the virtual machine. When   reconfiguring a virtual machine to add an existing virtual disk backed by an   RDM, the compatibility mode of that backing must be left unspecified.   <p><br>See <a href="vim.vm.device.VirtualDiskOption.CompatibilityMode.md">VirtualDiskCompatibilityMode</a><br> |
| diskMode | string | true | None | The disk mode. Valid values are:   <ul>   <li><a href="vim.vm.device.VirtualDiskOption.DiskMode.md#persistent">persistent</a>   <li><a href="vim.vm.device.VirtualDiskOption.DiskMode.md#independent_persistent">independent_persistent</a>   <li><a href="vim.vm.device.VirtualDiskOption.DiskMode.md#independent_nonpersistent">independent_nonpersistent</a>   <li><a href="vim.vm.device.VirtualDiskOption.DiskMode.md#nonpersistent">nonpersistent</a>   <li><a href="vim.vm.device.VirtualDiskOption.DiskMode.md#undoable">undoable</a>   <li><a href="vim.vm.device.VirtualDiskOption.DiskMode.md#append">append</a>   </ul>   <p>   Disk modes are only supported when the raw disk mapping is using virtual   compatibility mode.<br>See <a href="vim.vm.device.VirtualDiskOption.DiskMode.md">VirtualDiskMode</a><br> |
| uuid | string | true | None | Disk UUID for the virtual disk, if available. Disk UUID is not available if   the raw disk mapping is in physical compatibility mode. |
| contentId | string | true | None | Content ID of the virtual disk file, if available.  <p>  A content ID indicates the logical contents of the disk backing and its parents.  <p>  This property is only guaranteed to be up to date if this disk backing is not  currently being written to by any virtual machine.  <p>  The only supported operation is comparing if two content IDs are equal or not.  The guarantee provided by the content ID is that if two disk backings have the  same content ID and are not currently being written to, then reads issued from  the guest operating system to those disk backings will return the same data. |
| changeId | string | true | None | The change ID of the virtual disk for the corresponding  snapshot or virtual machine. This can be used to track  incremental changes to a virtual disk. See   <a href="vim.VirtualMachine.md#queryChangedDiskAreas">QueryChangedDiskAreas</a>. |
| parent | [vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo](vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo.md "vim.vm.device.VirtualDisk.RawDiskMappingVer1BackingInfo") | true | None | The parent of this virtual disk file, if this is a delta disk backing.  This will be unset if this is not a delta disk backing.  <p>  A delta disk backing is a way to preserve a virtual disk backing  at some point in time.  A delta disk backing is a file backing which in  turn points to the original virtual disk backing (the parent).  After a delta  disk backing is added, all writes go to the delta disk backing.  All reads  first try the delta disk backing and then try the parent backing if needed.  <p>  A delta disk backing can be added to a disk either implicitly during  snapshot operations, or explicitly during create or reconfigure of the virtual  machine.  <p>  Note that the type of the backing is consistent throughout the chain; any new  delta disk backing which is added is of the same type as the original disk .  Also note that since the parent backing is not being written to,  it is possible that the parent backing may be shared among multiple  disks belonging to multiple virtual machines.  <p>  During virtual machine <a href="vim.Folder.md#createVm">creation</a> and  <a href="vim.VirtualMachine.md#reconfigure">reconfiguration</a> this property is  only checked if the <a href="vim.vm.device.VirtualDeviceSpec.md">VirtualDeviceConfigSpec</a> specifies  an <a href="vim.vm.device.VirtualDeviceSpec.Operation.md#add">add operation</a> with a  <a href="vim.vm.device.VirtualDeviceSpec.FileOperation.md#create">create file operation</a>.  In this case, a new delta disk backing is created which points to the parent  disk backing.  Only the <a href="vim.vm.device.VirtualDevice.FileBackingInfo.md#fileName">fileName</a>  property is important; all other properties will be ignored.  The parent backing  is assumed to exist and will not be recursively created.  <p>  Only raw disk mappings in <a href="vim.vm.device.VirtualDiskOption.CompatibilityMode.md#virtualMode">virtual compatibility mode</a> can have parents.  <p>  This property may only be set if  <a href="vim.host.Capability.md#deltaDiskBackingsSupported">deltaDiskBackingsSupported</a>  is true. |

