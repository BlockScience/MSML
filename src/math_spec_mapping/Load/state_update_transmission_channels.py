from typing import Dict
from ..Classes import StateUpdateTransmissionChannel
from .general import check_json_keys


def convert_state_update_transmission_channel(
    data: Dict, ms: Dict
) -> StateUpdateTransmissionChannel:
    """Function to convert dictionary to state update transmission channel

    Args:
        data (Dict): The data to convert
        ms (Dict): MathSpec dictionary

    Returns:
        StateUpdateTransmissionChannel: Action transmission channel object
    """

    # Check the keys are correct
    check_json_keys(data, "State Update Transmission Channel")

    # Assert the origin is in mechanisms then map
    origin = data["origin"]
    assert origin in ms["Mechanisms"], "{} not found in mechanisms".format(origin)
    data["origin"] = ms["Mechanisms"][origin]

    # Assert entity is in entities then map
    entity = data["entity"]
    assert entity in ms["Entities"], "{} not found in entities".format(entity)
    data["entity"] = ms["Entities"][entity]

    # Assert variable is in entity state then map
    entity = data["entity"]
    variable = data["variable"]

    assert variable in entity.state.variable_map, "{} variable not in {} state".format(
        variable, entity.name
    )
    data["variable"] = entity.state.variable_map[variable]

    # Add in the updates logic
    data["origin"].updates.append((data["entity"], data["variable"]))
    data["entity"].state.updated_by.append(data["origin"])
    data["entity"].add_impacted_by_mechanism(data["origin"])
    data["variable"].updated_by.append(data["origin"])

    # Copy
    data = data.copy()

    # Build the state update transmission channel object
    return StateUpdateTransmissionChannel(data)


def load_state_update_transmission_channels(
    ms: Dict, state_update_transmission_channels
) -> None:
    """Function to load state update transmission channels into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["State Update Transmission Channels"] = []
    for sutc in state_update_transmission_channels:
        ms["State Update Transmission Channels"].append(
            convert_state_update_transmission_channel(sutc, ms)
        )
