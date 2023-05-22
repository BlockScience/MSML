from typing import Dict


class Entity:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.state = data["state"]
