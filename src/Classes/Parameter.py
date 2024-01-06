from typing import Dict

# All parameters and parameter sets


class ParameterContainer:
    def __init__(self, data: Dict):
        self.data = data

        # TODO: Get rid of this when params are fully built out
        self.all_parameters = []
        for x in self.data.values():
            x = x.parameters
            x = [y.name for y in x]
            self.all_parameters.extend(x)


# A set of parameters


class ParameterSet:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.parameters = data["parameters"]


# Individual Parameter


class Parameter:
    def __init__(self, data: Dict):
        self.variable_type = data["variable_type"]
        self.name = data["name"]
        self.description = data["description"]
        self.symbol = data["symbol"]
        self.domain = data["domain"]
