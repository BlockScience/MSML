from typing import Dict, List
from .Block import Block


class PolicyOption:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.logic = data["logic"]
        self.implementations = data["implementations"]


class Policy(Block):
    def __init__(self, data: Dict):
        super().__init__(data)
        self.policy_options: List[PolicyOption] = data["policy_options"]
        self.block_type = "Policy"
