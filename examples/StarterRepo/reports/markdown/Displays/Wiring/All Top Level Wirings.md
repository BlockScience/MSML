## Wiring Diagrams

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Variable A"])
EES0 --- EE0
end

subgraph X4["Dummy Boundary Wiring"]
direction TB
X1["Dummy Boundary Action"]
X2["Dummy Policy"]
X3["Dummy Mechanism"]
X3 --> EES0
X1--"Dummy Space 1"--->X2
X2--"Dummy Space 2"--->X3
end
```

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Variable A"])
EES0 --- EE0
end

subgraph X4["Dummy Boundary Wiring 2"]
direction TB
X1["Dummy Boundary Action 2"]
X2["Dummy Policy"]
X3["Dummy Mechanism"]
X3 --> EES0
X1--"Dummy Space 1"--->X2
X2--"Dummy Space 2"--->X3
end
```

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Variable A"])
EES0 --- EE0
end

subgraph X4["Dummy Control Wiring"]
direction TB
X1["Dummy Control Action"]
X2["Dummy Policy"]
X3["Dummy Mechanism"]
X3 --> EES0
X1--"Dummy Space 1"--->X2
X2-."Dummy Space 2"..->X3
end
```

## Description

The wirings which are not components of other wirings.
## Wirings
1. [[Dummy Boundary Wiring]]
2. [[Dummy Boundary Wiring 2]]
3. [[Dummy Control Wiring]]

## Unique Components Used
1. [[Dummy Boundary Action]]
2. [[Dummy Boundary Action 2]]
3. [[Dummy Control Action]]
4. [[Dummy Mechanism]]
5. [[Dummy Policy]]

## Unique Parameters Used
1. [[dummy_parameter]]

