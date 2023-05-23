from typing import Dict
from ..Classes import StateUpdateTransmissionChannel
from .general import check_json_keys


def convert_state_update_transmission_channel(data: Dict) -> StateUpdateTransmissionChannel:
    """Function to convert dictionary to state update transmission channel

    Args:
        data (Dict): The data to convert

    Returns:
        StateUpdateTransmissionChannel: Action transmission channel object
    """

    # Check the keys are correct
    check_json_keys(data, "State Update Transmission Channel")

    # Copy
    data = data.copy()

    # Build the state update transmission channel object
    return StateUpdateTransmissionChannel(data)


def load_state_update_transmission_channels(ms: Dict, json: Dict) -> None:
    """Function to load state update transmission channels into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["State Update Transmission Channels"] = []
    for sutc in json["State Update Transmission Channels"]:
        ms["State Update Transmission Channels"].append(
            convert_state_update_transmission_channel(sutc))
