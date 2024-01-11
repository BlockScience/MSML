from typing import List
from ..Classes import Policy


def write_out_policy(policy: Policy) -> str:
    out = ""
    out += "<h3>"
    out += policy.label
    out += "</h3>"
    out += "<p>"
    out += policy.description
    out += "</p>"

    out += "<h4>Preceded By:</h4>\n"
    for i, x in enumerate(policy.called_by):
        x = x[0]
        out += "<p>"
        out += "{}. {}".format(i + 1, x.name)
        out += "</p>"

    out += "<h4>Domain Spaces:</h4>\n"
    for i, x in enumerate(policy.domain):
        out += "<p>"
        out += "{}. {}".format(i + 1, x.name)
        out += "</p>"

    out += "<h4>Followed By:</h4>\n"
    for i, x in enumerate(policy.calls):
        x = x[0]
        out += "<p>"
        out += "{}. {}".format(i + 1, x.name)
        out += "</p>"

    out += "<h4>Codomain Spaces:</h4>\n"
    for i, x in enumerate(policy.codomain):
        out += "<p>"
        out += "{}. {}".format(i + 1, x.name)
        out += "</p>"

    out += "<h4>Constraints:</h4>\n"
    for i, x in enumerate(policy.constraints):
        out += "<p>"
        out += "{}. {}\n".format(i + 1, x)
        out += "</p>"

    if policy.policy_options:
        out += "<h4>Policy Options:</h4>\n"
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
    return out


def write_out_policies(ms: dict, policy_names: List[str]) -> str:
    out = "<h2>Policies</h2>"
    for name in policy_names:
        out += write_out_policy(ms.policies[name])
    return out
