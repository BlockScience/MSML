from typing import Dict


class Entity:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.state = data["state"]

        # Boundary actions are added during parsing
        self.boundary_actions = []

    def __repr__(self):
        return "<{} Entity>".format(self.name)

    def add_boundary_action(self, boundary_action) -> None:
        self.boundary_actions.append(boundary_action)
