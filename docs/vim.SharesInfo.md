vim.SharesInfo
==============
inherits from [vmodl.DynamicData](docs/vmodl.DynamicData.md)


Specification of shares.   <p>   Shares are used to determine relative allocation between resource consumers.   In general, a consumer with more shares gets proportionally more of   the resource, subject to certain other constraints.

| property | type | optional | priv | desc |
|:---------|:-----|:---------|:-----|:-----|
| shares | int | None | None | The number of shares allocated. Used to determine resource allocation in case of    resource contention. This value is only set if level is set to custom. If level is    not set to custom, this value is ignored. Therefore, only shares with custom    values can be compared.   <p>   There is no unit for this value. It is a relative measure based on the settings    for other resource pools. |
| level | [vim.SharesInfo.Level](vim.SharesInfo.Level.md "vim.SharesInfo.Level") | None | None | The allocation level.  The level is a simplified view of shares.   Levels map to a pre-determined set of numeric values for shares.   If the shares value does not map to a predefined size, then   the level is set as custom. |

