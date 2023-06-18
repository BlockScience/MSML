from typing import Dict


class Mechanism:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.logic = data["logic"]
        self.domain = data["domain"]
        self.parameters_used = data["parameters_used"]
        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name
        self.called_by = []
        self.updates = []
