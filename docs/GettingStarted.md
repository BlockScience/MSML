---
title: Getting Started
nav_order: 4
layout: page
---

Getting started with your first MSML specification can seem like a daunting task but this short guide will hopefully make it easier.

## 1. Review the Concepts

- Within this documentation, you can find specific technical documentation including the background theory and the components under "Technical Documentation"
- Feel free to go as deep into it as you feel necessary; if you prefer just jumping straight in you can move on to step 2 or step 3

## 2. Review Canonical Examples & Tutorials

- Within this documentation, you can find a section "Canonical Examples" which has links to examples and tutorials on how to use MSML
- The MSML template is the easiest to grasp and also is what is forked to start a new MSML specification so it is recommended above all the others to first review

## 3. Fork the MSML Template

- The [MSML Template](https://github.com/BlockScience/MSML-Template) can be forked by pushing the green button labeled "Use this template"
- The template comes with starter "DUMMY" components to show the format of a repository

## 4. Write New Components

- The core functionality for MSML is writing new components without code attatched, the recommended flow is to add components and then every time restart the kernel and run the "Build Obsidian.ipynb" notebook
    - This notebook will flag any errors that might have been introduced
    - If there are no errors, the Obsidian vault will be updated with your components which you can look through
    - You **must** restart the python kernel each time to make sure that the notebook pulls the latest components in
- To add a component, go into the src folder and then locate the sub-folder which is the new component you are adding first
    - For example, if it is spaces, go into the "Spaces" folder
- To add a new component to a file already existing, go into that file, such as "Dummy.py", the code in this file of the template looks like:

```python
dummy_abcedf_space = {
    "name": "DUMMY ABCDEF Space",
    "schema": {
        "string": "DUMMY ABCDEF Type",
    },
}


dummy_string_length_space = {
    "name": "DUMMY String Length Space",
    "schema": {
        "string": "DUMMY ABCDEF Type",
        "length": "DUMMY Integer Type",
        "unique_length": "DUMMY Integer Type",
    },
}

dummy_spaces = [dummy_abcedf_space, dummy_string_length_space]
```
- Add in a new component with the same schema, and then add that to "dummy_spaces" list
- It is recommended to add separate files for sets of components such as "User.py" for spaces that are related to users and eventually delete "Dummy.py" in favor of specifically named files
- When adding a new file, make sure to update the "\_\_init\_\_.py" file, which looks like:

```python
from .Dummy import dummy_spaces

spaces = []
spaces.extend(dummy_spaces)
```

- You would import something like user_spaces from .User and then add "spaces.extend(user_spaces)" to make sure the new spaces are integrated in
- After adding a new component, kernel restart and re-run the Obsidian creation notebook and make sure it runs successfully

## 5. Bind Code to Components

- MSML has extended capabilities that allow for binding code to different components
- Go to the folder "src/Implementations/Python"
- For whichever components you want to define code for, move to that folder, for example "BoundaryActions.py"
- The "\_\_init\_\_" file looks like:

```python
from .Dummy import v1_dummy_boundary, v1_dummy_boundary2, v2_dummy_boundary2

boundary_action_options = {
    "Length-1 ABC Equal Weight Option": v1_dummy_boundary,
    "DUMMY Length-2 ABC Equal Weight Option": v1_dummy_boundary2,
    "DUMMY Length-2 ABC Equal Weight 2 Option": v2_dummy_boundary2,
}
```

- Each key here corresponds to the name of a boundary action option defined out in the specification, for any new boundary action options without functions you will simply add the key and a function representing it in the same format as the other functions (with three parameters of state, parameters and spaces)
- The only special cases are metrics and stateful metrics which have a slightly different set of arguments but are defined out the same way, by adding a key with the exact name of the metric/stateful metric
- Mechanisms also do not have options, so instead the key for these functions should be the mechanism name
- The "Implementation Playground.ipynb" can be used to test out the functions after creation
- Test cases can also be built up from these functions
- Wiring functionality is automatically created as long as every single component has a function definition (and if not a warning will be given when loading)
- You may need to update the base state and parameters to get the notebook running which is covered in the next section

## 6. Create a Basic Simulation

### State and Parameters

- For a basic simulation, what is needed first of all is either one or multiple base states and base parameters
- Ensure the base parameter and state have all the components defined out in the spec and nothing extra (if there are any functional parameterizations missing then MSML will alert you)
- Under simulation/config/params.py, you can define out as many parameter sets that will be used as baselines in experiments and simulations. The template repository looks like:

```python
from copy import deepcopy

params_base = {
    "DUMMY D Probability": 0.5,
    "DUMMY Length Multiplier": 3,
    "FP DUMMY Length-1 DEF Control Action": "DUMMY Length-1 DEF Equal Weight Option",
    "FP DUMMY Length-2 ABC Combo Boundary Action": "DUMMY Length-2 ABC Equal Weight Option",
}

params_test1 = deepcopy(params_base)
params_test1["DUMMY D Probability"] = 1
params_test1["FP DUMMY Length-1 DEF Control Action"] = (
    "DUMMY Length-1 DEF D Probability Option"
)


params_test2 = deepcopy(params_base)
params_test2["DUMMY D Probability"] = 0
params_test2["FP DUMMY Length-1 DEF Control Action"] = (
    "DUMMY Length-1 DEF D Probability Option"
)
```
- If you add any new paramter sets, make sure to add them to the "\_\_init\_\_.py" file in the config folder as well as one level up in the simulation folder
- Do the same for the state, found in simulation/config/state.py, which looks like:

```python
from copy import deepcopy

state_base = {
    "Dummy": {"Words": "", "Total Length": None},
    "Time": 0,
    "Simulation Log": [],
}

state_test1 = deepcopy(state_base)
state_test1["Time"] = 100
```

### Pre and Post Processing
- The file "simulation/postprocessing/post.py" holds the post processing function that is applied after simulation runs to piece together simulation data
- The code below from the template shows a very basic version that takes a simulation log and transforms it into a dataframe

```python
import pandas as pd


def post_processing_function(state, params):
    df = pd.DataFrame(state["Simulation Log"])
    df["Length (Nominal)"] = (
        df["Length (Multiplied)"] / params["DUMMY Length Multiplier"]
    )
    df["D Count"] = df["Word"].apply(lambda x: x.count("D") if len(x) > 0 else None)
    return df
```

- The functions in "simulation/preprocessing/param_preperation.py" are for writing out functions that prepare pieces of the parameters before running (i.e. if you want to make sure assertions are true or if you want something like PARAM_A = 1 - PARAM_B instead of manually setting PARAM_A)
- The examples from the template:

```python
def check_d_probability(params):
    # If the functional parameterization is set to equal weight, override the D probability parameter to always be 1/3
    if (
        params["FP DUMMY Length-1 DEF Control Action"]
        == "DUMMY Length-1 DEF Equal Weight Option"
    ):
        params["DUMMY D Probability"] = 1 / 3
    return params
```

- The functions in "simulation/preprocessing/state_preperation.py" are for writing out functions that prepare pieces of state before running a simulation such as if you have a parameter of "number_of_agents" and want a function which actually creates the class instances of those agents before running
- The examples from the template:

```python
def compute_starting_total_length(state, params):
    state["Dummy"]["Total Length"] = params["DUMMY Length Multiplier"] * len(
        state["Dummy"]["Words"]
    )
    return state
```

- For all make sure to add the functions to both the folder and one level up's "\_\_init\_\_.py" file

### Running a Simulation

- In "notebooks/Single%20Simulation.ipynb", the first code block defined below shows what happends for defining out a simulation

```python
import sys
import os

sys.path.append(os.path.abspath('..'))


from simulation import (params_base, state_base, compute_starting_total_length, check_d_probability, post_processing_function,
                        percent_ending_in_d_metric, average_d_count_metric, plot_length_single_simulation)

from math_spec_mapping import load_from_json

"""# For development purposes
sys.path.append(os.path.abspath('../..'))
from MSML.src.math_spec_mapping import (load_from_json)"""

from copy import deepcopy
from src import math_spec_json

ms = load_from_json(deepcopy(math_spec_json))

# Start by logging the starting state
blocks = ["DUMMY Log Simulation Data Mechanism"]

# Add in 20 blocks alternating between the 2 boundary action wirings
blocks.extend(["DUMMY Length-2 Boundary Wiring",
               "DUMMY Length-1 Boundary Wiring"] * 10)

# Add in 30 blocks alternating between the 2 boundary action wirings and the control action wirings
blocks.extend(["DUMMY Length-2 Boundary Wiring",
               "DUMMY Length-1 Boundary Wiring",
               "DUMMY Control Wiring"] * 10)

# Define an experiment
experiment = {"Name": "Baseline",
               "Param Modifications": {"FP DUMMY Length-1 DEF Control Action": "DUMMY Length-1 DEF D Probability Option"},
               "State Modifications": {"Dummy": {"Words": "AA",
                                                 "Total Length": 1 # This is incorrect but we will see that it is in fact corrected by the state preperation function
                                                 }},
               "Blocks": blocks}

state, params, msi, df, metrics= ms.run_experiment(experiment,
                  params_base,
                  state_base,
                  post_processing_function,
                  state_preperation_functions=[compute_starting_total_length],
                  parameter_preperation_functions=[check_d_probability],
                  metrics_functions=[percent_ending_in_d_metric,
                                     average_d_count_metric])
```

- Import any new functionality defined from the prior steps in "from simultion import ...."
- Create a list of blocks that should be sequentially exexcuted for your simulation, these can be wirings or individual components, or a mix of both
- Define out an experiment object with:
    - A name
    - Any modifications to the base parameter set through "Param Modifications"
    - Any state modifications with "State Modifications"
    - Passing in the blocks to execute
- For the function, we pass in:
    - The defined experiment object
    - The base parameter set
    - The base state set
    - Any state preparation functions we want to apply
    - Any parameter preparation functions we want to apply
    - Any metric functions we want to apply (covered in section 8)
- The outputs are the ending state, the ending parameter set (only should be modified by parameter preparation functions), the math spec implementation object, the dataframe built from our post-processing function, and the metrics built from our metric functions (covered later)

## 7. Create Experiments

- To create sets of experiments (for reproducibility), first go into the file at "simulation/config/experiment.py"
- The full code looks like:

```python
blocks = ["DUMMY Log Simulation Data Mechanism"]
blocks.extend(["DUMMY Length-2 Boundary Wiring", "DUMMY Length-1 Boundary Wiring"] * 10)
blocks.extend(
    [
        "DUMMY Length-2 Boundary Wiring",
        "DUMMY Length-1 Boundary Wiring",
        "DUMMY Control Wiring",
    ]
    * 10
)

experiments_map = {}


experiments_map["Baseline"] = {
    "Name": "Baseline",
    "Param Modifications": None,
    "State Modifications": None,
    "Blocks": blocks,
    "Monte Carlo Runs": 5,
}

experiments_map["Control Option V2 Low D Probability"] = {
    "Name": "Control Option V2 Low D Probability",
    "Param Modifications": {
        "FP DUMMY Length-1 DEF Control Action": "DUMMY Length-1 DEF D Probability Option",
        "DUMMY D Probability": 0.1,
    },
    "State Modifications": None,
    "Blocks": blocks,
    "Monte Carlo Runs": 5,
}

experiments_map["Control Option V2 High D Probability"] = {
    "Name": "Control Option V2 High D Probability",
    "Param Modifications": {
        "FP DUMMY Length-1 DEF Control Action": "DUMMY Length-1 DEF D Probability Option",
        "DUMMY D Probability": 0.9,
    },
    "State Modifications": None,
    "Blocks": blocks,
    "Monte Carlo Runs": 5,
}
```
- To add new experiments we add keys into the experiments_map dictionary
- Each new experiment needs the following:
    - A name
    - Any modifications to the base parameter set through "Param Modifications"
    - Any state modifications with "State Modifications"
    - Passing in the blocks to execute
    - A number of monte carlo runs to execute on this experiment
- Within "notebooks/Experiment%20Simulations.ipynb" there is the following code which shows how to run multiple simulations

```python
import sys
import os

sys.path.append(os.path.abspath('..'))


from simulation import (params_base, state_base, compute_starting_total_length, check_d_probability, post_processing_function,
                        percent_ending_in_d_metric, average_d_count_metric, plot_length_experiment_simulation, plot_d_count_experiment_simulation,
                        experiments_map)
from IPython.display import display, Markdown
from math_spec_mapping import load_from_json, write_initial_state_variables_tables, write_parameter_table_markdown

"""# For development purposes
sys.path.append(os.path.abspath('../..'))
from MSML.src.math_spec_mapping import (load_from_json, write_initial_state_variables_tables, write_parameter_table_markdown)"""

from copy import deepcopy
from src import math_spec_json

ms = load_from_json(deepcopy(math_spec_json))

experiment_names = ["Baseline", "Control Option V2 Low D Probability", "Control Option V2 High D Probability"]
experiments = [experiments_map[x] for x in experiment_names]


df, metrics, state_l, params_l = ms.run_experiments(experiments,
                    params_base,
                    state_base,
                    post_processing_function,
                    state_preperation_functions=[compute_starting_total_length],
                    parameter_preperation_functions=[check_d_probability],
                    metrics_functions=[percent_ending_in_d_metric,
                                        average_d_count_metric,
                                        ])
```
- The primary differences are that:
    - One must modify the experiment_names variable to define out what experiments to run
    - The function run_experiments is used instead of run_experiment
    - The output is a dataframe of results with metadata on which simulations were run, the metrics and lists of ending states and parameters

## 8. Add Analytics & Metrics

- In the folder "simulation/analytics", one can add visualizations and other convenience functions for repeated analytics
- This folder is completely flexible to whatever the user wants to do and also can be ignored if it is preferred to write all analytics directly into the notebook
- The recommended paradigm is to write visualizations for single simulations in single.py and visualizations for experiments into experiments.py but it is only a recommendation
- In "simulation/postprocessing/metrics.py", metric functions can be written which define out metrics at the simulation run level (to see which simulations pass certain thresholds)
- The format is to have a dataframe passed with single simulation results and then assign values to the metric dictionary based on whatever logic one wants, for example, here are two metric functions defined out currently in the template:

```python
def percent_ending_in_d_metric(metrics, state, params, df):
    metrics["Percent Ending in D"] = (
        df["Word"].apply(lambda x: x[-1] == "D" if len(x) > 0 else None).mean()
    )


def average_d_count_metric(metrics, state, params, df):
    metrics["Average D Count"] = df["D Count"].mean()
```