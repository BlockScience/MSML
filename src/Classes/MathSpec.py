from typing import Dict, List
from .Entity import Entity


class MathSpec:

    def __init__(self, ms_dict: Dict, json: Dict):
        # Internal variables to keep track
        self._ms_dict = ms_dict
        self._json = json
        self.action_transmission_channels = ms_dict["Action Transmission Channels"]
        self.boundary_actions = ms_dict['Boundary Actions']
        self.entities = ms_dict['Entities']
        self.mechanisms = ms_dict['Mechanisms']
        self.parameters = ms_dict['Parameters']
        self.policies = ms_dict['Parameters']
        self.policies = ms_dict['Policies']
        self.spaces = ms_dict["Spaces"]
        self.state = ms_dict["State"]
        self.state_update_transmission_channels = ms_dict['State Update Transmission Channels']
        self.stateful_metrics = ms_dict['Stateful Metrics']

    def find_relevant_entities(self, action_keys: List[str]) -> List[Entity]:
        """Function to find all entities that can call any of the actions

        Args:
            action_keys (List[str]): List of keys for behavioral actions

        Returns:
            List[Entity]: List of relevant entities
        """

        out = []
        # Iterate through and add all entities
        for key in action_keys:
            assert key in self.boundary_actions, "{} not a valid boundary action".format(
                key)
            out.extend(self.boundary_actions[key].called_by)

        # Get unique records
        out = list(set(out))

        return out
