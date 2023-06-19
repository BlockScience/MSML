from ..Classes import MathSpec
from .boundary_actions import write_out_boundary_actions
from .policies import write_out_policies
from .mechanisms import write_out_mechanisms
from .general import load_svg_graphviz
from .node_map import create_action_chains_graph


def write_basic_report_full(ms: MathSpec, directory: str, name: str) -> None:
    out = ""
    out += "<h2>Action Maps</h2>"
    behaviors = list(ms.boundary_actions.keys())
    for behavior in behaviors:
        out += load_svg_graphviz(create_action_chains_graph(ms,
                                                            [behavior], behavior))

    out += write_out_boundary_actions(ms, behaviors)
    out += write_out_policies(ms, list(ms.policies.keys()))
    out += write_out_mechanisms(ms, list(ms.mechanisms.keys()))

    with open("{}/{}.html".format(directory, name), "w") as f:
        f.write(out)
