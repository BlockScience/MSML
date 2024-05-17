# Boundary Action Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction
```

The definition of different actions that might happen outside of the system such as customers coming into a shop. Generally will be called by entities.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## BoundaryAction Type

`object` ([Boundary Action](schema-definitions-boundary-action.md))

# BoundaryAction Properties

| Property                                              | Type     | Required | Nullable       | Defined by                                                                                                                                                                                                    |
| :---------------------------------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [name](#name)                                         | `string` | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/name")                                       |
| [description](#description)                           | `string` | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/description")                         |
| [constraints](#constraints)                           | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/constraints")                         |
| [boundary\_action\_options](#boundary_action_options) | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-boundary_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/boundary_action_options") |
| [called\_by](#called_by)                              | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-called_by.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/called_by")                             |
| [codomain](#codomain)                                 | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/codomain")                               |
| [parameters\_used](#parameters_used)                  | `array`  | Required | cannot be null | [MSML](schema-definitions-boundary-action-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/parameters_used")                 |
| Additional Properties                                 | Any      | Optional | can be null    |                                                                                                                                                                                                               |

## name

Name of the boundary action

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/name")

### name Type

`string`

## description

Quick description of the boundary action

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/description")

### description Type

`string`

## constraints

Any constraints which the boundary action must respect

`constraints`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/constraints")

### constraints Type

`string[]`

## boundary\_action\_options

The options for implementation of the boundary action

`boundary_action_options`

*   is required

*   Type: `object[]` ([BoundaryActionOption](schema-definitions-boundaryactionoption.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-boundary_action_options.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/boundary_action_options")

### boundary\_action\_options Type

`object[]` ([BoundaryActionOption](schema-definitions-boundaryactionoption.md))

## called\_by

The entities which are allowed to call this boundary action

`called_by`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-called_by.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/called_by")

### called\_by Type

`string[]`

## codomain

List of outputs that come out of this block

`codomain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-codomain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/codomain")

### codomain Type

`string[]`

## parameters\_used

The string keys of parameters which have an effect on the boundary action

`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-boundary-action-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/BoundaryAction/properties/parameters_used")

### parameters\_used Type

`string[]`

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
