from typing import Dict


def check_json_keys(json: Dict, check_set_key: str) -> None:
    """Function to check the correct keys are in the json dictionary

    Args:
        json (Dict): MathSpec json formatted dictionary
        check_set_key (str): The key for what checking set to use
    """

    # Get a temporary list of keys
    keys = list(json.keys())

    # Pick the correct checking set
    check_sets = {"Math Spec": ['Action Transmission Channels',
                                'Boundary Actions',
                                'Entities',
                                'Mechanisms',
                                'Parameters',
                                'Policies',
                                'Spaces',
                                'State',
                                'State Update Transmission Channels',
                                'Stateful Metrics'],
                  "State": ['name', 'notes', 'variables'],
                  "State Variable": ['type', 'name', 'description', 'symbol', 'domain'],
                  "Entity": ['name', 'notes', 'state'],
                  "Boundary Action": ['name', 'description', 'constraints', 'boundary_action_options', 'called_by', 'codomain', 'parameters_used'],
                  "Action Transmission Channel": ['origin', 'target', 'space', 'optional'],
                  "Mechanism": ["name", "description", "constraints", "logic", "domain", "parameters_used"],
                  "State Update Transmission Channel": ['origin', 'entity', 'variable', 'optional']}

    check_set = check_sets[check_set_key]

    # Check each key is in the json
    for k in check_set:
        assert k in keys, "{} not in json keys".format(k)
        keys.remove(k)

    # Make sure there are no extra keys in the json
    assert len(keys) == 0, "There are extra keys in json: {}".format(
        ", ".join(keys))
