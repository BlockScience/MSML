from ..Classes import MathSpec
from .boundary_actions import write_out_boundary_actions
from .policies import write_out_policies
from .mechanisms import write_out_mechanisms


def write_basic_report_full(ms: MathSpec, directory: str, name: str) -> None:
    out = ""
    out += write_out_boundary_actions(ms, list(ms.boundary_actions.keys()))
    out += write_out_policies(ms, list(ms.policies.keys()))
    out += write_out_mechanisms(ms, list(ms.mechanisms.keys()))

    with open("{}/{}.html".format(directory, name), "w") as f:
        f.write(out)
