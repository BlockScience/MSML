from typing import Dict


class Space:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.schema = data["schema"]
