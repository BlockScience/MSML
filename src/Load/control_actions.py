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

    # Check the keys are correct
    check_json_keys(data, "Control Action")

    # Copy
    data = data.copy()

    # Convert the boundary action options
    new_cao = []
    for ca in data["control_action_options"]:
        check_json_keys(ca, "Control Action Option")
        new_cao.append(ControlActionOption(ca))
    data["control_action_options"] = new_cao

    # Build the control action object
    return ControlAction(data)


def load_control_actions(ms: Dict, json: Dict) -> None:
    """Function to load control actions into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Control Actions"] = {}
    for key in json["Control Actions"]:
        ms["Control Actions"][key] = convert_control_action(
            json["Control Actions"][key], ms)
