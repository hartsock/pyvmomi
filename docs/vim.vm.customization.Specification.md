vim.vm.customization.Specification
==================================
inherits from [vmodl.DynamicData](docs/vmodl.DynamicData.md)


The Specification data object type contains information required to customize a   virtual machine when deploying it or migrating it to a new  host.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| options | [vim.vm.customization.Options](vim.vm.customization.Options.md "vim.vm.customization.Options") | true | None | Optional operations (either LinuxOptions or WinOptions). |
| identity | [vim.vm.customization.IdentitySettings](vim.vm.customization.IdentitySettings.md "vim.vm.customization.IdentitySettings") | None | None | Network identity and settings, similar to Microsoft's Sysprep tool. This is a   Sysprep, LinuxPrep, or SysprepText object. |
| globalIPSettings | [vim.vm.customization.GlobalIPSettings](vim.vm.customization.GlobalIPSettings.md "vim.vm.customization.GlobalIPSettings") | None | None | Global IP settings constitute the IP settings that are not specific to a   particular virtual network adapter. |
| nicSettingMap | [vim.vm.customization.AdapterMapping](vim.vm.customization.AdapterMapping.md "vim.vm.customization.AdapterMapping") | true | None | IP settings that are specific to a particular virtual network adapter. The   AdapterMapping object maps a network adapter's MAC address to its Adapter   settings object. May be empty if there are no network adapters, else should   match number of network adapters in the VM. |
| encryptionKey | int | true | None | Byte array containing the public key used to encrypt any passwords stored in the   specification. Both the client and the server can use this to determine if   stored passwords can be decrypted by the server or if the passwords need to be   re-entered and re-encrypted before the specification can be used. |

