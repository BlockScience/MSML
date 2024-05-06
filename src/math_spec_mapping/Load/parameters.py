from typing import Dict
from ..Classes import ParameterContainer, ParameterSet, Parameter
from .general import check_json_keys


def convert_parameter_set(ms, data: Dict) -> ParameterSet:
    if "metadata" not in data:
        data["metadata"] = {}
    # Check the keys are correct
    check_json_keys(data, "Parameter Set")

    # Copy
    data = data.copy()

    # Convert the parameters
    new_parameters = []
    for param in data["parameters"]:
        if "metadata" not in param:
            param["metadata"] = {}
        check_json_keys(param, "Parameter")
        assert param["variable_type"] in ms["Types"], "Type of {} not in ms".format(
            param["variable_type"]
        )
        param["variable_type"] = ms["Types"][param["variable_type"]]
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
    for param in json["Parameters"]:
        ms["Parameters"][param["name"]] = convert_parameter_set(ms, param)

    # Placeholder for now
    ms["Parameters"] = ParameterContainer(ms["Parameters"])
