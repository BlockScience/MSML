from typing import Dict
from ..Classes import Policy


from .general import check_json_keys


def convert_policy(data: Dict) -> Policy:
    """Function to convert dictionary to policy object

    Args:
        data (Dict): The data to convert

    Returns:
        Policy: Policy object
    """

    # Check the keys are correct
    check_json_keys(data, "Policy")

    # Copy
    data = data.copy()

    # Build the action transmission channel object
    return Policy(data)


def load_policies(ms: Dict, json: Dict) -> None:
    """Function to load policies into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Policies"] = {}
    for key in json["Policies"]:
        ms["Policies"][key] = convert_policy(json["Policies"][key])
