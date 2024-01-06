from typing import Dict
from ..Classes import ParameterContainer


def load_parameters(ms: Dict, json: Dict) -> None:
    """Function to load parameters into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Parameters"] = {}

    # Convert parameter sets
    for key in json["Parameters"]:
        ms["Parameters"][key] = json["Parameters"][key]

    # Placeholder for now
    ms["Parameters"] = ParameterContainer(ms["Parameters"])
