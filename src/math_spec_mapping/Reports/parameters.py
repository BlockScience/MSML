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


def write_parameter_table_markdown(
    ms, initial_values=None, links=False, compress_arrays=False
):
    if initial_values:
        table = """| Name | Description | Parameter Class | Symbol | Domain | Initial Value |
| --- | --- | --- | --- | --- | --- |
"""
    else:
        table = """| Name | Description | Parameter Class | Symbol | Domain |
| --- | --- | --- | --- | --- |
"""

    for name in ms.parameters.parameter_map:
        var = ms.parameters.parameter_map[name]
        table_vars = [
            var.name,
            var.description,
            var.parameter_class,
            var.symbol,
            var.domain,
        ]
        table += "|"
        for i, tv in enumerate(table_vars):
            if tv:
                if links and i == 0:
                    table += "[[{}\|{}]]".format(tv, tv)
                else:
                    table += "{}".format(tv)
            table += "|"
        if initial_values:
            if compress_arrays:
                iv = initial_values[var.name]
                if type(iv) == list:
                    if len(iv) > 4:
                        iv = "[{}, {}, ... , {}, {}]".format(
                            iv[0], iv[1], iv[-2], iv[-1]
                        )
                table += " {} |".format(iv)
            else:
                table += " {} |".format(initial_values[var.name])

        table += "\n"

    return table
