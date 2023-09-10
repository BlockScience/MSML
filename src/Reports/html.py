from ..Classes import MathSpec
from .spaces import write_out_spaces
from .boundary_actions import write_out_boundary_actions
from .policies import write_out_policies
from .mechanisms import write_out_mechanisms
from .general import load_svg_graphviz
from .node_map import create_action_chains_graph
from typing import List


def write_basic_report_full(ms: MathSpec, directory: str, name: str) -> None:
    out = ""
    out += "<h2>Action Maps</h2>"
    behaviors = list(ms.boundary_actions.keys())
    for behavior in behaviors:
        out += load_svg_graphviz(create_action_chains_graph(ms,
                                                            [behavior], behavior))
    out += write_out_spaces(ms, list(ms.spaces.keys()))
    out += write_out_boundary_actions(ms, behaviors)
    out += write_out_policies(ms, list(ms.policies.keys()))
    out += write_out_mechanisms(ms, list(ms.mechanisms.keys()))

    with open("{}/{}.html".format(directory, name), "w") as f:
        f.write(out)


def write_action_chain_reports(ms: MathSpec, directory: str, actions: List[str]) -> None:
    """Function to write reports on each action chain specified

    Args:
        ms (MathSpec): The mathematical specification object
        directory (str): Directory to put reports into
        actions (List[str]): List of actions to create reports on
    """

    for action in actions:
        all_nodes = ms.crawl_action_chains([action])
        out = ""
        out += "<h2>Action Map</h2>"
        out += load_svg_graphviz(create_action_chains_graph(ms,
                                                                [action], action))
        out += write_out_spaces(ms, [x.__name__ for x in all_nodes["Spaces"]])
        out += write_out_boundary_actions(ms, [x.name for x in all_nodes["Boundary Actions"]])
        out += write_out_policies(ms, [x.name for x in all_nodes["Policies"]])
        out += write_out_mechanisms(ms, [x.name for x in all_nodes["Mechanisms"]])

        with open("{}/{}.html".format(directory, action), "w") as f:
            f.write(out)