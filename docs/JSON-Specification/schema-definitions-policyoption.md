# PolicyOption Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption
```

The concrete possible implementations that a given policy block can reference or select

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## PolicyOption Type

`object` ([PolicyOption](schema-definitions-policyoption.md))

# PolicyOption Properties

| Property                    | Type     | Required | Nullable       | Defined by                                                                                                                                                                       |
| :-------------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)               | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/name")               |
| [description](#description) | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/description") |
| [logic](#logic)             | `string` | Required | cannot be null | [MSML](schema-definitions-policyoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/logic")             |
| [metadata](#metadata)       | `object` | Optional | cannot be null | [MSML](schema-definitions-policyoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/metadata")       |

## name

The name of the policy option

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/name")

### name Type

`string`

## description

A description of the implementation

`description`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-description.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/description")

### description Type

`string`

## logic

Any logic associated with the implementation

`logic`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-logic.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/logic")

### logic Type

`string`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-policyoption-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-policyoption-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/PolicyOption/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-policyoption-properties-metadata.md))
