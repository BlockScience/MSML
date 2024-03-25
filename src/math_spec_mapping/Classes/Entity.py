from typing import Dict
from .ControlAction import ControlAction
from .BoundaryAction import BoundaryAction


class Entity:

    def __init__(self, data: Dict):
        self.name = data["name"]
        self.notes = data["notes"]
        self.state = data["state"]
        self.metadata = data["metadata"]

        if "label" in data:
            self.label = data["label"]
        else:
            self.label = self.name

        # Boundary actions are added during parsing
        self.boundary_actions = []
        self.impacted_by_mechanism = []
        self.impacted_by_actions = []

    def __repr__(self):
        return "<{} Entity>".format(self.name)

    def add_boundary_action(self, boundary_action) -> None:
        self.boundary_actions.append(boundary_action)

    def add_impacted_by_mechanism(self, mechanism) -> None:
        self.impacted_by_mechanism.append(mechanism)
        q = [mechanism]
        while len(q) > 0:
            cur = q.pop()
            if type(cur) == ControlAction or type(cur) == BoundaryAction:
                if cur not in self.impacted_by_actions:
                    self.impacted_by_actions.append(cur)
            else:
                q.extend([x[0] for x in cur.called_by])
