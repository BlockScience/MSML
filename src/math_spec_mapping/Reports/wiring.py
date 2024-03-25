from ..Classes import MathSpec
from .spaces import write_out_spaces
from .boundary_actions import write_out_boundary_actions
from .control_actions import write_out_control_actions
from .policies import write_out_policies
from .mechanisms import write_out_mechanisms
from .general import load_svg_graphviz, write_header
from .node_map import create_action_chains_graph
from .parameters import write_out_params
from .state import write_local_state_variable_tables, write_global_state_variable_table
from typing import List


def write_wiring_report(ms: MathSpec, directory: str, wiring_name) -> None:
    all_nodes = ms.crawl_wiring(wiring_name)
    wiring = ms.wiring[wiring_name]
    out = ""
    # out += write_header()
    # out += "\n"
    # out += "\n"
    out += "## Wiring Diagram"
    out += "\n"
    out += "\n"
    out += wiring.render_mermaid_root()
    out += "\n"
    out += "\n"
    out += "## State\n"
    out += write_global_state_variable_table(ms.state["Global State"])
    out += write_local_state_variable_tables(all_nodes["State"])
    out += write_out_spaces(ms, [x.name for x in all_nodes["Spaces"]])
    out += write_out_boundary_actions(
        ms, [x.name for x in all_nodes["Boundary Actions"]]
    )
    out += write_out_control_actions(ms, [x.name for x in all_nodes["Control Actions"]])
    out += write_out_policies(ms, [x.name for x in all_nodes["Policies"]])
    out += write_out_mechanisms(ms, [x.name for x in all_nodes["Mechanisms"]])
    out += write_out_params(ms, all_nodes["Parameters"])

    with open("{}/{}.md".format(directory, wiring_name), "w") as f:
        f.write(out)
