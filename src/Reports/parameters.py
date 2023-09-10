from ..Classes import MathSpec
from typing import List



def write_out_params(ms: MathSpec, params: List[str]) -> str:
    out = "<h2>Parameters</h2>"
    for name in params:
        out += "<p>{}</p>".format(name)

    return out