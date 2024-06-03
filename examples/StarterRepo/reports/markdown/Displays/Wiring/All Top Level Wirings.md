## Wiring Diagrams

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
end

subgraph X4["Dummy Boundary Wiring"]
direction TB
X1["Dummy Boundary Action"]
X2["DUMMY Letter Count Policy"]
X3["DUMMY Log Results Mechanism"]
X3 --> EES1
X3 --> EES0
X1--"Dummy Space 1"--->X2
X2--"Dummy Space 2"--->X3
end
```

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
end

subgraph X4["Dummy Boundary Wiring 2"]
direction TB
X1["Dummy Boundary Action 2"]
X2["DUMMY Letter Count Policy"]
X3["DUMMY Log Results Mechanism"]
X3 --> EES1
X3 --> EES0
X1--"Dummy Space 1"--->X2
X2--"Dummy Space 2"--->X3
end
```

```mermaid
graph TB

subgraph SVS["State Variables"]
EE0[("Dummy")]
EES0(["Total Length"])
EES0 --- EE0
EES1(["Words"])
EES1 --- EE0
end

subgraph X4["Dummy Control Wiring"]
direction TB
X1["Dummy Control Action"]
X2["DUMMY Letter Count Policy"]
X3["DUMMY Log Results Mechanism"]
X3 --> EES1
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
1. [[DUMMY Letter Count Policy]]
2. [[DUMMY Log Results Mechanism]]
3. [[Dummy Boundary Action]]
4. [[Dummy Boundary Action 2]]
5. [[Dummy Control Action]]

## Unique Parameters Used
1. [[DUMMY D Probability]]
2. [[DUMMY Length Multiplier]]

