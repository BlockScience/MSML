import os
from .state import write_state_section
from inspect import signature, getsource, getfile, getsourcelines


def get_source_code(
    ms,
    component_type,
    implementation_name,
):
    if implementation_name in ms.implementations["python"][component_type]:
        code = ms.implementations["python"][component_type][implementation_name]
    else:
        return None
    source_code = """```python
{}```""".format(
        getsource(code)
    )
    file_path = getfile(code) + "#L{}".format(getsourcelines(code)[1])
    return source_code, file_path


def write_entity_markdown_report(ms, path, entity, add_metadata=True):
    entity = ms.entities[entity]
    if "Entities" not in os.listdir(path):
        os.makedirs(path + "/Entities")
    out = ""
    if add_metadata:
        metadata = entity.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )
    out += "## Notes"
    out += "\n"
    out += entity.notes
    out += "\n"
    out += "## State"
    out += "\n"
    out += write_state_section(entity.state, links=True)
    out += "\n"
    out += "\n"
    out += "## Boundary Actions"
    out += "\n"
    for ba in entity.boundary_actions:
        out += "### [[{}]]".format(ba.name)
        out += "\n"
    out += "## Mechanisms Impacting the Entity"
    out += "\n"
    for mc in entity.impacted_by_mechanism:
        out += "### [[{}]]".format(mc.name)
        out += "\n"
    out += "## Actions Impacting the Entity"
    out += "\n"
    for ac in entity.impacted_by_actions:
        out += "### [[{}]]".format(ac.name)
        out += "\n"

    path = "{}/Entities/{}.md".format(path, entity.name)
    out = write_source_code_block(entity, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_source_code_block(component, text, path):
    if hasattr(component, "source_code_location"):
        file_path = component.source_code_location
    else:
        file_path = component["Source Code Location"]
    if file_path:
        file_path = os.path.relpath(file_path, path)
        text += "## Spec Source Code Location\n\n"
        text += "Spec Path (only works if vault is opened at level including the src folder): [{}]({})".format(
            file_path, file_path
        )
        text += "\n\n"
    return text


def write_state_markdown_report(ms, path, state, add_metadata=True):
    state = ms.state[state]
    if "States" not in os.listdir(path):
        os.makedirs(path + "/States")
    out = ""
    if add_metadata:
        metadata = state.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    out += write_state_section(state, links=True)
    out += "\n"
    out += "\n"
    out += "## Updated By"
    out += "\n"
    for ba in state.updated_by:
        out += "### [[{}]]".format(ba.name)
        out += "\n"

    path = "{}/States/{}.md".format(path, state.name)
    out = write_source_code_block(state, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_types_markdown_report(ms, path, t, add_metadata=True):
    # t = ms.types[t]
    if "Types" not in os.listdir(path):
        os.makedirs(path + "/Types")
    out = ""
    if add_metadata:
        metadata = t.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    out += "## Type"
    out += "\n"

    if "python" in t.type:
        out += "### Python Type\n"
        out += t.type_name["python"]
        out += "\n"
    if "typescript" in t.type:
        out += "### Typescript Type\n"
        out += t.type_name["typescript"]
        out += "\n"
    if "julia" in t.type:
        out += "### Julia Type\n"
        out += t.type_name["julia"]
        out += "\n"
    out += "\n"
    out += "## Notes"
    out += "\n\n"
    out += t.notes
    out += "\n"

    path = "{}/Types/{}.md".format(path, t.name)
    out = write_source_code_block(t, out, path)
    with open(path, "w") as f:
        f.write(out)


def write_boundary_action_markdown_report(ms, path, boundary_action, add_metadata=True):
    boundary_action = ms.boundary_actions[boundary_action]
    if "Boundary Actions" not in os.listdir(path):
        os.makedirs(path + "/Boundary Actions")
    out = ""
    if add_metadata:
        metadata = boundary_action.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    out += "## Description"
    out += "\n"
    out += "\n"
    out += boundary_action.description
    out += "\n"

    out += "## Called By\n"
    for i, x in enumerate(boundary_action.called_by):
        out += "{}. [[{}]]".format(i + 1, x.label)
        out += "\n"
    out += "\n"

    out += "## Followed By\n"
    for i, x in enumerate([x[0] for x in boundary_action.calls]):
        out += "{}. [[{}]]".format(i + 1, x.label)
        out += "\n"
    out += "\n"

    out += "## Constraints\n"
    for i, x in enumerate(boundary_action.constraints):
        out += "{}. {}".format(i + 1, x)
        out += "\n"
    out += "\n"

    out += "## Codomain Spaces\n"
    for i, x in enumerate(boundary_action.codomain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Metrics Used\n"
    for i, x in enumerate(boundary_action.metrics_used):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Parameters Used\n"
    for i, x in enumerate(sorted(boundary_action.parameters_used, key=lambda x: x)):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"
    out += "\n"

    if boundary_action.boundary_action_options:
        out += "## Boundary Action Options:\n"
        for i, x in enumerate(boundary_action.boundary_action_options):
            out += "### {}. {}\n".format(i + 1, x.name)
            out += "#### Description\n"
            out += x.description
            out += "\n"

            out += "#### Logic\n"
            out += x.logic
            out += "\n"

            temp = get_source_code(ms, "boundary_action_options", x.name)
            if temp:
                source_code, file_path = temp
                file_path = os.path.relpath(
                    file_path, "{}/Boundary Actions".format(path)
                )
                out += "#### Python Implementation\n"
                out += source_code
                out += "\n"
                out += "Implementation Path (only works if vault is opened at level including the src folder): [{}]({})".format(
                    file_path, file_path
                )
                out += "\n"

            out += "\n"

    path = "{}/Boundary Actions/{}.md".format(path, boundary_action.label)
    out = write_source_code_block(boundary_action, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_policy_markdown_report(ms, path, policy, add_metadata=True):
    policy = ms.policies[policy]
    if "Policies" not in os.listdir(path):
        os.makedirs(path + "/Policies")

    out = ""
    if add_metadata:
        metadata = policy.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    out += "## Description"
    out += "\n"
    out += "\n"
    out += policy.description
    out += "\n"

    out += "## Called By\n"
    for i, x in enumerate(policy.called_by):
        x = x[0]
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "## Domain Spaces\n"
    for i, x in enumerate(policy.domain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "## Followed By\n"
    for i, x in enumerate(policy.calls):
        x = x[0]
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "## Codomain Spaces\n"
    for i, x in enumerate(policy.codomain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "## Constraints\n"
    for i, x in enumerate(policy.constraints):
        out += "{}. {}".format(i + 1, x)
        out += "\n"

    out += "## Parameters Used\n"
    for i, x in enumerate(sorted(policy.parameters_used, key=lambda x: x)):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"

    out += "## Metrics Used\n"
    for i, x in enumerate(policy.metrics_used):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    if policy.policy_options:
        out += "## Policy Options\n"
        for i, x in enumerate(policy.policy_options):
            out += "### {}. {}\n".format(i + 1, x.name)
            out += "#### Description\n"
            out += x.description
            out += "\n"

            out += "#### Logic\n"
            out += x.logic
            out += "\n"

            temp = get_source_code(ms, "policies", x.name)
            if temp:
                source_code, file_path = temp
                file_path = os.path.relpath(file_path, "{}/Policies".format(path))
                out += "#### Python Implementation\n"
                out += source_code
                out += "\n"
                out += "Implementation Path (only works if vault is opened at level including the src folder): [{}]({})".format(
                    file_path, file_path
                )
                out += "\n"

            out += "\n"

    path = "{}/Policies/{}.md".format(path, policy.label)
    out = write_source_code_block(policy, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_mechanism_markdown_report(ms, path, mechanism, add_metadata=True):
    mechanism = ms.mechanisms[mechanism]

    out = ""
    if add_metadata:
        metadata = mechanism.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )
    out += "## Description"
    out += "\n"
    out += "\n"
    out += mechanism.description
    out += "\n"

    if "Mechanisms" not in os.listdir(path):
        os.makedirs(path + "/Mechanisms")

    out += "## Called By\n"
    for i, x in enumerate(mechanism.called_by):
        x = x[0]
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "## Domain Spaces\n"
    for i, x in enumerate(mechanism.domain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "## Constraints\n"
    for i, x in enumerate(mechanism.constraints):
        out += "{}. {}".format(i + 1, x)
        out += "\n"

    out += "## Metrics Used\n"
    for i, x in enumerate(mechanism.metrics_used):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Parameters Used\n"
    for i, x in enumerate(sorted(mechanism.parameters_used, key=lambda x: x)):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"
    out += "\n"

    out += "## Logic\n"
    out += mechanism.logic

    out += "\n\n"
    out += "## Updates\n\n"
    for i, x in enumerate(mechanism.updates):
        out += "{}. [[{}]].[[{}|{}]]".format(
            i + 1, x[0].name, x[0].state.name + "-" + x[1].name, x[1].name
        )
        out += "\n"

    temp = get_source_code(ms, "mechanisms", mechanism.name)
    if temp:
        source_code, file_path = temp
        file_path = os.path.relpath(file_path, "{}/Mechanisms".format(path))
        out += "## Python Implementation\n"
        out += source_code
        out += "\n"
        out += "Implementation Path (only works if vault is opened at level including the src folder): [{}]({})".format(
            file_path, file_path
        )
        out += "\n"

    out += "\n"

    path = "{}/Mechanisms/{}.md".format(path, mechanism.label)
    out = write_source_code_block(mechanism, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_space_markdown_report(ms, path, space, add_metadata=True):
    space = ms.spaces[space]

    if "Spaces" not in os.listdir(path):
        os.makedirs(path + "/Spaces")

    out = ""
    if add_metadata:
        metadata = space.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    if space.description:
        out += "## Description"
        out += "\n"
        out += space.description
        out += "\n"
        out += "\n"

    out += "## Schema"
    out += "\n"
    out += "\n"
    d = space.schema
    d = ",\n".join(
        ["{}: [[{}]]".format(a, b.name) for a, b in zip(d.keys(), d.values())]
    )
    d = "{" + d + "}"
    out += d
    out += "\n\n"

    out += "## Blocks with Space in Domain"
    out += "\n"
    for i, x in enumerate(sorted(space.domain_blocks, key=lambda x: x.name)):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Blocks with Space in Codomain"
    out += "\n"
    for i, x in enumerate(sorted(space.codomain_blocks, key=lambda x: x.name)):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    path = "{}/Spaces/{}.md".format(path, space.name)
    out = write_source_code_block(space, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_control_action_markdown_report(ms, path, control_action, add_metadata=True):
    control_action = ms.control_actions[control_action]
    if "Control Actions" not in os.listdir(path):
        os.makedirs(path + "/Control Actions")
    out = ""
    if add_metadata:
        metadata = control_action.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    out += "## Description"
    out += "\n"
    out += "\n"
    out += control_action.description
    out += "\n"

    out += "## Followed By\n"
    for i, x in enumerate([x[0] for x in control_action.calls]):
        out += "{}. [[{}]]".format(i + 1, x.label)
        out += "\n"
    out += "\n"

    out += "## Constraints"
    for i, x in enumerate(control_action.constraints):
        out += "{}. {}".format(i + 1, x)
        out += "\n"

    out += "\n"
    out += "## Codomain Spaces\n"
    for i, x in enumerate(control_action.codomain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Metrics Used\n"
    for i, x in enumerate(control_action.metrics_used):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Parameters Used\n"
    for i, x in enumerate(sorted(control_action.parameters_used, key=lambda x: x)):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"
    out += "\n"

    if control_action.control_action_options:
        out += "## Control Action Options:\n"
        for i, x in enumerate(control_action.control_action_options):
            out += "### {}. {}\n".format(i + 1, x.name)
            out += "#### Description\n"
            out += x.description
            out += "\n"

            out += "#### Logic\n"
            out += x.logic
            out += "\n"

            temp = get_source_code(ms, "control_action_options", x.name)
            if temp:
                source_code, file_path = temp
                file_path = os.path.relpath(
                    file_path, "{}/Control Actions".format(path)
                )
                out += "#### Python Implementation\n"
                out += source_code
                out += "\n"
                out += "Implementation Path (only works if vault is opened at level including the src folder): [{}]({})".format(
                    file_path, file_path
                )
                out += "\n"

            out += "\n"

    path = "{}/Control Actions/{}.md".format(path, control_action.label)
    out = write_source_code_block(control_action, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_wiring_markdown_report(ms, path, wiring, add_metadata=True):
    wiring = ms.wiring[wiring]
    out = ""
    if "Wiring" not in os.listdir(path):
        os.makedirs(path + "/Wiring")
    if add_metadata:
        metadata = wiring.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )
    out += "## Wiring Diagram (Zoomed Out)"
    out += "\n"
    out += "\n"
    out += "- For display of only depth of 1 in the components/nested wirings\n"
    out += wiring.render_mermaid_root(go_deep="First")
    out += "\n"
    out += "\n"

    out += "## Wiring Diagram"
    out += "\n"
    out += "\n"
    out += wiring.render_mermaid_root()
    out += "\n"
    out += "\n"
    out += "## Description"
    out += "\n"
    out += "\n"
    out += "Block Type: {}".format(wiring.block_type)
    out += "\n"
    out += wiring.description
    out += "\n"

    out += "## Components\n"
    for i, x in enumerate(wiring.components):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "\n"

    out += "## All Blocks\n"
    for i, x in enumerate(sorted(wiring.components_full(), key=lambda x: x.name)):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "\n"

    out += "## Constraints\n"
    for i, x in enumerate(wiring.constraints):
        out += "{}. {}".format(i + 1, x)
        out += "\n"
    out += "\n"

    out += "## Domain Spaces\n"
    for i, x in enumerate(wiring.domain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Codomain Spaces\n"
    for i, x in enumerate(wiring.codomain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## All Spaces Used\n"
    for i, x in enumerate(sorted(wiring.all_spaces_used, key=lambda x: x.name)):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Metrics Used\n"
    for i, x in enumerate(wiring.metrics_used):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Parameters Used\n"
    for i, x in enumerate(sorted(wiring.parameters_used, key=lambda x: x)):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"
    out += "\n"

    out += "## Called By\n"
    for i, x in enumerate(wiring.called_by):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## Calls\n"
    for i, x in enumerate(wiring.calls):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    out += "## All State Updates\n"

    for i, x in enumerate(
        sorted(wiring.all_updates, key=lambda x: x[0].name + "-" + x[1].name)
    ):
        out += "{}. [[{}]].[[{}|{}]]".format(
            i + 1,
            x[0].name,
            ms.entities[x[0].name].state.name + "-" + x[1].name,
            x[1].name,
        )
        out += "\n"
    out += "\n"

    path = "{}/Wiring/{}.md".format(path, wiring.name)
    out = write_source_code_block(wiring, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_parameter_markdown_report(ms, path, parameter, add_metadata=True):
    param = ms.parameters.parameter_map[parameter]
    out = ""
    if "Parameters" not in os.listdir(path):
        os.makedirs(path + "/Parameters")
    if add_metadata:
        metadata = param.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    out += "Description: {}\n\n".format(param.description)
    out += "Type: [[{}]]\n\n".format(param.variable_type.name)
    out += "Symbol: {}\n\n".format(param.symbol)
    out += "Domain: {}\n\n".format(param.domain)
    out += "Parameter Class: {}\n\n".format(param.parameter_class)

    path = "{}/Parameters/{}.md".format(path, param.name)
    out = write_source_code_block(param, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_stateful_metrics_markdown_report(ms, path, metric, add_metadata=True):
    metric = ms.get_specific_stateful_metrics(metric)
    out = ""
    if "Stateful Metrics" not in os.listdir(path):
        os.makedirs(path + "/Stateful Metrics")
    if add_metadata:
        metadata = metric.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    out += "Description: {}\n\n".format(metric.description)
    out += "Type: [[{}]]\n\n".format(metric.type)
    out += "Symbol: {}\n\n".format(metric.symbol)
    out += "Domain: {}\n\n".format(metric.domain)

    out += "## Parameters Used\n"
    for i, x in enumerate(sorted(metric.parameters_used, key=lambda x: x)):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"
    out += "\n"

    out += "## Variables Used\n"
    for i, x in enumerate(metric.variables_used):
        out += "{}. [[{}]].{}".format(i + 1, x[0], x[1])
        out += "\n"
    out += "\n"

    temp = get_source_code(ms, "stateful_metrics", metric.name)
    if temp:
        source_code, file_path = temp
        file_path = os.path.relpath(file_path, "{}/Stateful Metrics".format(path))
        out += "## Python Implementation\n"
        out += source_code
        out += "\n"
        out += "Implementation Path (only works if vault is opened at level including the src folder): [{}]({})".format(
            file_path, file_path
        )
        out += "\n"

    out += "\n"

    path = "{}/Stateful Metrics/{}.md".format(path, metric.name)

    out = write_source_code_block(metric, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_metrics_markdown_report(ms, path, metric, add_metadata=True):
    metric = ms.metrics[metric]
    out = ""
    if "Metrics" not in os.listdir(path):
        os.makedirs(path + "/Metrics")
    if add_metadata:
        metadata = metric.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )

    out += "Description: {}\n\n".format(metric.description)
    out += "Type: [[{}]]\n\n".format(metric.type)
    out += "Symbol: {}\n\n".format(metric.symbol)

    out += "## Logic\n"
    out += metric.logic
    out += "\n\n"

    out += "## Parameters Used\n"
    for i, x in enumerate(sorted(metric.parameters_used, key=lambda x: x)):
        out += "{}. [[{}]]".format(i + 1, x)
        var = ms.parameters.parameter_map[x]
        if var.symbol:
            out += " , symbol: {}".format(var.symbol)
        out += "\n"
    out += "\n"

    out += "## Variables Used\n"
    for i, x in enumerate(metric.variables_used):
        out += "{}. [[{}]].[[{}-{}|{}]]".format(i + 1, x[0], x[0], x[1], x[1])
        var = ms.state[x[0]].variable_map[x[1]]
        if var.symbol:
            out += " , symbol: {}".format(var.symbol)
        out += "\n"
    out += "\n"

    out += "## Domain Spaces\n"
    for i, x in enumerate(metric.domain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    out += "## Metrics Used\n"
    for i, x in enumerate(metric.metrics_used):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"

    temp = get_source_code(ms, "metrics", metric.name)
    if temp:
        source_code, file_path = temp
        file_path = os.path.relpath(file_path, "{}/Metrics".format(path))
        out += "## Python Implementation\n"
        out += source_code
        out += "\n"
        out += "Implementation Path (only works if vault is opened at level including the src folder): [{}]({})".format(
            file_path, file_path
        )
        out += "\n"

    out += "\n"

    path = "{}/Metrics/{}.md".format(path, metric.name)
    out = write_source_code_block(metric, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_displays_markdown_reports(ms, path, add_metadata=True):
    if "Displays" not in os.listdir(path):
        os.makedirs(path + "/Displays")
    if "Wiring" not in os.listdir(path + "/Displays"):
        os.makedirs(path + "/Displays/Wiring")

    for wiring in ms.displays["Wiring"]:
        write_wiring_display_markdown_report(
            ms, path, wiring, add_metadata=add_metadata
        )


def write_state_variables_markdown_reports(ms, path, state, add_metadata=True):
    if "State Variables" not in os.listdir(path):
        os.makedirs(path + "/State Variables")
    state = ms.state[state]
    for variable in state.variables:
        out = ""
        if add_metadata:
            metadata = variable.metadata
            if len(metadata) > 0:
                out += """---
        {}
---
""".format(
                    "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
                )
        out += "Description: "
        out += variable.description
        out += "\n\n"
        out += "Underlying state: [[{}]]".format(state.name)
        out += "\n\n"
        out += "Type: [["
        out += variable.type.name
        out += "]]\n\n"
        out += "Symbol: "
        if variable.symbol:
            out += variable.symbol
        out += "\n\n"
        out += "Domain: "
        if variable.domain:
            out += variable.domain
        out += "\n\n"

        out += "Updated By:\n"
        for i, x in enumerate(sorted(variable.updated_by, key=lambda x: x.name)):
            out += "{}. [[{}]]".format(i + 1, x.name)
            out += "\n"
        out += "\n"

        with open(
            "{}/State Variables/{}.md".format(
                path, "{}-{}".format(state.name, variable.name)
            ),
            "w",
        ) as f:
            f.write(out)


def write_wiring_display_markdown_report(ms, path, wiring, add_metadata=True):
    wirings = [ms.wiring[w] for w in wiring["components"]]
    out = ""

    out += "## Wiring Diagrams"
    out += "\n"
    out += "\n"
    for w in wirings:
        out += w.render_mermaid_root()
        out += "\n"
        out += "\n"
    out += "## Description"
    out += "\n"
    out += "\n"
    out += wiring["description"]
    out += "\n"

    out += "## Wirings\n"
    for i, x in enumerate(wiring["components"]):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"
    out += "\n"

    out += "## Unique Components Used\n"
    components = [set(x.components_full()) for x in wirings]
    components = set().union(*components)
    components = sorted(components, key=lambda x: x.name)
    for i, x in enumerate(components):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    """domain = [set(x.domain) for x in wirings]
    domain = set().union(*domain)
    out += "## Unique Domain Spaces\n"
    for i, x in enumerate(domain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"

    codomain = [set(x.codomain) for x in wirings]
    codomain = set().union(*codomain)
    out += "## Unique Codomain Spaces\n"
    for i, x in enumerate(codomain):
        out += "{}. [[{}]]".format(i + 1, x.name)
        out += "\n"
    out += "\n"""

    parameters = [set(x.parameters_used) for x in wirings]
    parameters = set().union(*parameters)
    parameters = sorted(parameters, key=lambda x: x)
    out += "## Unique Parameters Used\n"
    for i, x in enumerate(sorted(parameters, key=lambda x: x)):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"
    out += "\n"

    path = "{}/Displays/Wiring/{}.md".format(path, wiring["name"])
    out = write_source_code_block(wiring, out, path)

    with open(path, "w") as f:
        f.write(out)


def write_all_markdown_reports(ms, path, clear_folders=False):
    if clear_folders:
        for x in [
            "Metrics",
            "Mechanisms",
            "Types",
            "Control Actions",
            "Spaces",
            "Boundary Actions",
            "Policies",
            "Wiring",
            "States",
            "Parameters",
            "Entities",
            "Stateful Metrics",
        ]:
            if os.path.exists("{}/{}".format(path, x)):
                for y in os.listdir("{}/{}".format(path, x)):
                    os.remove("{}/{}/{}".format(path, x, y))

    # Write entities
    entities = list(ms.entities.keys())
    for x in entities:
        write_entity_markdown_report(ms, path, x)

    # Write states
    states = list(ms.state.keys())
    for x in states:
        write_state_markdown_report(ms, path, x)
        write_state_variables_markdown_reports(ms, path, x)

    # Write types
    for t in ms.types.values():
        write_types_markdown_report(ms, path, t)

    # Write boundary actions
    boundary_actions = list(ms.boundary_actions.keys())
    for x in boundary_actions:
        write_boundary_action_markdown_report(ms, path, x)

    # Write policies
    policies = list(ms.policies.keys())
    for x in policies:
        write_policy_markdown_report(ms, path, x)

    # Write mechanisms
    mechanisms = list(ms.mechanisms.keys())
    for x in mechanisms:
        write_mechanism_markdown_report(ms, path, x)

    # Write spaces
    spaces = list(ms.spaces.keys())
    for x in spaces:
        write_space_markdown_report(ms, path, x)

    # Write control actions
    control_actions = list(ms.control_actions.keys())
    for x in control_actions:
        write_control_action_markdown_report(ms, path, x)

    # Write wiring
    wiring = list(ms.wiring.keys())
    for x in wiring:
        write_wiring_markdown_report(ms, path, x)

    # Write parameters
    parameters = ms.parameters.all_parameters
    for x in parameters:
        write_parameter_markdown_report(ms, path, x)

    # Write stateful metrics
    stateful_metrics = ms.get_all_stateful_metric_names()
    for x in stateful_metrics:
        write_stateful_metrics_markdown_report(ms, path, x)

    # Write metrics
    for x in ms.metrics:
        write_metrics_markdown_report(ms, path, x)

    # Write displays
    if ms.displays:
        write_displays_markdown_reports(ms, path, add_metadata=True)
