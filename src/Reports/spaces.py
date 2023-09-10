from ..Classes import MathSpec
from typing import List, TypedDict


def write_out_space(space: TypedDict) -> str:
    """out = ""
    out += "<h3>"
    out += mechanism.label
    out += "</h3>"
    out += "<p>"
    out += mechanism.description
    out += "</p>"

    out += "<h4>Preceded By:</h4>\n"
    for i, x in enumerate(mechanism.called_by):
        x = x[0]
        out += "<p>"
        out += "{}. {}".format(i+1, x.name)
        out += "</p>"

    out += "<h4>Domain Spaces:</h4>\n"
    for i, x in enumerate(mechanism.domain):
        out += "<p>"
        out += "{}. {}".format(i+1, x.__name__)
        out += "</p>"

    out += "<h4>State Updates:</h4>\n"
    for i, x in enumerate(mechanism.updates):
        out += "<p>"
        out += "{}. {}.{}".format(i+1, x[0].name, x[1].name)
        out += "</p>"

    out += "<h4>Constraints:</h4>\n"
    for i, x in enumerate(mechanism.constraints):
        out += "<p>"
        out += "{}. {}\n".format(i+1, x)
        out += "</p>"

    out += "<h4>Logic:</h4>\n"
    out += "<p>"
    out += mechanism.logic
    out += "</p>"
    return out"""
    return "<p>HOLD</p>"


def write_out_spaces(ms: MathSpec, spaces: List[str]) -> str:
    out = "<h2>Spaces</h2>"
    for name in spaces:
        out += write_out_space(ms.spaces[name])

    return out