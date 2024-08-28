from typing import Dict, List
from .Entity import Entity
from .Policy import Policy
from .Mechanism import Mechanism
from .ControlAction import ControlAction
from .BoundaryAction import BoundaryAction
import os
from copy import deepcopy
import shutil
import pandas as pd
from inspect import signature, getsource


class MathSpec:
    def __init__(self, ms_dict: Dict, json: Dict):
        # Internal variables to keep track
        self._ms_dict = ms_dict
        self._json = json
        self.type_keys = ms_dict["Type Keys"]
        self.implementations = ms_dict["Implementations"]
        self.action_transmission_channels = ms_dict["Action Transmission Channels"]
        self.boundary_actions = ms_dict["Boundary Actions"]
        self.control_actions = ms_dict["Control Actions"]
        self.entities = ms_dict["Entities"]
        self.mechanisms = ms_dict["Mechanisms"]
        self.parameters = ms_dict["Parameters"]
        self.policies = ms_dict["Policies"]
        self.spaces = ms_dict["Spaces"]
        self.state = ms_dict["State"]
        self.state_update_transmission_channels = ms_dict[
            "State Update Transmission Channels"
        ]
        self.stateful_metrics = ms_dict["Stateful Metrics"]
        self.wiring = ms_dict["Wiring"]
        self.blocks = ms_dict["Blocks"]
        self.types = ms_dict["Types"]
        self.metrics = ms_dict["Metrics"]
        self.displays = ms_dict["Displays"]
        self.stateful_metrics_map = {}
        for x in self.stateful_metrics:
            for y in self.stateful_metrics[x].metrics:
                self.stateful_metrics_map[y.name] = y

        self._check_parameters()
        self._crawl_parameters()
        self._crawl_parameters_exploded()
        self._check_dictionary_names()
        self._build_functional_parameters()
        self._build_parameter_types()
        self._crawl_spaces()
        self._set_source_code()

    def _check_dictionary_names(self):
        for key in self.boundary_actions:
            assert key == self.boundary_actions[key].name
        for key in self.control_actions:
            assert key == self.control_actions[key].name
        for key in self.entities:
            assert key == self.entities[key].name
        for key in self.mechanisms:
            assert key == self.mechanisms[key].name
        for key in self.policies:
            assert key == self.policies[key].name

    def _check_parameters(self):
        for ba in self.boundary_actions.values():
            for param in ba.parameters_used:
                assert param in self.parameters.all_parameters, "{} not found".format(
                    param
                )

        for ca in self.control_actions.values():
            for param in ca.parameters_used:
                assert param in self.parameters.all_parameters, "{} not found".format(
                    param
                )

        for p in self.policies.values():
            for param in p.parameters_used:
                assert param in self.parameters.all_parameters, "{} not found".format(
                    param
                )

        for m in self.mechanisms.values():
            for param in m.parameters_used:
                assert param in self.parameters.all_parameters, "{} not found".format(
                    param
                )

    def _crawl_parameters(self):
        param_links = {}

        for param in self.parameters.all_parameters:
            param_links[param] = {
                "Boundary Actions": [],
                "Control Actions": [],
                "Policies": [],
                "Mechanisms": [],
            }

        for ba in self.boundary_actions.values():
            for param in ba.parameters_used:
                param_links[param]["Boundary Actions"].append(ba)

        for ca in self.control_actions.values():
            for param in ca.parameters_used:
                param_links[param]["Control Actions"].append(ca)

        for p in self.policies.values():
            for param in p.parameters_used:
                param_links[param]["Policies"].append(p)

        for m in self.mechanisms.values():
            for param in m.parameters_used:
                param_links[param]["Mechanisms"].append(m)

        self.param_links = param_links

    def _crawl_parameters_exploded(self):
        param_links_exploded = {}

        for key in self.param_links:
            param_links_exploded[key] = {}
            for key2 in self.param_links[key]:
                param_links_exploded[key][key2] = self.param_links[key][key2][:]

        for param in param_links_exploded:
            q = []
            d = param_links_exploded[param]
            d["Entities"] = []
            for key in d:
                q.extend(d[key])

            q1 = q.copy()
            q2 = q.copy()

            # Look for downstream
            while len(q1) > 0:
                cur = q1.pop()
                if type(cur) == ControlAction:
                    if cur not in d["Control Actions"]:
                        d["Control Actions"].append(cur)
                elif type(cur) == BoundaryAction:
                    if cur not in d["Boundary Actions"]:
                        d["Boundary Actions"].append(cur)
                    for entity in cur.called_by:
                        if entity not in d["Entities"]:
                            d["Entities"].append(entity)
                elif type(cur) == Policy:
                    if cur not in d["Policies"]:
                        d["Policies"].append(cur)
                        q1.extend([x[0] for x in cur.called_by])
                elif type(cur) == Mechanism:
                    if cur not in d["Mechanisms"]:
                        d["Mechanisms"].append(cur)
                        q1.extend([x[0] for x in cur.called_by])
                else:
                    assert False

            # Look for upstream
            while len(q2) > 0:
                cur = q2.pop()
                if type(cur) == ControlAction:
                    if cur not in d["Control Actions"]:
                        d["Control Actions"].append(cur)
                    q2.extend([x[0] for x in cur.calls])
                elif type(cur) == BoundaryAction:
                    if cur not in d["Boundary Actions"]:
                        d["Boundary Actions"].append(cur)
                        q2.extend([x[0] for x in cur.calls])
                elif type(cur) == Policy:
                    if cur not in d["Policies"]:
                        d["Policies"].append(cur)
                        q2.extend([x[0] for x in cur.calls])
                elif type(cur) == Mechanism:
                    if cur not in d["Mechanisms"]:
                        d["Mechanisms"].append(cur)
                    for entity in [x[0] for x in cur.updates]:
                        if entity not in d["Entities"]:
                            d["Entities"].append(entity)
                else:
                    assert False

            self.param_links_exploded = param_links_exploded

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
            assert (
                key in self.boundary_actions
            ), "{} not a valid boundary action".format(key)
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
            assert (
                key in self.boundary_actions or key in self.control_actions
            ), "{} not a valid boundary or control action".format(key)
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

        out["Entities"] = self.find_relevant_entities(
            [x.name for x in out["Boundary Actions"]]
        )

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

    def crawl_wiring(self, wiring_name) -> dict:
        wiring = self.wiring[wiring_name]
        out = {}

        out["Boundary Actions"] = []
        out["Control Actions"] = []
        out["Policies"] = []
        out["Mechanisms"] = []
        out["State Updates"] = []
        out["Entities2"] = []
        out["Spaces"] = set()
        out["Parameters"] = set()
        out["Wiring"] = []
        q = [wiring.name]
        while len(q) > 0:
            x = q.pop()
            if x in self.wiring:
                if x not in out["Wiring"]:
                    x = self.wiring[x]
                    out["Wiring"].append(x)
                    q.extend([y.name for y in x.components])
                else:
                    x = None
            elif x in self.boundary_actions:
                if x not in out["Boundary Actions"]:
                    x = self.boundary_actions[x]
                    out["Boundary Actions"].append(x)
                else:
                    x = None
            elif x in self.control_actions:
                if x not in out["Control Actions"]:
                    x = self.control_actions[x]
                    out["Control Actions"].append(x)
                else:
                    x = None
            elif x in self.policies:
                if x not in out["Policies"]:
                    x = self.policies[x]
                    out["Policies"].append(x)
                else:
                    x = None
            elif x in self.mechanisms:
                if x not in out["Mechanisms"]:
                    x = self.mechanisms[x]
                    out["Mechanisms"].append(x)
                    for y in x.updates:
                        if y not in out["State Updates"]:
                            out["State Updates"].append(y)
                        if y[0] not in out["Entities2"]:
                            out["Entities2"].append(y[0])
                else:
                    x = None
            else:
                assert False

            if x:
                out["Spaces"].update(x.codomain)
                out["Spaces"].update(x.domain)
                out["Parameters"].update(x.parameters_used)

        out["Entities"] = self.find_relevant_entities(
            [x.name for x in out["Boundary Actions"]]
        )

        out["State"] = [x.state for x in out["Entities"]]
        out["State"] = list(set(out["State"]))
        return out

    def get_specific_stateful_metrics(self, metric):
        for x in self.stateful_metrics.values():
            for y in x.metrics:
                if metric == y.name:
                    return y
        print("Metric not found")
        return None

    def get_all_stateful_metric_names(self):
        sm = []
        for metrics in self.stateful_metrics.values():
            sm.extend([x.name for x in metrics.metrics])
        return sm

    def _build_functional_parameters(self):
        opts = [
            (x, x.policy_options)
            for x in self.policies.values()
            if len(x.policy_options) > 1
        ]
        opts.extend(
            [
                (x, x.boundary_action_options)
                for x in self.boundary_actions.values()
                if len(x.boundary_action_options) > 1
            ]
        )
        opts.extend(
            [
                (x, x.control_action_options)
                for x in self.control_actions.values()
                if len(x.control_action_options) > 1
            ]
        )
        self.functional_parameters = {}
        for x in opts:
            x, y = x
            self.functional_parameters["FP {}".format(x.name)] = {}
            for y1 in y:
                self.functional_parameters["FP {}".format(x.name)][y1.name] = y1

    def _build_parameter_types(self):
        system_parameters_types = {}
        behavioral_parameters_types = {}
        functional_parameters_types = {}

        for x in self.parameters.all_parameters:
            pt = self.parameters.parameter_map[x].variable_type.original_type_name
            pc = self.parameters.parameter_map[x].parameter_class
            if pc == "Functional":
                functional_parameters_types[x] = pt
            elif pc == "System":
                system_parameters_types[x] = pt
            elif pc == "Behavioral":
                behavioral_parameters_types[x] = pt
            else:
                assert False
        for x in self.functional_parameters:
            functional_parameters_types[x] = "str"

        self.system_parameters_types = system_parameters_types
        self.behavioral_parameters_types = behavioral_parameters_types
        self.functional_parameters_types = functional_parameters_types

    def _crawl_spaces(self):
        self._used_spaces = []
        self._used_spaces.extend([x.codomain for x in self.control_actions.values()])
        self._used_spaces.extend([x.codomain for x in self.boundary_actions.values()])
        self._used_spaces.extend([x.domain for x in self.policies.values()])
        self._used_spaces.extend([x.codomain for x in self.policies.values()])
        self._used_spaces.extend([x.domain for x in self.mechanisms.values()])

        self._used_spaces = list(set().union(*self._used_spaces))
        us_names = [y.name for y in self._used_spaces]
        self._unused_spaces = [self.spaces[x] for x in self.spaces if x not in us_names]

    def metaprogramming_python_types(self, model_directory, overwrite=False):
        path = model_directory + "/types.py"
        if not overwrite:
            assert "types.py" not in os.listdir(
                model_directory
            ), "The types file is already written, either delete it or switch to overwrite mode"
        out = "import typing\n\n"
        for t in self.types:
            t = self.types[t]
            assert "python" in t.type, "No python type associated with {}".format(
                t.name
            )
            x = t.type["python"]
            type_desc = x.__name__ if hasattr(x, "__name__") else str(x)
            out += "{} = {}".format(t.original_type_name, type_desc)
            out += "\n"
        with open(path, "w") as f:
            f.write(out)

    def metaprogramming_python_spaces(self, model_directory, overwrite=False):
        path = model_directory + "/spaces.py"
        if not overwrite:
            assert "spaces.py" not in os.listdir(
                model_directory
            ), "The spaces file is already written, either delete it or switch to overwrite mode"
        unique_spaces = set().union(
            *[set(x.schema.values()) for x in self.spaces.values()]
        )
        unique_types = [x.original_type_name for x in unique_spaces]
        out = ""
        out += "from .types import {}".format(", ".join(unique_types))
        out += "\n"
        out += "from typing import TypedDict"
        out += "\n"
        out += "\n"

        for space in self.spaces:
            out += self.spaces[space].name_variable
            out += " = "
            d = self.spaces[space].schema
            d = [(x, d[x].original_type_name) for x in d]
            d = ["'{}': {}".format(x[0], x[1]) for x in d]
            d = ", ".join(d)
            d = "{" + d + "}"
            out += "TypedDict('{}', {})".format(self.spaces[space].name, d)
            out += "\n"

        with open(path, "w") as f:
            f.write(out)

    def run_experiment(
        self,
        experiment,
        params_base,
        state_base,
        post_processing_function,
        state_preperation_functions=None,
        parameter_preperation_functions=None,
        metrics_functions=None,
    ):
        if experiment["Param Modifications"]:
            params_base = deepcopy(params_base)
            for key in experiment["Param Modifications"]:
                params_base[key] = experiment["Param Modifications"][key]
        if experiment["State Modifications"]:
            state_base = deepcopy(state_base)
            for key in experiment["State Modifications"]:
                state_base[key] = experiment["State Modifications"][key]
        msi = self.build_implementation(params_base)
        state, params = msi.prepare_state_and_params(
            state_base,
            params_base,
            state_preperation_functions=state_preperation_functions,
            parameter_preperation_functions=parameter_preperation_functions,
        )

        state = msi.execute_blocks(state, params, experiment["Blocks"])
        df = post_processing_function(state, params)

        if metrics_functions:
            metrics = {}
            for metrics_function in metrics_functions:
                metrics_function(metrics, state, params, df)
            metrics = pd.Series(metrics)
        else:
            metrics = None

        return state, params, msi, df, metrics

    def run_experiments(
        self,
        experiments,
        params_base,
        state_base,
        post_processing_function,
        state_preperation_functions=None,
        parameter_preperation_functions=None,
        metrics_functions=None,
    ):
        state_l = []
        params_l = []
        df_l = []
        metrics_l = []
        for experiment in experiments:
            for i in range(experiment["Monte Carlo Runs"]):
                state, params, msi, df, metrics = self.run_experiment(
                    experiment,
                    params_base,
                    state_base,
                    post_processing_function,
                    state_preperation_functions=state_preperation_functions,
                    parameter_preperation_functions=parameter_preperation_functions,
                    metrics_functions=metrics_functions,
                )
                df["Monte Carlo Run"] = i + 1
                df["Experiment"] = experiment["Name"]
                metrics.loc["Monte Carlo Run"] = i + 1
                metrics.loc["Experiment"] = experiment["Name"]
                metrics.name = "{}-{}".format(experiment["Name"], i + 1)
                state_l.append(state)
                params_l.append(params)
                df_l.append(df)
                metrics_l.append(metrics)
        df = pd.concat(df_l)
        metrics = pd.concat(metrics_l, axis=1).T
        return df, metrics, state_l, params_l

    def metaprogramming_python_states(
        self, model_directory, overwrite=False, default_values=None
    ):
        path = model_directory + "/states.py"
        if not overwrite:
            assert "states.py" not in os.listdir(
                model_directory
            ), "The states file is already written, either delete it or switch to overwrite mode"
        out = ""
        unique_types = [x.variables for x in self.state.values()]
        unique_types = [set(y.type.original_type_name for y in x) for x in unique_types]
        unique_types = set().union(*unique_types)
        out = ""
        out += "from .types import {}".format(", ".join(unique_types))
        out += "\n"
        out += "from typing import TypedDict"
        out += "\n"
        out += "\n"

        for state in self.state:
            out += self.state[state].name_variable
            out += " = "
            d = self.state[state].variables
            d = [(x.name, x.type.original_type_name) for x in d]
            d = ["'{}': {}".format(x[0], x[1]) for x in d]
            d = ", ".join(d)
            d = "{" + d + "}"
            out += "TypedDict('{}', {})".format(self.state[state].name, d)
            out += "\n"
        out += "\n"
        out += "state: GlobalState = "
        out += "{"
        for x in self.state["Global State"].variables:
            out += '"{}"'.format(x.name)
            out += ": "
            val = "None"
            if default_values:
                if x.name in default_values:
                    val = str(default_values[x.name])
            out += val
            out += ",\n"
        out += "}"

        with open(path, "w") as f:
            f.write(out)

    def metaprogramming_python_parameters(
        self, model_directory, overwrite=False, default_values=None
    ):
        path = model_directory + "/parameters.py"
        if not overwrite:
            assert "parameters.py" not in os.listdir(
                model_directory
            ), "The parameters file is already written, either delete it or switch to overwrite mode"
        out = ""

        unique_types = (
            set(self.system_parameters_types.values())
            .union(set(self.functional_parameters_types.values()))
            .union(set(self.behavioral_parameters_types.values()))
        )
        unique_types = [x for x in unique_types if x != "str"]

        out = ""
        out += "from .types import {}".format(", ".join(unique_types))
        out += "\n"
        out += "from typing import TypedDict"
        out += "\n"
        out += "\n"

        d = self.system_parameters_types
        d = [(x, d[x]) for x in d]
        d = ["'{}': {}".format(x[0], x[1]) for x in d]
        d = ", ".join(d)
        d = "{" + d + "}"

        out += "SystemParameters = TypedDict('SystemParameters', {})".format(d)
        out += "\n\n"

        d = self.behavioral_parameters_types
        d = [(x, d[x]) for x in d]
        d = ["'{}': {}".format(x[0], x[1]) for x in d]
        d = ", ".join(d)
        d = "{" + d + "}"

        out += "BehavioralParameters = TypedDict('BehavioralParameters', {})".format(d)
        out += "\n\n"

        d = self.functional_parameters_types
        d = [(x, d[x]) for x in d]
        d = ["'{}': {}".format(x[0], x[1]) for x in d]
        d = ", ".join(d)
        d = "{" + d + "}"

        out += "FunctionalParameters = TypedDict('FunctionalParameters', {})".format(d)
        out += "\n\n"
        out += """Parameters = TypedDict("Parameters",{**BehavioralParameters.__annotations__,
 **FunctionalParameters.__annotations__,
**SystemParameters.__annotations__})"""
        out += "\n\n"

        out += "functional_parameters: FunctionalParameters = "
        out += "{"
        for key in self.functional_parameters_types:
            out += '"{}"'.format(key)
            out += ": "
            val = "None"
            if default_values:
                if key in default_values:
                    val = str(default_values[key])
            out += val
            out += ",\n"
        out += "}"
        out += "\n\n"

        out += "behavioral_parameters: BehavioralParameters = "
        out += "{"
        for key in self.behavioral_parameters_types:
            out += '"{}"'.format(key)
            out += ": "
            val = "None"
            if default_values:
                if key in default_values:
                    val = str(default_values[key])
            out += val
            out += ",\n"
        out += "}"
        out += "\n\n"

        out += "system_parameters: SystemParameters = "
        out += "{"
        for key in self.system_parameters_types:
            out += '"{}"'.format(key)
            out += ": "
            val = "None"
            if default_values:
                if key in default_values:
                    val = str(default_values[key])
            out += val
            out += ",\n"
        out += "}"
        out += "\n\n"

        out += "parameters: Parameters = {**behavioral_parameters, **functional_parameters, **system_parameters}"

        with open(path, "w") as f:
            f.write(out)

    def metaprogramming_boundary_actions(
        self, model_directory, overwrite=False, default_values=None
    ):
        path = model_directory + "/boundary_actions.py"
        if not overwrite:
            assert "boundary_actions.py" not in os.listdir(
                model_directory
            ), "The boundary actions file is already written, either delete it or switch to overwrite mode"
        out = ""

        unique_spaces = set().union(
            *[x.all_spaces_used for x in self.boundary_actions.values()]
        )
        unique_spaces = [x.name_variable for x in unique_spaces]

        out += "from .spaces import {}".format(", ".join(unique_spaces))
        out += "\n\n"
        for x in self.boundary_actions.values():
            out += "def "
            out += x.model_name
            out += "(state, params) -> ({}):".format(
                ", ".join([y.name_variable for y in x.codomain])
            )
            out += "\n\n"

        with open(path, "w") as f:
            f.write(out)

    def metaprogramming_julia_types(self, model_directory, overwrite=False):
        path = model_directory + "/types.jl"
        if not overwrite:
            assert "types.jl" not in os.listdir(
                model_directory
            ), "The types file is already written, either delete it or switch to overwrite mode"

        shutil.copyfile("src/TypeMappings/types.jl", path)

    def metaprogramming_julia_spaces(
        self, model_directory, cadCAD_path, overwrite=False
    ):
        path = model_directory + "/spaces.jl"
        if not overwrite:
            assert "spaces.jl" not in os.listdir(
                model_directory
            ), "The spaces file is already written, either delete it or switch to overwrite mode"

        out = """include("{}")
include("types.jl")
using .Spaces: generate_space_type

""".format(
            cadCAD_path
        )

        for space in self.spaces:
            name = self.spaces[space].name
            schema = self.spaces[space].schema
            schema = ["{}={}".format(x, schema[x].original_type_name) for x in schema]
            if len(schema) >= 1:
                schema = ", ".join(schema) + ","
                out += 'generate_space_type(({}), "{}")'.format(schema, name)
                out += "\n"
            # out += "{} = Spaces.{}".format(name, name)

        with open(path, "w") as f:
            f.write(out)

    def build_implementation(self, params):
        return MathSpecImplementation(self, params)

    def _set_source_code(self):
        if "python" not in self.implementations:
            self.source_code = None
            return
        self.source_code = deepcopy(self.implementations["python"])
        for x in self.source_code:
            for y in self.source_code[x]:
                self.source_code[x][y] = getsource(self.source_code[x][y])


