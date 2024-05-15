## Wiring Diagrams

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Variable A"])
EES0 --- EE0
end

subgraph X4["Dummy Boundary Block"]
direction TB
X1["Dummy Boundary Action"]
X2["Dummy Policy"]
X3["Dummy Mechanism"]
X3 --> EES0
X1--"Dummy Space 1"--->X2
X2--"Dummy Space 2"--->X3
end
```

## Description

The wirings related to only boundary type actions.
## Wirings
1. [[Dummy Boundary Block]]

## Unique Components Used
1. [[Dummy Boundary Action]]
2. [[Dummy Mechanism]]
3. [[Dummy Policy]]

## Unique Parameters Used
1. [[dummy_parameter]]

