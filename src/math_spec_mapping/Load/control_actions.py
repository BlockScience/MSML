from typing import Dict
from ..Classes import ControlAction, ControlActionOption
from .general import check_json_keys, check_domain_codomain_spaces


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

    check_domain_codomain_spaces(data, ms)

    if len(data["codomain"]) == 0:
        data["codomain"] = ("Empty Space",)

    # Copy
    data = data.copy()

    # Convert the boundary action options
    new_cao = []
    for ca in data["control_action_options"]:
        check_json_keys(ca, "Control Action Option")
        ca["implementations"] = {}
        if "python" in ms["Implementations"]:
            if "control_action_options" in ms["Implementations"]["python"]:
                if (
                    ca["name"]
                    in ms["Implementations"]["python"]["control_action_options"]
                ):
                    ca["implementations"]["python"] = ms["Implementations"]["python"][
                        "control_action_options"
                    ][ca["name"]]
        new_cao.append(ControlActionOption(ca))
    data["control_action_options"] = new_cao

    data["codomain"] = tuple(ms["Spaces"][x] for x in data["codomain"])
    data["domain"] = (ms["Spaces"]["Empty Space"],)

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

        key = ca["name"]
        for space in ms["Control Actions"][key].domain:
            space.domain_blocks.append(ms["Control Actions"][key])

        for space in ms["Control Actions"][key].codomain:
            space.codomain_blocks.append(ms["Control Actions"][key])
