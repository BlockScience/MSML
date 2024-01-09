from typing import Dict
from .Block import Block


class ControlAction(Block):
    def __init__(self, data: Dict):
        data["domain"] = None
        super().__init__(data)
        self.control_action_options = data["control_action_options"]


class ControlActionOption:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.logic = data["logic"]
