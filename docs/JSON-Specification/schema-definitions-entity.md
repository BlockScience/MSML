# Entity Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity
```

Entities are any class of user or infrastructure that should have their own state and potentially ability to call boundary actions. Examples could be a customer or a company (for which a simulation might assume it is acting as one cohesive unit)

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## Entity Type

`object` ([Entity](schema-definitions-entity.md))

# Entity Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                     |
| :-------------------- | :------- | :------- | :------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/name")         |
| [notes](#notes)       | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/notes")       |
| [state](#state)       | `string` | Required | cannot be null | [MSML](schema-definitions-entity-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/state")       |
| [metadata](#metadata) | `object` | Optional | cannot be null | [MSML](schema-definitions-entity-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/metadata") |

## name

The name of the entity

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/name")

### name Type

`string`

## notes

Any notes on the entity

`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/notes")

### notes Type

`string`

## state

The string key for the state associated with the entity

`state`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/state")

### state Type

`string`

## metadata



`metadata`

*   is optional

*   Type: `object` ([Details](schema-definitions-entity-properties-metadata.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-entity-properties-metadata.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/Entity/properties/metadata")

### metadata Type

`object` ([Details](schema-definitions-entity-properties-metadata.md))
