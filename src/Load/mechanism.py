from typing import Dict
from ..Classes import Mechanism
from .general import check_json_keys


def convert_mechanism(data: Dict) -> Mechanism:
    """Function to convert dictionary to mechanism object

    Args:
        data (Dict): The data to convert

    Returns:
        Mechanism: Mechanism object
    """

    # Check the keys are correct
    check_json_keys(data, "Mechanism")

    # Copy
    data = data.copy()

    # Build the action transmission channel object
    return Mechanism(data)


def load_mechanisms(ms: Dict, json: Dict) -> None:
    """Function to load states into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Mechanisms"] = {}
    for key in json["Mechanisms"]:
        ms["Mechanisms"][key] = convert_mechanism(json["Mechanisms"][key])
