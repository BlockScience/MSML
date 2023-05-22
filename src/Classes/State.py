from typing import Dict


class State:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.variables = data["variables"]
        self._write_variable_map()

    def _write_variable_map(self) -> None:
        """
        Convenience function which maps variable names to the objects
        """

        self.variable_map = {}

        # Iterate through
        for var in self.variables:
            key = var.name

            # Check variable name not repeated
            assert var.name not in self.variable_map, "Variable name {} is already present in variables!".format(
                key)

            self.variable_map[key] = var


class StateVariable:

    def __init__(self, data: Dict):
        self.type = data["type"]
        self.name = data["name"]
        self.description = data["description"]
        self.symbol = data["symbol"]
        self.domain = data["domain"]