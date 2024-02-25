# Metric Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## Metric Type

`object` ([Metric](schema-definitions-metric.md))

# Metric Properties

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                   |
| :----------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                        | `string` | Required | cannot be null | [MSML](schema-definitions-metric-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/type")                       |
| [name](#name)                        | `string` | Required | cannot be null | [MSML](schema-definitions-metric-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/name")                       |
| [description](#description)          | `string` | Required | cannot be null | [MSML](schema-definitions-metric-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/description")         |
| [variables\_used](#variables_used)   | `array`  | Required | cannot be null | [MSML](schema-definitions-metric-properties-variables_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/variables_used")   |
| [parameters\_used](#parameters_used) | `array`  | Required | cannot be null | [MSML](schema-definitions-metric-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/parameters_used") |
| [metrics\_used](#metrics_used)       | `array`  | Required | cannot be null | [MSML](schema-definitions-metric-properties-metrics_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/metrics_used")       |
| [domain](#domain)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-metric-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/domain")                   |
| [logic](#logic)                      | `string` | Required | cannot be null | [MSML](schema-definitions-metric-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/logic")                     |
| [symbol](#symbol)                    | `string` | Required | can be null    | [MSML](schema-definitions-metric-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/symbol")                   |

## type



`type`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/type")

### type Type

`string`

## name



`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/name")

### name Type

`string`

## description



`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/description")

### description Type

`string`

## variables\_used



`variables_used`

*   is required

*   Type: `string[][]`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-variables_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/variables_used")

### variables\_used Type

`string[][]`

## parameters\_used



`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/parameters_used")

### parameters\_used Type

`string[]`

## metrics\_used



`metrics_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-metrics_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/metrics_used")

### metrics\_used Type

`string[]`

## domain



`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/domain")

### domain Type

`string[]`

## logic



`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-metric-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/logic")

### logic Type

`string`

## symbol



`symbol`

*   is required

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-metric-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Metric/properties/symbol")

### symbol Type

`string`
