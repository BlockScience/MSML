from typing import Dict
from ..Classes import MathSpec
from .general import check_json_keys
from .states import load_states
from .entities import load_entities
from .boundary_actions import load_boundary_actions
from .action_transmission_channel import load_action_transmission_channels


def load_from_json(json: Dict) -> MathSpec:
    """Function to load a math spec from a json format

    Args:
        json (Dict): The json format

    Returns:
        MathSpec: MathSpec object
    """

    # Assert the keys are correct in the json
    check_json_keys(json, "Math Spec")

    ms = {}

    # Do loading one by one to transfer the json
    load_states(ms, json)
    load_entities(ms, json)
    load_boundary_actions(ms, json)

    load_action_transmission_channels(ms, json)

    ms = MathSpec(ms, json)
    return ms
