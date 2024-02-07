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
    out += t.__repr__()

    with open("{}/Types/{}.md".format(path, t.__name__), "w") as f:
        f.write(out)
