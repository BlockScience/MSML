from typing import Dict
from .Block import Block
from .Space import TerminatingSpace


class Mechanism(Block):
    def __init__(self, data: Dict):
        data["codomain"] = (TerminatingSpace,)
        super().__init__(data)
        self.logic = data["logic"]
        self.updates = []
        self.block_type = "Mechanism"
        self.implementations = data["implementations"]
