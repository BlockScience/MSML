from typing import Dict


def check_json_keys(json: Dict) -> None:
    """Function to check the correct keys are in the json dictionary

    Args:
        json (Dict): MathSpec json formatted dictionary
    """

    # Get a temporary list of keys
    keys = list(json.keys())

    # Check each key is in the json
    for k in ['Action Transmission Channels',
              'Boundary Actions',
              'Entities',
              'Mechanisms',
              'Parameters',
              'Policies',
              'Spaces',
              'State',
              'State Update Transmission Channels',
              'Stateful Metrics']:
        assert k in keys, "{} not in json keys".format(k)
        keys.remove(k)

    # Make sure there are no extra keys in the json
    assert len(keys) == 0, "There are extra keys in json: {}".format(
        ", ".join(keys))
