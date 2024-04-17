# Untitled object in MSML Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar
```



| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## StatefulMetricVar Type

`object` ([Details](schema-definitions-statefulmetricvar.md))

# StatefulMetricVar Properties

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                                         |
| :----------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [type](#type)                        | `string` | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/type")                       |
| [name](#name)                        | `string` | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/name")                       |
| [description](#description)          | `string` | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/description")         |
| [variables\_used](#variables_used)   | `array`  | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-variables_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/variables_used")   |
| [parameters\_used](#parameters_used) | `array`  | Optional | cannot be null | [MSML](schema-definitions-statefulmetricvar-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/parameters_used") |
| [symbol](#symbol)                    | `string` | Optional | can be null    | [MSML](schema-definitions-statefulmetricvar-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/symbol")                   |
| [domain](#domain)                    | `string` | Optional | can be null    | [MSML](schema-definitions-statefulmetricvar-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/domain")                   |

## type

The type of the metric variable

`type`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-type.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/type")

### type Type

`string`

## name

The name of the stateful metric variable

`name`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/name")

### name Type

`string`

## description

The description of the computation

`description`

*   is optional

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/description")

### description Type

`string`

## variables\_used

The variables used for computation of the form (state, variable)

`variables_used`

*   is optional

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-variables_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/variables_used")

### variables\_used Type

unknown\[]

## parameters\_used



`parameters_used`

*   is optional

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/parameters_used")

### parameters\_used Type

`string[]`

## symbol

The symbol associated with the stateful metric (optional)

`symbol`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-symbol.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/symbol")

### symbol Type

`string`

## domain

The mathematical domain of the stateful metric (optional)

`domain`

*   is optional

*   Type: `string`

*   can be null

*   defined in: [MSML](schema-definitions-statefulmetricvar-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetricVar/properties/domain")

### domain Type

`string`
