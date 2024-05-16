# BoundaryActionOption Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption
```

Specific implementations of a control action which are in the same form of the underlying control action definition.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## BoundaryActionOption Type

`object` ([BoundaryActionOption](schema-definitions-boundaryactionoption.md))

# BoundaryActionOption Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                                       |
| :-------------------------- | :------- | :------- | :------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)               | `string` | Required | cannot be null | [MSML](schema-definitions-boundaryactionoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/name")               |
| [description](#description) | `string` | Required | cannot be null | [MSML](schema-definitions-boundaryactionoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/description") |
| [logic](#logic)             | `string` | Required | cannot be null | [MSML](schema-definitions-boundaryactionoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/logic")             |
| [metadata](#metadata)       | `object` | Optional | cannot be null | [MSML](schema-definitions-boundaryactionoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/metadata")       |

## name

The name of the boundary action option

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundaryactionoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/name")

### name Type

`string`

## description

A description of what this implementation does

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundaryactionoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/description")

### description Type

`string`

## logic

The logic related to the implementation

`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundaryactionoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/logic")

### logic Type

`string`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-boundaryactionoption-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-boundaryactionoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryActionOption/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-boundaryactionoption-properties-metadata.md))
