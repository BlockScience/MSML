from typing import Dict


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
