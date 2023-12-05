```mermaid
graph
subgraph X4[Simulation 1]
X1[A]
X2[B]
X3[C]
X1-->X2
X2-->X3
end
```

```mermaid
graph
subgraph X4[Simulation 2]
X1[A]
X2[B]
X3[C]
X1 ~~~ X2
X2 ~~~ X3
end
```

```mermaid
graph
subgraph X8[Simulation 3]
subgraph X3[Parallel Block]
X1[A]
X2[B]
X1 ~~~ X2
end
subgraph X6[Stack Block]
X4[C]
X5[D]
X4-->X5
end
X7[E]
X3-->X6
X6-->X7
end
```


