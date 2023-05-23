from typing import Dict


def load_spaces(ms: Dict, json: Dict) -> None:
    """Function to load spaces into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    # Placeholder for now
    ms["Spaces"] = json["Spaces"]
