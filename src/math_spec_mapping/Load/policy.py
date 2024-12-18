from typing import Dict
from ..Classes import Policy, PolicyOption


from .general import check_json_keys, check_domain_codomain_spaces


def convert_policy_options(data: Dict, ms) -> PolicyOption:
    """Function to convert policy options

    Args:
        data (Dict): Policy option data

    Returns:
        PolicyOption: The policy option object
    """

    # Check the keys are correct
    check_json_keys(data, "Policy Option")

    # Copy
    data = data.copy()

    data["implementations"] = {}

    if "python" in ms["Implementations"]:
        if "policies" in ms["Implementations"]["python"]:
            if data["name"] in ms["Implementations"]["python"]["policies"]:
                data["implementations"]["python"] = ms["Implementations"]["python"][
                    "policies"
                ][data["name"]]

    # Build the policy object
    return PolicyOption(data)


def convert_policy(data: Dict, ms: Dict) -> Policy:
    """Function to convert dictionary to policy object

    Args:
        data (Dict): The data to convert

    Returns:
        Policy: Policy object
    """

    if "metadata" not in data:
        data["metadata"] = {}
    # Check the keys are correct
    check_json_keys(data, "Policy")

    data["codomain"] = tuple(data["codomain"])
    data["domain"] = tuple(data["domain"])

    assert type(data["codomain"]) == tuple, "{} codomain is not a tuple".format(
        data["name"]
    )
    assert type(data["domain"]) == tuple, "{} domain is not a tuple".format(
        data["name"]
    )
    check_domain_codomain_spaces(data, ms)

    if len(data["codomain"]) == 0:
        data["codomain"] = ("Empty Space",)

    if len(data["domain"]) == 0:
        data["domain"] = ("Empty Space",)

    # Copy
    data = data.copy()

    # Convert policy options
    policy_options = []
    for po in data["policy_options"]:
        policy_options.append(convert_policy_options(po, ms))
    data["policy_options"] = policy_options

    data["codomain"] = tuple(ms["Spaces"][x] for x in data["codomain"])
    data["domain"] = tuple(ms["Spaces"][x] for x in data["domain"])

    # Build the policy object
    return Policy(data)


def load_policies(ms: Dict, json: Dict) -> None:
    """Function to load policies into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    ms["Policies"] = {}
    for policy in json["Policies"]:
        ms["Policies"][policy["name"]] = convert_policy(policy, ms)

        key = policy["name"]
        for space in ms["Policies"][key].domain:
            space.domain_blocks.append(ms["Policies"][key])

        for space in ms["Policies"][key].codomain:
            space.codomain_blocks.append(ms["Policies"][key])
