# State Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State
```

The definition of states in the system. There is one global system state and then the rest of the definitions are local states, generally for recording what entity states there are.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## State Type

`object` ([State](schema-definitions-state.md))

# State Properties

| Property                | Type     | Required | Nullable       | Defined by                                                                                                                                                     |
| :---------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)           | `string` | Required | cannot be null | [MSML](schema-definitions-state-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/name")           |
| [notes](#notes)         | `string` | Required | cannot be null | [MSML](schema-definitions-state-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/notes")         |
| [variables](#variables) | `array`  | Required | cannot be null | [MSML](schema-definitions-state-properties-variables.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/variables") |

## name

Any notes about the state or its implementation

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/name")

### name Type

`string`

## notes

The name of the state

`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/notes")

### notes Type

`string`

## variables

All the attatched state variables for the component

`variables`

*   is required

*   Type: `object[]` ([Variable](schema-definitions-variable.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-state-properties-variables.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/State/properties/variables")

### variables Type

`object[]` ([Variable](schema-definitions-variable.md))
