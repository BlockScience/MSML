from typing import Dict


class BoundaryAction:

    def __init__(self, data: Dict):
        self.name = data['name']
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.boundary_action_options = data["boundary_action_options"]
        self.called_by = data["called_by"]
        self.codomain = data["codomain"]
        self.parameters_used = data["parameters_used"]
        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name
        self.calls = []


class BoundaryActionOption:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.logic = data["logic"]
