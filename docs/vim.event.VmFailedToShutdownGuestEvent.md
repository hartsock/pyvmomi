vim.event.VmFailedToShutdownGuestEvent
======================================
inherits from [vim.event.VmEvent](docs/vim.event.VmEvent.md)


This event records a failure to shut down the guest on a virtual machine.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| reason | [vmodl.LocalizedMethodFault](vmodl.LocalizedMethodFault.md "vmodl.LocalizedMethodFault") | None | None | The reason for the failure. |

