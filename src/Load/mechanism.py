from typing import Dict
from ..Classes import Mechanism
from .general import check_json_keys


def convert_mechanism(data: Dict, ms: Dict) -> Mechanism:
    """Function to convert dictionary to mechanism object

    Args:
        data (Dict): The data to convert

    Returns:
        Mechanism: Mechanism object
    """

    if "metadata" not in data:
        data["metadata"] = {}

    data["domain"] = tuple(data["domain"])

    # Check the keys are correct
    check_json_keys(data, "Mechanism")
    assert type(data["domain"]) == tuple, "{} domain is not a tuple".format(
        data["name"]
    )
    if len(data["domain"]) == 0:
        data["domain"] = ("Empty Space",)

    # Copy
    data = data.copy()

    new_channels = []
    updates = data.pop("updates")
    for x in updates:
        new_channels.append(
            {
                "origin": data["name"],
                "entity": x[0],
                "variable": x[1],
                "optional": x[2],
            }
        )

    data["domain"] = tuple(ms["Spaces"][x] for x in data["domain"])

    # Build the action transmission channel object
    return Mechanism(data), new_channels


def load_mechanisms(ms: Dict, json: Dict) -> None:
    """Function to load states into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Mechanisms"] = {}
    state_update_transmission_channels = []
    for m in json["Mechanisms"]:
        ms["Mechanisms"][m["name"]], new_channels = convert_mechanism(m, ms)
        state_update_transmission_channels.extend(new_channels)
    return state_update_transmission_channels
