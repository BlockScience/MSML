from ..Classes import MathSpec
from typing import List, TypedDict


def write_out_space(space: TypedDict) -> str:
    out = ""
    out += "<h3>"
    out += space.__name__
    out += "</h3>"

    d = space.__annotations__
    d = ",<br/>".join(["{}: {}".format(a, b.__name__) for a,b in zip(d.keys(), d.values())])
    d = "{" + d + "}"

    out += "<p>"
    out += d
    out += "</p>"

    return out


def write_out_spaces(ms: MathSpec, spaces: List[str]) -> str:
    out = "<h2>Spaces</h2>"
    for name in spaces:
        out += write_out_space(ms.spaces[name])

    return out