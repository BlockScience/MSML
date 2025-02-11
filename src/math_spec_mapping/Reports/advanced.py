from ..Classes import MathSpec
from .state import write_state_section


def write_glossary_report(ms: MathSpec, directory: str) -> None:
    """Function to write a report of each component and its description in MSML

    Args:
        ms (MathSpec): The mathematical specification object
        directory (str): Directory to put reports into
    """
    out = "# Glossary\n\n"

    out += "## Entities\n\n"
    for entity in ms.entities:
        if entity == "Global":
            continue
        entity = ms.entities[entity]
        out += "**{}**: {}".format(entity.name, entity.notes)
        out += "\n\n"
    out += "\n"

    out += "## State\n\n"
    states = list(ms.state.keys())
    states.remove("Global State")
    states = ["Global State"] + states
    for state in states:
        out += "### {}\n\n".format(state)
        out += write_state_section(ms.state[state])
        out += "\n\n"
    out += "\n\n"

    for name, component in [
        ["Types", ms.types],
        ["Spaces", ms.spaces],
        ["Boundary Actions", ms.boundary_actions],
        ["Control Actions", ms.control_actions],
        ["Policies", ms.policies],
        ["Mechanisms", ms.mechanisms],
        ["Wiring", ms.wiring],
    ]:
        out += "## {}\n\n".format(name)
        for key in component:
            if hasattr(component[key], "description"):
                desc = component[key].description
            else:
                desc = component[key].notes

            out += "**{}**: {}\n\n".format(key, desc)
        out += "\n\n"

    path = directory + "/Glossary.md"
    with open(path, "w") as f:
        f.write(out)
