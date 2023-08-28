from typing import Dict


class ControlAction:

    def __init__(self, data: Dict):
        self.name = data['name']
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.control_action_options = data["control_action_options"]
        self.codomain = data["codomain"]
        self.parameters_used = data["parameters_used"]
        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name
        self.calls = []


class ControlActionOption:

    def __init__(self, data: Dict):
        pass
