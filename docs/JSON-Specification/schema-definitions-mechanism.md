# Mechanism Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism
```

Anything that updates state in the system, usually policies will call these with the outputs of logic. The reasoning to split them out is so that if at some point you want to add a recording variable every time an account is changed or do something like have a variable listener, you can just change the mechanism responsible for it in only one place.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## Mechanism Type

`object` ([Mechanism](schema-definitions-mechanism.md))

# Mechanism Properties

| Property                             | Type     | Required | Nullable       | Defined by                                                                                                                                                                         |
| :----------------------------------- | :------- | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)                        | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/name")                       |
| [description](#description)          | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/description")         |
| [constraints](#constraints)          | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints")         |
| [logic](#logic)                      | `string` | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/logic")                     |
| [domain](#domain)                    | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain")                   |
| [parameters\_used](#parameters_used) | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used") |
| [updates](#updates)                  | `array`  | Required | cannot be null | [MSML](schema-definitions-mechanism-properties-updates.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates")                 |
| [metadata](#metadata)                | `object` | Optional | cannot be null | [MSML](schema-definitions-mechanism-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/metadata")               |

## name

The name of the mechanism

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/name")

### name Type

`string`

## description

The description of what the mechanism does

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/description")

### description Type

`string`

## constraints

Any constraints which the mechanism must respect

`constraints`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-constraints.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/constraints")

### constraints Type

`string[]`

## logic

The logic of how the mechanism should work

`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/logic")

### logic Type

`string`

## domain

The spaces which are the input into the mechanism

`domain`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-domain.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/domain")

### domain Type

`string[]`

## parameters\_used

The string keys of parameters which have an effect on the mechanism

`parameters_used`

*   is required

*   Type: `string[]`

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-parameters_used.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/parameters_used")

### parameters\_used Type

`string[]`

## updates

The states updates that the mechanism causes in the form of (Entity, State Variable)

`updates`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-updates.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/updates")

### updates Type

unknown\[]

## metadata

Any metadata that is added onto the mechanism

`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-mechanism-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-mechanism-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Mechanism/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-mechanism-properties-metadata.md))
