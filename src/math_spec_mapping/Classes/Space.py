from typing import Dict


class Space:
    def __init__(self, data: Dict):
        self.name = data["name"]
        self.schema = data["schema"]
        self.metadata = data["metadata"]
        self.description = data["description"]
        self.name_variable = self.name.replace(" ", "").replace("-", "_")
        self.domain_blocks = []
        self.codomain_blocks = []

    def __repr__(self):
        return self.name


TerminatingSpace = Space(
    {
        "name": "Terminating Space",
        "schema": {},
        "metadata": {},
        "description": "Built-in space for denoting termination of block",
    }
)
EmptySpace = Space(
    {
        "name": "Empty Space",
        "schema": {},
        "metadata": {},
        "description": "Built-in space for denoting returning no data",
    }
)
