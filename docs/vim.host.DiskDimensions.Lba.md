vim.host.DiskDimensions.Lba
===========================
inherits from [vmodl.DynamicData](docs/vmodl.DynamicData.md)


This data object type describes the logical block addressing system    that uses block numbers and block sizes to refer to a block.  This    scheme is employed by SCSI.  If a SCSI disk is not involved,   then blockSize is 512 bytes.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| blockSize | int | None | None | The size of the blocks. |
| block | long | None | None | The number of blocks. |

