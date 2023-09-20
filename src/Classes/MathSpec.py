from typing import Dict, List
from .Entity import Entity
from .Policy import Policy
from .Mechanism import Mechanism


class MathSpec:

    def __init__(self, ms_dict: Dict, json: Dict):
        # Internal variables to keep track
        self._ms_dict = ms_dict
        self._json = json
        self.action_transmission_channels = ms_dict["Action Transmission Channels"]
        self.boundary_actions = ms_dict['Boundary Actions']
        self.control_actions = ms_dict['Control Actions']
        self.entities = ms_dict['Entities']
        self.mechanisms = ms_dict['Mechanisms']
        self.parameters = ms_dict['Parameters']
        self.policies = ms_dict['Policies']
        self.spaces = ms_dict["Spaces"]
        self.state = ms_dict["State"]
        self.state_update_transmission_channels = ms_dict['State Update Transmission Channels']
        self.stateful_metrics = ms_dict['Stateful Metrics']

        self._crawl_parameters()

    def _crawl_parameters(self):
        param_links = {}

        for param in self.parameters.all_parameters:
            param_links[param] = {"Boundary Actions": [],
                                "Control Actions": [],
                                "Policies": [],
                                "Mechanisms": []}
            
        for ba in self.boundary_actions.values():
            for param in ba.parameters_used:
                param_links[param]["Boundary Actions"].append(ba)
                
        for ca in self.control_actions.values():
            for param in ca.parameters_used:
                param_links[param]["Control Actions"].append(ca)
                
        for p in self.policies.values():
            for param in p.parameters_used:
                param_links[param]["Policies"].append(ca)
                
        for m in self.mechanisms.values():
            for param in m.parameters_used:
                param_links[param]["Mechanisms"].append(ca)
        
        self.param_links = param_links

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

    def crawl_action_chains(self, action_keys: List[str]) -> dict:
        """Crawl the graph of the actions to find all policies, entities, edges, etc.

        Args:
            action_keys (List[str]): List of keys for behavioral actions

        Returns:
            dict: A dictionary of all nodes and edges
        """
        out = {}
        
        out["Boundary Actions"] = []
        out["Control Actions"] = []
        out["Policies"] = []
        out["Mechanisms"] = []
        out["State Updates"] = []
        out["Entities2"] = []
        out["Spaces"] = set()
        out["Parameters"] = set()
        q = []
        # Iterate through and add all calls
        for key in action_keys:
            assert key in self.boundary_actions or key in self.control_actions, "{} not a valid boundary or control action".format(
                key)
            if key in self.boundary_actions:
                q.extend(self.boundary_actions[key].calls)
                out["Boundary Actions"].append(self.boundary_actions[key])
                out["Spaces"].update(self.boundary_actions[key].codomain)
                out["Parameters"].update(self.boundary_actions[key].parameters_used)
            else:
                q.extend(self.control_actions[key].calls)
                out["Control Actions"].append(self.control_actions[key])
                out["Spaces"].update(self.control_actions[key].codomain)
                out["Parameters"].update(self.control_actions[key].parameters_used)
                
        
        out["Entities"] = self.find_relevant_entities([x.name for x in out["Boundary Actions"]])

        out["State"] = [x.state for x in out["Entities"]]
        out["State"] = list(set(out["State"]))

        while len(q) > 0:
            curr = q.pop(0)
            optional_flag = curr[1]
            curr = curr[0]
            if type(curr) == Policy:
                if curr in out["Policies"]:
                    continue
                else:
                    out["Policies"].append(curr)
                    q.extend(curr.calls)
                    out["Spaces"].update(curr.codomain)
                    out["Parameters"].update(curr.parameters_used)
            elif type(curr) == Mechanism:
                if curr in out["Mechanisms"]:
                    continue
                else:
                    out["Mechanisms"].append(curr)
                    out["Parameters"].update(curr.parameters_used)
                    for x in curr.updates:
                        if x not in out["State Updates"]:
                            out["State Updates"].append(x)
                        if x[0] not in out["Entities2"]:
                            out["Entities2"].append(x[0])
            else:
                assert False, "Unknown type in queue"
        out["Spaces"] = list(out["Spaces"])
        out["Parameters"] = list(out["Parameters"])
        return out
