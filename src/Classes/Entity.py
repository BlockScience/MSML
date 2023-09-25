from typing import Dict


class Entity:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.state = data["state"]

        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name

        # Boundary actions are added during parsing
        self.boundary_actions = []
        self.impacted_by = []

    def __repr__(self):
        return "<{} Entity>".format(self.name)

    def add_boundary_action(self, boundary_action) -> None:
        self.boundary_actions.append(boundary_action)
    
    def add_impacted_by_mechanism(self, mechanism) -> None:
        self.impacted_by.append(mechanism)