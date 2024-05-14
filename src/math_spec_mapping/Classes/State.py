from typing import Dict, List, TypedDict
from enum import Enum


class State:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.variables = data["variables"]
        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name
        self._write_variable_map()
        self.updated_by = []
        self.metadata = data["metadata"]
        self.name_variable = self.name.replace(" ", "").replace("-", "_")

    def _write_variable_map(self) -> None:
        """
        Convenience function which maps variable names to the objects
        """

        self.variable_map = {}

        # Iterate through
        for var in self.variables:
            key = var.name

            # Check variable name not repeated
            assert (
                var.name not in self.variable_map
            ), "Variable name {} is already present in variables for the state of {}!".format(
                key, self.name
            )

            self.variable_map[key] = var


class StateVariable:

    def __init__(self, data: Dict):
        self.type = data["type"]
        self.name = data["name"]
        self.description = data["description"]
        self.symbol = data["symbol"]
        self.domain = data["domain"]
        self.updated_by = []
        self.metadata = data["metadata"]

        # Add check for type of List
        if hasattr(self.type, "_name"):
            if self.type._name == "List":
                self.type.__name__ = self.type.__repr__().replace("typing.", "")
