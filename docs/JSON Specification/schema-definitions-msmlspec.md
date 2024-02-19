# MSMLSpec Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec
```

A JSON schema that is used in the mathematical specification mapping library to create the underlying MSML object.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                  |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Forbidden             | none                | [schema.schema.json\*](../../out/schema.schema.json "open original schema") |

## MSMLSpec Type

`object` ([MSMLSpec](schema-definitions-msmlspec.md))

# MSMLSpec Properties

| Property                              | Type    | Required | Nullable       | Defined by                                                                                                                                                                         |
| :------------------------------------ | :------ | :------- | :------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Policies](#policies)                 | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-policies.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Policies")                 |
| [Spaces](#spaces)                     | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-spaces.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Spaces")                     |
| [State](#state)                       | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/State")                       |
| [Stateful Metrics](#stateful-metrics) | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-stateful-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Stateful Metrics") |
| [Parameters](#parameters)             | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Parameters")             |
| [Mechanisms](#mechanisms)             | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-mechanisms.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Mechanisms")             |
| [Entities](#entities)                 | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-entities.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Entities")                 |
| [Boundary Actions](#boundary-actions) | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-boundary-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Boundary Actions") |
| [Control Actions](#control-actions)   | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-control-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Control Actions")   |
| [Wiring](#wiring)                     | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-wiring.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Wiring")                     |
| [Types](#types)                       | `array` | Required | cannot be null | [MSML](schema-definitions-msmlspec-properties-types.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Types")                       |

## Policies



`Policies`

*   is required

*   Type: `object[]` ([Policy](schema-definitions-policy.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-policies.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Policies")

### Policies Type

`object[]` ([Policy](schema-definitions-policy.md))

## Spaces



`Spaces`

*   is required

*   Type: `object[]` ([Space](schema-definitions-space.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-spaces.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Spaces")

### Spaces Type

`object[]` ([Space](schema-definitions-space.md))

## State



`State`

*   is required

*   Type: `object[]` ([State](schema-definitions-state.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-state.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/State")

### State Type

`object[]` ([State](schema-definitions-state.md))

## Stateful Metrics



`Stateful Metrics`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-stateful-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Stateful Metrics")

### Stateful Metrics Type

unknown\[]

## Parameters



`Parameters`

*   is required

*   Type: `object[]` ([Parameter](schema-definitions-parameter.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-parameters.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Parameters")

### Parameters Type

`object[]` ([Parameter](schema-definitions-parameter.md))

## Mechanisms



`Mechanisms`

*   is required

*   Type: `object[]` ([Mechanism](schema-definitions-mechanism.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-mechanisms.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Mechanisms")

### Mechanisms Type

`object[]` ([Mechanism](schema-definitions-mechanism.md))

## Entities



`Entities`

*   is required

*   Type: `object[]` ([Entity](schema-definitions-entity.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-entities.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Entities")

### Entities Type

`object[]` ([Entity](schema-definitions-entity.md))

## Boundary Actions



`Boundary Actions`

*   is required

*   Type: unknown\[]

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-boundary-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Boundary Actions")

### Boundary Actions Type

unknown\[]

## Control Actions



`Control Actions`

*   is required

*   Type: `object[]` ([ControlAction](schema-definitions-controlaction.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-control-actions.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Control Actions")

### Control Actions Type

`object[]` ([ControlAction](schema-definitions-controlaction.md))

## Wiring



`Wiring`

*   is required

*   Type: `object[]` ([Wiring](schema-definitions-wiring.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-wiring.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Wiring")

### Wiring Type

`object[]` ([Wiring](schema-definitions-wiring.md))

## Types



`Types`

*   is required

*   Type: `object[]` ([Type](schema-definitions-type.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-msmlspec-properties-types.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/MSMLSpec/properties/Types")

### Types Type

`object[]` ([Type](schema-definitions-type.md))
