from typing import Dict


class Space:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.schema = data["schema"]


TerminatingSpace = Space({"name": "Terminating Space", "schema": {}})
EmptySpace = Space({"name": "Empty Space", "schema": {}})
