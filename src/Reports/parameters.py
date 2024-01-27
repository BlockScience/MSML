from ..Classes import MathSpec
from typing import List


def write_out_params(ms: MathSpec, params: List[str]) -> str:
    out = "<h2>Parameters</h2>"
    for name in params:
        out += "<h3>{}</h3>".format(name)
        param = ms.parameters.parameter_map[name]
        out += "<p>Description: {}</p>".format(param.description)
        out += "<p>Symbol: {}</p>".format(param.symbol)
        out += "<p>Domain: {}</p>".format(param.domain)
        out += "<p>Parameter Class: {}</p>".format(param.parameter_class)

    return out
