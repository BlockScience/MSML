from typing import Dict
from ..Classes import BoundaryAction
from .general import check_json_keys


def convert_boundary_action(data: Dict) -> BoundaryAction:
    """Function to convert boundary action

    Args:
        data (Dict): JSON data

    Returns:
        BoundaryAction: Boundary action object
    """

    # Check the keys are correct
    check_json_keys(data, "Boundary Action")

    # Copy
    data = data.copy()

    # Build the boundary action object
    return BoundaryAction(data)


def load_boundary_actions(ms: Dict, json: Dict) -> None:
    """Function to load boundary actions into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Boundary Actions"] = {}
    for key in json["Boundary Actions"]:
        ms["Boundary Actions"][key] = convert_boundary_action(
            json["Boundary Actions"][key])
