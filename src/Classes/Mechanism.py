from typing import Dict
from .Block import Block


class Mechanism(Block):
    def __init__(self, data: Dict):
        data["codomain"] = None
        super().__init__(data)
        self.logic = data["logic"]
        self.updates = []
