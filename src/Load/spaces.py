from typing import Dict
from ..Classes import Space
from .general import check_json_keys


def convert_space(data: Dict) -> Space:
    # Check the keys are correct
    check_json_keys(data, "Space")

    # Copy
    data = data.copy()

    # Build the space object
    return Space(data)


def load_spaces(ms: Dict, json: Dict) -> None:
    """Function to load spaces into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    # Placeholder for now
    ms["Spaces"] = {}

    for space in json["Spaces"]:
        ms["Spaces"][space["name"]] = convert_space(space)
