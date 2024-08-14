from typing import Dict
from .Block import Block


class ControlAction(Block):
    def __init__(self, data: Dict):
        super().__init__(data)
        self.control_action_options = data["control_action_options"]
        self.block_type = "Control Action"


class ControlActionOption:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.logic = data["logic"]
        self.implementations = data["implementations"]
