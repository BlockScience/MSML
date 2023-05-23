from typing import Dict
from ..Classes import ParameterContainer


def load_parameters(ms: Dict, json: Dict) -> None:
    """Function to load parameters into the new dictionary

    Args:
        ms (Dict): MathSpec dictionary
        json (Dict): JSON version of MathSpec to load
    """

    # Placeholder for now
    ms["Parameters"] = ParameterContainer(json["Parameters"])
