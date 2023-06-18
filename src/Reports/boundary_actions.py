from typing import List
from ..Classes import BoundaryAction


def write_out_boundary_action(boundary_action: BoundaryAction) -> str:
    out = ""
    out += "<h3>"
    out += boundary_action.label
    out += "</h3>"
    out += "<p>"
    out += boundary_action.description
    out += "</p>"
    out += "<h4>Called By:</h4>\n"
    for i, x in enumerate(boundary_action.called_by):
        out += "<p>"
        out += "{}. {}".format(i+1, x.label)
        out += "</p>"
    out += "<h4>Constraints:</h4>\n"
    for i, x in enumerate(boundary_action.constraints):
        out += "<p>"
        out += "{}. {}".format(i+1, x)
        out += "</p>"
    return out


def write_out_boundary_actions(ms: dict, action_names: List[str]) -> str:
    out = "<h2>Behavioral Action Space</h2>"
    for name in action_names:
        out += write_out_boundary_action(ms.boundary_actions[name])

    return out
