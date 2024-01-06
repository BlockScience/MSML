from typing import Dict
from ..Classes import ParameterContainer, ParameterSet, Parameter
from .general import check_json_keys


def convert_parameter_set(data: Dict) -> ParameterSet:
    # Check the keys are correct
    check_json_keys(data, "Parameter Set")

    # Copy
    data = data.copy()

    # Convert the parameters
    new_parameters = []
    for param in data["parameters"]:
        check_json_keys(param, "Parameter")
        new_parameters.append(Parameter(param))
    data["parameters"] = new_parameters

    # Build the state object
    return ParameterSet(data)


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
