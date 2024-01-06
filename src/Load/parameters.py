from typing import Dict
from ..Classes import ParameterContainer, ParameterSet
from .general import check_json_keys


def convert_parameter_set(data: Dict) -> ParameterSet:
    # Check the keys are correct
    check_json_keys(data, "Parameter Set")

    return data


def load_parameters(ms: Dict, json: Dict) -> None:
    """Function to load parameters into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Parameters"] = {}

    # Convert parameter sets
    for key in json["Parameters"]:
        ms["Parameters"][key] = convert_parameter_set(json["Parameters"][key])

    # Placeholder for now
    ms["Parameters"] = ParameterContainer(ms["Parameters"])
