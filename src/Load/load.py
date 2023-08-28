from typing import Dict
from ..Classes import MathSpec
from .general import check_json_keys
from .states import load_states
from .entities import load_entities
from .boundary_actions import load_boundary_actions
from .control_actions import load_control_actions
from .action_transmission_channel import load_action_transmission_channels
from .mechanism import load_mechanisms
from .state_update_transmission_channels import load_state_update_transmission_channels
from .parameters import load_parameters
from .policy import load_policies
from .spaces import load_spaces
from .stateful_metrics import load_stateful_metrics


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
    load_control_actions(ms, json)
    load_mechanisms(ms, json)
    load_parameters(ms, json)
    load_policies(ms, json)
    load_spaces(ms, json)
    load_stateful_metrics(ms, json)
    load_action_transmission_channels(ms, json)
    load_state_update_transmission_channels(ms, json)

    # Assert all keys are correct for the ms version
    check_json_keys(ms, "Math Spec")

    ms = MathSpec(ms, json)
    return ms
