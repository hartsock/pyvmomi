vim.event.VmNoCompatibleHostForSecondaryEvent
=============================================
inherits from [vim.event.VmEvent](docs/vim.event.VmEvent.md)
as of [vSphere API 4.0](vim.version.md#vim.version.version5)


This event records that no compatible host was found to place a   secondary VM.   A default alarm will be triggered upon this event, which by default   would trigger a SNMP trap.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|

