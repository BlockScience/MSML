from typing import List
from ..Classes import ControlAction


def write_out_control_action(control_action: ControlAction) -> str:
    out = ""
    out += "<h3>"
    out += control_action.label
    out += "</h3>"
    out += "<p>"
    out += control_action.description
    out += "</p>"

    out += "<h4>Constraints:</h4>\n"
    for i, x in enumerate(control_action.constraints):
        out += "<p>"
        out += "{}. {}".format(i+1, x)
        out += "</p>"
    if control_action.control_action_options:
        out += "<h4>Control Action Options:</h4>\n"
        for i, x in enumerate(control_action.control_action_options):
            out += "<details>"
            out += "<summary><b>{}. {}</b></summary>".format(i+1, x.name)
            out += "<p>"
            out += x.description
            out += "</p>"

            out += "<p>"
            out += "Logic: {}".format(x.logic)
            out += "</p>"

            out += "</details>"
        out += "<br/>"
    return out


def write_out_control_actions(ms: dict, action_names: List[str]) -> str:
    out = "<h2>Control Action Space</h2>"
    for name in action_names:
        out += write_out_control_action(ms.control_actions[name])

    return out