class MathSpecImplementation:
    def __init__(self, ms: MathSpec, params):
        self.ms = deepcopy(ms)
        self.params = params
        self.control_actions = self.load_control_actions()
        self.boundary_actions = self.load_boundary_actions()
        self.policies = self.load_policies()
        self.mechanisms = self.load_mechanisms()
        self.stateful_metrics = self.load_stateful_metrics()
        self.metrics = self.load_metrics()
        self.load_wiring()
        self.load_components()
        self.load_source_files()

    def load_control_actions(self):
        control_actions = {}
        for ca in self.ms.control_actions:
            ca = self.ms.control_actions[ca]
            opts = ca.control_action_options
            if len(opts) == 0:
                print("{} has no control action options".format(ca.name))
            else:
                if len(opts) == 1:
                    opt = opts[0]
                else:
                    assert (
                        "FP {}".format(ca.name) in self.params
                    ), "No functional parameterization for {}. To fix this error, add {} to the parameters passed to ms.build_implementation. Option can be: {}".format(
                        ca.name, "FP " + ca.name, [x.name for x in opts]
                    )
                    opt = self.ms.functional_parameters["FP {}".format(ca.name)][
                        self.params["FP {}".format(ca.name)]
                    ]

                if "python" not in opt.implementations:
                    print(
                        "No python implementation for {} / {}. To fix this, go to Implementations/Python/ControlActions and add {}".format(
                            ca.name, opt.name, opt.name
                        )
                    )
                else:
                    control_actions[ca.name] = opt.implementations["python"]
        return control_actions

    def load_boundary_actions(self):
        boundary_actions = {}
        for ba in self.ms.boundary_actions:
            ba = self.ms.boundary_actions[ba]
            opts = ba.boundary_action_options
            if len(opts) == 0:
                print("{} has no boundary action options".format(ba.name))
            else:
                if len(opts) == 1:
                    opt = opts[0]
                else:
                    assert (
                        "FP {}".format(ba.name) in self.params
                    ), "No functional parameterization for {}. To fix this error, add {} to the parameters passed to ms.build_implementation. Option can be: {}".format(
                        ba.name, "FP " + ba.name, [x.name for x in opts]
                    )

                    opt = self.ms.functional_parameters["FP {}".format(ba.name)][
                        self.params["FP {}".format(ba.name)]
                    ]

                if "python" not in opt.implementations:
                    print(
                        "No python implementation for {} / {}. To fix this, go to Implementations/Python/BoundaryActions and add {}".format(
                            ba.name, opt.name, opt.name
                        )
                    )
                else:
                    boundary_actions[ba.name] = opt.implementations["python"]
        return boundary_actions

    def load_mechanisms(self):
        mechanisms = {}
        for m in self.ms.mechanisms:
            m = self.ms.mechanisms[m]
            if "python" not in m.implementations:
                print(
                    "No python implementation for {}. To fix this, go to Implementations/Python/Mechanisms and add {}".format(
                        m.name, m.name
                    )
                )
            else:
                mechanisms[m.name] = m.implementations["python"]
        return mechanisms

    def load_single_wiring(self, wiring):
        hold = wiring
        domain_sizes = {}
        for x in wiring.components:
            domain_sizes[x.name] = len(x.domain)
        components = [x.name for x in wiring.components]
        if wiring.block_type == "Stack Block":

            def wiring(state, params, spaces):
                for component in components:
                    spaces = self.blocks[component](state, params, spaces)
                return spaces

        elif wiring.block_type == "Parallel Block":

            spaces_mapping = {}

            for y in [x.name for x in wiring.domain_blocks2]:
                spaces_mapping[y] = []

            for i, x in enumerate([x.name for x in wiring.domain_blocks2]):
                spaces_mapping[x].append(i)

            def wiring(state, params, spaces):
                spaces_mapping_temp = deepcopy(spaces_mapping)
                codomain = []
                for component in components:
                    if component in spaces_mapping_temp:
                        spaces_i = [spaces[i] for i in spaces_mapping_temp[component]][
                            : domain_sizes[component]
                        ]
                        # Fix for repeated block names
                        spaces_mapping_temp[component] = spaces_mapping_temp[component][
                            domain_sizes[component] :
                        ]
                    else:
                        assert component in [
                            x.name for x in hold.domain_blocks_empty
                        ], "{} not in domain_blocks_empty of wiring {}".format(
                            component, hold
                        )
                        spaces_i = []
                    spaces_i = self.blocks[component](state, params, spaces_i)
                    if spaces_i:
                        codomain.extend(spaces_i)
                return codomain

        else:
            assert False

        return wiring

    def load_policies(self):
        policies = {}
        for p in self.ms.policies:
            p = self.ms.policies[p]
            opts = p.policy_options
            if len(opts) == 0:
                print("{} has no policy options".format(p.name))
            else:
                if len(opts) == 1:
                    opt = opts[0]
                else:
                    assert (
                        "FP {}".format(p.name) in self.params
                    ), "No functional parameterization for {}. To fix this error, add {} to the parameters passed to ms.build_implementation. Option can be: {}".format(
                        p.name, "FP " + p.name, [x.name for x in opts]
                    )
                    opt = self.ms.functional_parameters["FP {}".format(p.name)][
                        self.params["FP {}".format(p.name)]
                    ]

                if "python" not in opt.implementations:
                    print(
                        "No python implementation for {} / {}. To fix this, go to Implementations/Python/Policies and add {}".format(
                            p.name, opt.name, opt.name
                        )
                    )
                else:
                    policies[p.name] = opt.implementations["python"]
        return policies

    def load_stateful_metrics(self):
        stateful_metrics = {}

        for sm in self.ms.stateful_metrics_map:
            sm = self.ms.stateful_metrics_map[sm]
            if "python" not in sm.implementations:
                print(
                    "No python implementation for {}. To fix this, go to Implementations/Python/StatefulMetrics and add {}".format(
                        sm.name, sm.name
                    )
                )
            else:
                stateful_metrics[sm.name] = sm.implementations["python"]

        return stateful_metrics

    def load_metrics(self):
        metrics = {}

        for m in self.ms.metrics:
            m = self.ms.metrics[m]
            if "python" not in m.implementations:
                print(
                    "No python implementation for {}. To fix this, go to Implementations/Python/Metrics and add {}".format(
                        m.name, m.name
                    )
                )
            else:
                metrics[m.name] = m.implementations["python"]

        return metrics

    def load_wiring(
        self,
    ):
        self.blocks = {}
        self.blocks.update(self.boundary_actions)
        self.blocks.update(self.control_actions)
        self.blocks.update(self.policies)
        self.blocks.update(self.mechanisms)

        self.wiring = {}

        wiring = [x for x in self.ms.wiring.values()]

        i = 1
        while i > 0:
            i = 0
            hold = []
            for w in wiring:
                components = [x.name for x in w.components]
                if all([x in self.blocks for x in components]):
                    i += 1
                    w2 = self.load_single_wiring(w)
                    assert w.name not in self.blocks, "{} was a repeated block".format(
                        w.name
                    )
                    if w2:
                        self.blocks[w.name] = w2
                        self.wiring[w.name] = w2

                else:
                    hold.append(w)
            wiring = hold
        if len(wiring) > 0:
            wiring = [x.name for x in wiring]
            print("The following wirings were not loading: {}".format(wiring))

    def validate_state_and_params(self, state, parameters):

        k1 = state.keys()
        k2 = [x.name for x in self.ms.state["Global State"].variables]

        not_in_state = [x for x in k2 if x not in k1]
        shouldnt_be_in_state = [x for x in k1 if x not in k2]
        assert (
            len(not_in_state) == 0
        ), "The following state variables are missing: {}".format(not_in_state)
        assert (
            len(shouldnt_be_in_state) == 0
        ), "The following state variables are extra: {}".format(shouldnt_be_in_state)

        k1 = parameters.keys()
        k2 = self.ms.parameters.all_parameters + list(
            self.ms.functional_parameters.keys()
        )

        not_in_params = [x for x in k2 if x not in k1]
        shouldnt_be_in_params = [x for x in k1 if x not in k2]
        assert (
            len(not_in_params) == 0
        ), "The following parameters are missing: {}".format(not_in_params)
        assert (
            len(shouldnt_be_in_params) == 0
        ), "The following parameters are extra: {}".format(shouldnt_be_in_params)

    def prepare_state_and_params(
        self,
        state,
        params,
        state_preperation_functions=None,
        parameter_preperation_functions=None,
    ):
        self.validate_state_and_params(state, params)
        state = deepcopy(state)
        params = deepcopy(params)
        state["Stateful Metrics"] = self.stateful_metrics
        state["Metrics"] = self.metrics
        if state_preperation_functions:
            for f in state_preperation_functions:
                if len(signature(f).parameters) == 1:
                    state = f(state)
                elif len(signature(f).parameters) == 2:
                    state = f(state, params)
                else:
                    assert (
                        False
                    ), "Incorrect number of parameters for the state preperation function"
                assert (
                    state is not None
                ), "A state must be returned from the state preperation functions"
        if parameter_preperation_functions:
            for f in parameter_preperation_functions:
                if len(signature(f).parameters) == 1:
                    params = f(params)
                elif len(signature(f).parameters) == 2:
                    params = f(params, state)
                else:
                    assert (
                        False
                    ), "Incorrect number of parameters for the state preperation function"
                assert (
                    params is not None
                ), "A parameter set must be returned from the parameter preperation functions"
        return state, params

    def load_components(self):
        self.components = {}
        self.components.update(self.control_actions)
        self.components.update(self.boundary_actions)
        self.components.update(self.policies)
        self.components.update(self.mechanisms)
        self.components.update(self.wiring)

    def execute_blocks(self, state, params, blocks):
        for block in blocks:
            self.components[block](state, params, [])
        return state

    def load_source_files(self):
        self.source_files = {}
        for key in self.components:
            self.source_files[key] = getsource(self.components[key])

    def print_source_code_files(self, keys=None):
        if not keys:
            keys = list(self.source_files.keys())
        for key in keys:
            print("-" * 20 + key + "-" * 20)
            print(self.source_files[key])
            print("\n\n\n")
