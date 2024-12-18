from typing import Dict
from ..Classes import ActionTransmissionChannel
from .general import check_json_keys


def convert_action_transmission_channel(
    data: Dict, ms: Dict
) -> ActionTransmissionChannel:
    """Function to convert dictionary to action transmission channel

    Args:
        data (Dict): The data to convert
        ms (Dict): MathSpec dictionary

    Returns:
        ActionTransmissionChannel: Action transmission channel object
    """

    # Check the keys are correct
    check_json_keys(data, "Action Transmission Channel")

    # Copy
    data = data.copy()

    data["space"] = ms["Spaces"][data["space"]]

    # Assert that the origin is in the math spec and only once then convert
    origin = data["origin"]
    is_boundary = origin in ms["Boundary Actions"]
    is_policy = origin in ms["Policies"]
    is_control = origin in ms["Control Actions"]
    assert is_boundary + is_policy + is_control > 0, "Can't find the origin"
    assert is_boundary + is_policy + is_control == 1, "Multiple versions of the origin"
    if is_boundary:
        data["origin"] = ms["Boundary Actions"][origin]
    if is_policy:
        data["origin"] = ms["Policies"][origin]
    if is_control:
        data["origin"] = ms["Control Actions"][origin]

    # Assert that the target is in the math spec and only once then convert
    target = data["target"]
    is_policy = target in ms["Policies"]
    is_mechanism = target in ms["Mechanisms"]
    assert is_policy + is_mechanism > 0, "Can't find the target"
    assert is_policy + is_mechanism == 1, "Multiple versions of the origin"
    if is_policy:
        data["target"] = ms["Policies"][target]
    if is_mechanism:
        data["target"] = ms["Mechanisms"][target]

    # Add in called by and called here with origin and target
    if (data["target"], data["optional"], data["space"]) not in data["origin"].calls:
        data["origin"].calls.append((data["target"], data["optional"], data["space"]))
    if (data["origin"], data["optional"], data["space"]) not in data[
        "target"
    ].called_by:
        data["target"].called_by.append(
            (data["origin"], data["optional"], data["space"])
        )

    # Build the action transmission channel object
    return ActionTransmissionChannel(data)


def load_action_transmission_channels(
    ms: Dict, action_transmission_channels: list
) -> None:
    """Function to load states into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        action_transmission_channels (list): List of action transmission channels
    """

    ms["Action Transmission Channels"] = []
    for atc in action_transmission_channels:
        atc = convert_action_transmission_channel(atc, ms)
        ms["Action Transmission Channels"].append(atc)
