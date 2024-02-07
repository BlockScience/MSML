import os


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
    out += entity.state.name
    out += "\n"
    out += "## Boundary Actions"
    out += "\n"
    for ba in entity.boundary_actions:
        out += "### [[{}]]".format(ba.name)
        out += "\n"

    with open("{}/Entities/{}.md".format(path, entity.name), "w") as f:
        f.write(out)

    """

        # Boundary actions are added during parsing
        self.boundary_actions = []
        self.impacted_by_mechanism = []
        self.impacted_by_actions = []"""
