from typing import Dict
from .Block import Block


class BoundaryAction(Block):
    def __init__(self, data: Dict):
        data["domain"] = tuple()
        super().__init__(data)
        self.boundary_action_options = data["boundary_action_options"]
        self.block_type = "Boundary Action"


class BoundaryActionOption:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.description = data["description"]
        self.logic = data["logic"]
