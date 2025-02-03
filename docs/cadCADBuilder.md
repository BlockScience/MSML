---
title: cadCAD Builder
layout: page
nav_order: 5
---

MSML provides interfaces for creating cadCAD style models that don't require end users poking around the actual code to use. The idea is that it provides a layer for data scientists to experiment just with toggling starting state and parameters and executing pre-packaged models.

## Components

### Inputs

The following is required for building the cadCAD model:

1. A math spec object with code bindings
2. A list of blocks which should be executed for each timestep
3. What state preparation and parameter preparation functions should be included to automatically run on experiment creation


### Outputs

The following is outputted by the creation function:

1. State Space: The nested and typed dictionary of all types for the state in the simulation that the data scientist needs to define
2. Parameter Space: The dictionary of parameters that the data scientist needs to define
3. Model: The executable model that can spawn experiments to run given valid state space and parameter space passed

## Creating a cadCAD Model in a Notebook

The [template notebook on building cadCAD models](https://github.com/BlockScience/MSML-Template/blob/main/notebooks/Build%20cadCAD.ipynb) shows how to create a cadCAD model from an MSML model.

## Using cadCAD Model Repositories

A recommended design pattern is to have MSML developers create a batch of cadCAD models to be run within a cadCADModels folder [similar to the template](https://github.com/BlockScience/MSML-Template/tree/main/cadCADModels).

The template also has an example of running the pre-built cadCAD models [here](https://github.com/BlockScience/MSML-Template/blob/main/notebooks/Pre-built%20cadCAD.ipynb).


## Model Functionality

### Experiment Creation

- To create an experiment, one runs model.create_experiment(state, params) and passes in a valid state and parameter dictionary
- The record_trajectory flag if set to true will record the state after each step of the simulation
- The use_deepcopy flag if set to true will use deepcopy for the trajectory recording


### Running Experiments

- Using experiment.run(T) where T is the number of time steps will advance the simulations that many timesteps
- If record_trajectory was set to true then the trajectories can be accessed from experiment.trajectories, if not you can always access the current state of the experiment by calling experiment.state

### Batch Experiments

- Batch experiments can be created and run through model.create_batch_experiments(...). An example of it is shown in the pre-built cadCAD notebook.