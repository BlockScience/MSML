from typing import Dict

# All parameters and parameter sets


class ParameterContainer:
    def __init__(self, data: Dict):
        self.data = data

        self.all_parameters = []
        self.parameter_map = {}
        for x in self.data.values():
            x = x.parameters
            for y in x:
                self.parameter_map[y.name] = y
            x = [y.name for y in x]
            self.all_parameters.extend(x)
        assert len(set(self.all_parameters)) == len(
            self.all_parameters
        ), "A parameter name is repeated!"


# A set of parameters


class ParameterSet:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.parameters = data["parameters"]
        self.metadata = data["metadata"]


# Individual Parameter


class Parameter:
    def __init__(self, data: Dict):
        self.variable_type = data["variable_type"]
        self.name = data["name"]
        self.description = data["description"]
        self.symbol = data["symbol"]
        self.domain = data["domain"]
        self.parameter_class = data[
            "parameter_class"
        ]  # I.e. behavioral, functional, system
        self.metadata = data["metadata"]
