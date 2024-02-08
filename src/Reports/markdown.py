import os
from .state import write_state_section


def write_entity_markdown_report(ms, path, entity):
    entity = ms.entities[entity]
    if "Entities" not in os.listdir(path):
        os.makedirs(path + "/Entities")
    out = ""
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


def write_state_markdown_report(ms, path, state):
    state = ms.state[state]
    if "States" not in os.listdir(path):
        os.makedirs(path + "/States")
    out = ""
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


def write_types_markdown_report(ms, path, t):
    # t = ms.types[t]
    if "Types" not in os.listdir(path):
        os.makedirs(path + "/Types")
    out = "## Type"
    out += "\n"
    out += str(t.__supertype__)

    with open("{}/Types/{}.md".format(path, t.__name__), "w") as f:
        f.write(out)


def write_boundary_action_markdown_report(ms, path, boundary_action):
    boundary_action = ms.boundary_actions[boundary_action]
    if "Boundary Actions" not in os.listdir(path):
        os.makedirs(path + "/Boundary Actions")

    out = ""
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

    if boundary_action.boundary_action_options:
        out += "## Boundary Action Options:\n"
        for i, x in enumerate(boundary_action.boundary_action_options):
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

    with open(
        "{}/Boundary Actions/{}.md".format(path, boundary_action.label), "w"
    ) as f:
        f.write(out)


def write_policy_markdown_report(ms, path, policy):
    policy = ms.policies[policy]
    if "Policies" not in os.listdir(path):
        os.makedirs(path + "/Policies")

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

    with open("{}/Policies/{}.md".format(path, policy.label), "w") as f:
        f.write(out)


def write_mechanism_markdown_report(ms, path, mechanism):
    mechanism = ms.mechanisms[mechanism]

    out = ""
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

    with open("{}/Mechanisms/{}.md".format(path, mechanism.label), "w") as f:
        f.write(out)
