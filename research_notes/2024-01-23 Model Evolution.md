# Model Evolution

The following is a work-in-progress idea of how MSML might support model building. One can think of a few phases of a model over its lifetime.

1. Requirements Gathering & Problem Definition
2. GDS Model
3. MSML Model without Implementation
4. MSML Model with Implementation
5. Simulation/cadCAD Model
6. Digital Twin

## Requirements Gathering & Problem Definition

The phase of the process where the modeler makes decisions on what requirements need to be fulfilled and what the definition of the problem is.

## GDS Model

A high level model showing blocks that represent actions within the system as well as their spaces. At this stage, there is no finer grained detail into things such as policy or mechanism blocks.

## MSML Model without Implementation

A refinement of the GDS model to build out state, parameter spaces, as well as more fine grained details and wirings.

## MSML Model with Implementation

The evolution of the model where functional parameterization and policy/boundary action/control action options are built out detailing different choices of logic can fit into individual blocks.

## Simulation/cadCAD Model

The simulation model capable of running the logic in the blocks in full scale experiments.

## Digital Twin

The enrichment of the model to not only cover simulation, but also backtesting a simulation model against live data as well as extrapolating data forward in a monte carlo fashion.