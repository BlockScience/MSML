from typing import Dict
from ..Classes import ControlAction, ControlActionOption
from .general import check_json_keys


def convert_control_action(data: Dict, ms: Dict) -> ControlAction:
    """Function to convert control action

    Args:
        data (Dict): JSON data
        ms (Dict): MathSpec dictionary

    Returns:
        ControlAction: Control action object
    """

    if "metadata" not in data:
        data["metadata"] = {}

    data["codomain"] = tuple(data["codomain"])

    # Check the keys are correct
    check_json_keys(data, "Control Action")
    assert type(data["codomain"]) == tuple, "{} codomain is not a tuple".format(
        data["name"]
    )

    if len(data["codomain"]) == 0:
        data["codomain"] = ("Empty Space",)

    # Copy
    data = data.copy()

    # Convert the boundary action options
    new_cao = []
    for ca in data["control_action_options"]:
        check_json_keys(ca, "Control Action Option")
        new_cao.append(ControlActionOption(ca))
    data["control_action_options"] = new_cao

    data["codomain"] = tuple(ms["Spaces"][x] for x in data["codomain"])

    # Build the control action object
    return ControlAction(data)


def load_control_actions(ms: Dict, json: Dict) -> None:
    """Function to load control actions into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Control Actions"] = {}
    for ca in json["Control Actions"]:
        ms["Control Actions"][ca["name"]] = convert_control_action(ca, ms)
