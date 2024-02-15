import os
from .state import write_state_section


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

    with open("{}/Entities/{}.md".format(path, entity.name), "w") as f:
        f.write(out)


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

    with open("{}/States/{}.md".format(path, state.name), "w") as f:
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
    out += str(t.type)
    out += "\n\n"
    out += "## Notes"
    out += "\n\n"
    out += t.notes

    with open("{}/Types/{}.md".format(path, t.name), "w") as f:
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

    out += "## Constraints"
    for i, x in enumerate(boundary_action.constraints):
        out += "{}. {}".format(i + 1, x)
        out += "\n"
    out += "\n"

    out += "## Codomain Spaces\n"
    for i, x in enumerate(boundary_action.codomain):
        out += "{}. [[{}]]".format(i + 1, x.name)
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
            out += "\n\n"

    with open(
        "{}/Boundary Actions/{}.md".format(path, boundary_action.label), "w"
    ) as f:
        f.write(out)


def write_policy_markdown_report(ms, path, policy, add_metadata=True):
    policy = ms.policies[policy]
    if "Policies" not in os.listdir(path):
        os.makedirs(path + "/Policies")
    if add_metadata:
        metadata = policy.metadata
        if len(metadata) > 0:
            out += """---
    {}
---
""".format(
                "\n".join(["{}: {}".format(x, metadata[x]) for x in metadata])
            )
    out = ""
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
        out += "{}. [[{}]]".format(i + 1, x)
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
            out += "\n\n"

    with open("{}/Policies/{}.md".format(path, policy.label), "w") as f:
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

    out += "## Logic\n"
    out += mechanism.logic

    out += "\n\n"
    out += "## Updates\n\n"
    for i, x in enumerate(mechanism.updates):
        out += "{}. [[{}]].{}".format(i + 1, x[0].name, x[1].name)
        out += "\n"

    with open("{}/Mechanisms/{}.md".format(path, mechanism.label), "w") as f:
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

    out += "## Schema"
    out += "\n"
    out += "\n"
    d = space.schema
    d = ",\n".join(["{}: {}".format(a, b.name) for a, b in zip(d.keys(), d.values())])
    d = "{" + d + "}"
    out += d
    out += "\n"

    with open("{}/Spaces/{}.md".format(path, space.name), "w") as f:
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

    if control_action.control_action_options:
        out += "## Control Action Options:\n"
        for i, x in enumerate(control_action.control_action_options):
            out += "<details>"
            out += "<summary><b>{}. {}</b></summary>".format(i + 1, x.name)
            out += "<p>"
            out += x.description
            out += "</p>"

            out += "<p>"
            out += "Logic: {}".format(x.logic)
            out += "</p>"

            out += "</details>"
        out += "<br/>"

    with open("{}/Control Actions/{}.md".format(path, control_action.label), "w") as f:
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

    out += "## Constraints"
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

    out += "## Parameters Used\n"
    for i, x in enumerate(wiring.parameters_used):
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

    with open("{}/Wiring/{}.md".format(path, wiring.name), "w") as f:
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
    out += "Symbol: {}\n\n".format(param.symbol)
    out += "Domain: {}\n\n".format(param.domain)
    out += "Parameter Class: {}\n\n".format(param.parameter_class)

    with open("{}/Parameters/{}.md".format(path, param.name), "w") as f:
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
    out += "Type: {}\n\n".format(metric.type)
    out += "Symbol: {}\n\n".format(metric.symbol)
    out += "Domain: {}\n\n".format(metric.domain)

    out += "## Parameters Used\n"
    for i, x in enumerate(metric.parameters_used):
        out += "{}. [[{}]]".format(i + 1, x)
        out += "\n"
    out += "\n"

    out += "## Parameters Used\n"
    for i, x in enumerate(metric.variables_used):
        out += "{}. {}.{}".format(i + 1, x[0], x[1])
        out += "\n"
    out += "\n"

    with open("{}/Stateful Metrics/{}.md".format(path, metric.name), "w") as f:
        f.write(out)


def write_all_markdown_reports(ms, path):

    # Write entities
    entities = list(ms.entities.keys())
    for x in entities:
        write_entity_markdown_report(ms, path, x)

    # Write states
    states = list(ms.state.keys())
    for x in states:
        write_state_markdown_report(ms, path, x)

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
