from typing import Dict


class Policy:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.constraints = data["constraints"]
        self.policy_options = data["policy_options"]
        self.domain = data["domain"]
        self.codomain = data["codomain"]
        self.parameters_used = data["parameters_used"]
        self.called_by = []
        self.calls = []
