vim.event.VmDasUpdateErrorEvent
===============================
inherits from [vim.event.VmEvent](docs/vim.event.VmEvent.md)


The event records that an error occured when updating the HA agents  with the current state of the virtual machine. If this occurs during a  powerOn operation, the virtual machine will not be failed over in the  event of a host failure. If it occurs during a powerOff, the virtual  machine will be automatically powered on if the host it was last running  on crashes.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|

