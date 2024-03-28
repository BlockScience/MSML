from typing import Dict


class Space:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.schema = data["schema"]
        self.metadata = data["metadata"]
        self.name_variable = self.name.replace(" ", "").replace("-", "_")

    def __repr__(self):
        return self.name


TerminatingSpace = Space({"name": "Terminating Space", "schema": {}, "metadata": {}})
EmptySpace = Space({"name": "Empty Space", "schema": {}, "metadata": {}})
