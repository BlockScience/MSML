from ..Classes import MathSpec
from .spaces import write_out_spaces
from .boundary_actions import write_out_boundary_actions
from .control_actions import write_out_control_actions
from .policies import write_out_policies
from .mechanisms import write_out_mechanisms
from .general import load_svg_graphviz, write_header
from .node_map import create_action_chains_graph
from .parameters import write_out_params
from .state import write_local_state_variable_tables
from typing import List


def write_basic_report_full(ms: MathSpec, directory: str, name: str) -> None:
    out = ""
    out += write_header()
    out += "<h2>Action Maps</h2>"
    behaviors = list(ms.boundary_actions.keys()) + list(ms.control_actions.keys())
    for behavior in behaviors:
        out += load_svg_graphviz(create_action_chains_graph(ms, [behavior], behavior))

    out += "<h2>State</h2>"
    out += write_local_state_variable_tables(ms.state.values())

    out += write_out_spaces(ms, list(ms.spaces.keys()))
    out += write_out_boundary_actions(ms, list(ms.boundary_actions.keys()))
    out += write_out_control_actions(ms, list(ms.control_actions.keys()))
    out += write_out_policies(ms, list(ms.policies.keys()))
    out += write_out_mechanisms(ms, list(ms.mechanisms.keys()))
    out += write_out_params(ms, list(ms.parameters.all_parameters))

    with open("{}/{}.html".format(directory, name), "w") as f:
        f.write(out)


def write_action_chain_reports(
    ms: MathSpec, directory: str, actions: List[str]
) -> None:
    """Function to write reports on each action chain specified

    Args:
        ms (MathSpec): The mathematical specification object
        directory (str): Directory to put reports into
        actions (List[str]): List of actions to create reports on
    """

    for action in actions:
        all_nodes = ms.crawl_action_chains([action])
        out = ""
        out += write_header()
        out += "<h2>Action Map</h2>"
        out += load_svg_graphviz(create_action_chains_graph(ms, [action], action))

        out += "<h2>State</h2>"
        out += write_local_state_variable_tables(all_nodes["State"])

        out += write_out_spaces(ms, [x.__name__ for x in all_nodes["Spaces"]])
        out += write_out_boundary_actions(
            ms, [x.name for x in all_nodes["Boundary Actions"]]
        )
        out += write_out_control_actions(
            ms, [x.name for x in all_nodes["Control Actions"]]
        )
        out += write_out_policies(ms, [x.name for x in all_nodes["Policies"]])
        out += write_out_mechanisms(ms, [x.name for x in all_nodes["Mechanisms"]])
        out += write_out_params(ms, all_nodes["Parameters"])

        with open("{}/{}.html".format(directory, action), "w") as f:
            f.write(out)


def write_entity_reports(ms: MathSpec, directory: str, entities: List[str]) -> None:
    """Function to write reports on each entity specified

    Args:
        ms (MathSpec): The mathematical specification object
        directory (str): Directory to put reports into
        entities (List[str]): List of entities to create reports on
    """

    for entity in entities:
        entity_obj = ms.entities[entity]
        actions = list(
            set(entity_obj.boundary_actions + entity_obj.impacted_by_actions)
        )
        actions = [x.name for x in actions]
        all_nodes = ms.crawl_action_chains(actions)
        out = ""
        out += write_header()
        out += "<h2>Action Map</h2>"
        out += load_svg_graphviz(create_action_chains_graph(ms, actions, entity))

        out += "<h2>State</h2>"
        out += write_local_state_variable_tables(all_nodes["State"])

        out += write_out_spaces(ms, [x.__name__ for x in all_nodes["Spaces"]])
        out += write_out_boundary_actions(
            ms, [x.name for x in all_nodes["Boundary Actions"]]
        )
        out += write_out_control_actions(
            ms, [x.name for x in all_nodes["Control Actions"]]
        )
        out += write_out_policies(ms, [x.name for x in all_nodes["Policies"]])
        out += write_out_mechanisms(ms, [x.name for x in all_nodes["Mechanisms"]])
        out += write_out_params(ms, all_nodes["Parameters"])

        with open("{}/{}.html".format(directory, entity), "w") as f:
            f.write(out)


def write_spec_tree(ms: MathSpec) -> str:
    """Write the tree of the specification structure

    Args:
        ms (MathSpec): The mathematical specification object

    Returns:
        str: The string representation of the tree
    """

    symbol1 = "├──"
    symbol2 = "│   ├──"
    symbol3 = "│   │   ├──"

    out = ""
    out += symbol1 + "Entities\n"
    for name in ms.entities.keys():
        out += symbol2 + name + "\n"

    out += symbol1 + "State\n"
    for name in ms.state.keys():
        out += symbol2 + name + "\n"
        for var in ms.state[name].variable_map.keys():
            out += symbol3 + var + "\n"

    out += symbol1 + "Stateful Metrics\n"
    for name in ms.stateful_metrics.keys():
        out += symbol2 + name + "\n"
        for var in ms.stateful_metrics[name].metrics:
            out += symbol3 + var.name + "\n"

    out += symbol1 + "Spaces\n"
    for name in ms.spaces.keys():
        out += symbol2 + name + "\n"
    out += symbol1 + "Parameters\n"
    for name in ms.parameters.data.keys():
        out += symbol2 + name + "\n"
        for param in [x.name for x in ms.parameters.data[name].parameters]:
            out += symbol3 + param + "\n"

    out += symbol1 + "Boundary Actions\n"
    for name in ms.boundary_actions.keys():
        out += symbol2 + name + "\n"

    out += symbol1 + "Control Actions\n"
    for name in ms.control_actions.keys():
        out += symbol2 + name + "\n"

    out += symbol1 + "Policies\n"
    for name in ms.policies.keys():
        out += symbol2 + name + "\n"

    out += symbol1 + "Mechanisms\n"
    for name in ms.mechanisms.keys():
        out += symbol2 + name + "\n"

    return out
