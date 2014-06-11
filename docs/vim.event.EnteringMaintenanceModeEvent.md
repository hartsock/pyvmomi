vim.event.EnteringMaintenanceModeEvent
======================================
inherits from [vim.event.HostEvent](docs/vim.event.HostEvent.md)


This event records that a host has begun the process of entering   maintenance mode. All virtual machine operations   are blocked, except the following:   <ul>   <li>MigrateVM   <li>PowerOffVM   <li>SuspendVM   <li>ShutdownGuest   <li>StandbyGuest   </ul>

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|

