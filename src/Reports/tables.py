import pandas as pd
from typing import Union

def create_parameter_impact_table(param_links: dict, orientation: str = "Parameters") -> Union[pd.DataFrame, pd.Series]:
    """Generates either a parameter dataframe or series from the parameter links.

    Args:
        param_links (dict): Either parameter links or exploded parameter links
        orientation (str, optional): Either Parameters (table with parameters as index,
        the block types as columns) or Blocks (series with the blocks and all the parameters
        that have an impact). Defaults to "Parameters".

    Returns:
        Union[pd.DataFrame, pd.Series]: The resulting table
    """
    pass