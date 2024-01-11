from ..Classes import Mechanism, MathSpec
from typing import List


def write_out_mechanism(mechanism: Mechanism) -> str:
    out = ""
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
        out += "{}. {}".format(i + 1, x.name)
        out += "</p>"

    out += "<h4>Domain Spaces:</h4>\n"
    for i, x in enumerate(mechanism.domain):
        out += "<p>"
        out += "{}. {}".format(i + 1, x.name)
        out += "</p>"

    out += "<h4>State Updates:</h4>\n"
    for i, x in enumerate(mechanism.updates):
        out += "<p>"
        out += "{}. {}.{}".format(i + 1, x[0].name, x[1].name)
        out += "</p>"

    out += "<h4>Constraints:</h4>\n"
    for i, x in enumerate(mechanism.constraints):
        out += "<p>"
        out += "{}. {}\n".format(i + 1, x)
        out += "</p>"

    out += "<h4>Logic:</h4>\n"
    out += "<p>"
    out += mechanism.logic
    out += "</p>"
    return out


def write_out_mechanisms(ms: MathSpec, mechanism_names: List[str]) -> str:
    out = "<h2>Mechanisms</h2>"
    for name in mechanism_names:
        out += write_out_mechanism(ms.mechanisms[name])

    return out
