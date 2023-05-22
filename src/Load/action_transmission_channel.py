from typing import Dict
from ..Classes import ActionTransmissionChannel
from .general import check_json_keys


def convert_action_transmission_channel(data: Dict) -> ActionTransmissionChannel:
    """Function to convert dictionary to action transmission channel

    Args:
        data (Dict): The data to convert

    Returns:
        ActionTransmissionChannel: Action transmission channel object
    """

    # Check the keys are correct
    check_json_keys(data, "Action Transmission Channel")

    # Copy
    data = data.copy()

    # Build the action transmission channel object
    return ActionTransmissionChannel(data)


def load_action_transmission_channels(ms: Dict, json: Dict) -> None:
    """Function to load states into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Action Transmission Channels"] = []
    for atc in json["Action Transmission Channels"]:
        ms["Action Transmission Channels"].append(
            convert_action_transmission_channel(atc))
