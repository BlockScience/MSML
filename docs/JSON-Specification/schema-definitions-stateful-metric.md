# Stateful Metric Schema

```txt
https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric
```

Variables that are not held directly in the state but can computed from the state & parameters.

| Abstract            | Extensible | Status         | Identifiable | Custom Properties | Additional Properties | Access Restrictions | Defined In                                                                                    |
| :------------------ | :--------- | :------------- | :----------- | :---------------- | :-------------------- | :------------------ | :-------------------------------------------------------------------------------------------- |
| Can be instantiated | No         | Unknown status | No           | Forbidden         | Allowed               | none                | [schema.schema.json\*](../../out/math_spec_mapping/schema.schema.json "open original schema") |

## StatefulMetric Type

`object` ([Stateful Metric](schema-definitions-stateful-metric.md))

# StatefulMetric Properties

| Property              | Type     | Required | Nullable       | Defined by                                                                                                                                                                    |
| :-------------------- | :------- | :------- | :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [name](#name)         | `string` | Required | cannot be null | [MSML](schema-definitions-stateful-metric-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/name")       |
| [notes](#notes)       | `string` | Required | cannot be null | [MSML](schema-definitions-stateful-metric-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/notes")     |
| [metrics](#metrics)   | `array`  | Required | cannot be null | [MSML](schema-definitions-stateful-metric-properties-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/metrics") |
| Additional Properties | Any      | Optional | can be null    |                                                                                                                                                                               |

## name

The name of the stateful metric set

`name`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-stateful-metric-properties-name.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/name")

### name Type

`string`

## notes

Any notes about the stateful metric set

`notes`

*   is required

*   Type: `string`

*   cannot be null

*   defined in: [MSML](schema-definitions-stateful-metric-properties-notes.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/notes")

### notes Type

`string`

## metrics



`metrics`

*   is required

*   Type: `object[]` ([Details](schema-definitions-statefulmetricvar.md))

*   cannot be null

*   defined in: [MSML](schema-definitions-stateful-metric-properties-metrics.md "https://github.com/BlockScience/MSML/src/schema.schema.json#/definitions/StatefulMetric/properties/metrics")

### metrics Type

`object[]` ([Details](schema-definitions-statefulmetricvar.md))

## Additional Properties

Additional properties are allowed and do not have to follow a specific schema
