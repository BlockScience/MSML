## Wiring Diagram

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

## State
<h3>Global State</h3><table>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
        <th>Symbol</th>
        <th>Domain</th>
      </tr></table><h3>Local States</h3><h4>Dummy State</h4><table>
      <tr>
        <th>Name</th>
        <th>Description</th>
        <th>Type</th>
        <th>Symbol</th>
        <th>Domain</th>
      </tr><tr><td>Variable A</td><td>Variable A</td><td>Dummy Compound Type</td><td></td><td></td></tr><tr><td>Variable B</td><td>Variable B</td><td>Dummy Type 1</td><td></td><td></td></tr><tr><td>Variable C</td><td>Variable C</td><td>Dummy Type 2</td><td></td><td></td></tr></table><h2>Spaces</h2><h3>Terminating Space</h3><p>{}</p><h3>Dummy Space 2</h3><p>{a: Dummy Type 1,<br/>b: Dummy Type 1,<br/>c: Dummy Type 2}</p><h3>Dummy Space 1</h3><p>{a: Dummy Type 1}</p><h2>Behavioral Action Space</h2><h3>Dummy Boundary Action</h3><p>Dummy</p><h4>Called By:</h4>
<p>1. Dummy</p><h4>Constraints:</h4>
<h4>Boundary Action Options:</h4>
<details><summary><b>1. V1 Dummy Boundary</b></summary><p>Description</p><p>Logic: A+B=C</p></details><br/><h2>Control Action Space</h2><h2>Policies</h2><h3>Dummy Policy</h3><p>Dummy Policy</p><h4>Preceded By:</h4>
<p>1. Dummy Boundary Action</p><p>2. Dummy Control Action</p><h4>Domain Spaces:</h4>
<p>1. Dummy Space 1</p><h4>Followed By:</h4>
<p>1. Dummy Mechanism</p><p>2. Dummy Mechanism</p><h4>Codomain Spaces:</h4>
<p>1. Dummy Space 2</p><h4>Constraints:</h4>
<h4>Policy Options:</h4>
<details><summary><b>1. Dummy Policy V1</b></summary><p>V1 Dummy Policy</p><p>Logic: 
Dummy
Dummy
Dummy
</p></details><br/><h2>Mechanisms</h2><h3>Dummy Mechanism</h3><p>Dummy Mechanism</p><h4>Preceded By:</h4>
<p>1. Dummy Policy</p><p>2. Dummy Policy</p><h4>Domain Spaces:</h4>
<p>1. Dummy Space 2</p><h4>State Updates:</h4>
<p>1. Dummy.Variable A</p><h4>Constraints:</h4>
<p>1. Constaint 1
</p><h4>Logic:</h4>
<p>Logic for update</p><h2>Parameters</h2><h3>dummy_parameter</h3><p>Description: </p><p>Symbol: None</p><p>Domain: None</p><p>Parameter Class: Behavioral</p>