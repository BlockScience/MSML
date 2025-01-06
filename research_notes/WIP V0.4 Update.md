# MSML v0.4 Update

Updated through V0.3.14

## MSML Review

MSML is a library for standardizing the creation of mathematical specifications as JSON objects as well as aiding in the automation of report and visualization creation from these standardized JSON. Please see the [README](../README.md) for more information.

## Updates from to v0.3.0 to V0.4.0

A total of XX issues were closed out over the development cycle, which broadly fall into the following categories below. However, for brevity, only the main updates will be covered, many smaller updates such as bug fixes, small improvements, etc. will not be noted here but can be found in the research journal.

### Implementations / Executable Code Blocks

- Boundary actions are now added in as an implementation
- Full wiring runs are now working/executing
- New functionality for validation of state and params before running wiring or blocks
- Stateful metrics were implemented and now are passed in as a module in the state that implementations can access and use
- State and parameter preparation function paradigms were added into MSML to allow for setting up parameters and state prior to simulations / executable codes
- Metrics were added into implementations to allow for mapping code to them
- Functionality was added in for linking source code to the blocks for easy viewing and writing into markdown reports; as well a source code printing function was added

### Metaprogramming

- Initial R&D into metaprogramming for Julia has yielded some success on metaprogramming for spaces and types in cadCAD.jl from MSML
- Boundary action metaprogramming has been started

### Simulations

- The mini-simulation runner was created
- Post-processing function paradigm was added into the mini-simulation runner
- Metric functions were added to the runner for post processing of data
- Ability to run lists of blocks built out

### Canonical Examples

- The MSML template was added as both a canonical example as well as a forkable template for getting started quickly with MSML
- The predator prey canonical example was created and has been completed up to simulations
- Introduction of the retirement planning canonical example as a guided walk through example
- Introduction of the Rideshare Modeling canonical example for building a massive end-to-end model of a rideshare simulation
- Big improvements to the starter repo including adding in executable code blocks and better naming, which was later rolled into the MSML template

## Research Notes

- A research note on metrics was created and worked through with stakeholders
- A research note on parameter class names and different ways that it could be implemented (plan is for a "bring your own ontology" approach moving forward)
- Development note on working through an issue with Latex escape characters
- Development research note for future proposals of changes to MSML

## Improvements and Convenience Functions

- A lot of bugs were discovered and fixed through dogfooding on client work and canonical examples
- Some major improvements across the board in terms of quality of life stuff; a lot of new assertions that are more descriptive added to easily see where the issues are
- New convenience functions such as one to remove dummy repo components after the starter repo scaffolding is no longer needed
- A parameter table creation function was built which automatically creates a markdown table of parameters, descriptions, and default values for experiment notebooks
- Improvements of assertions
- An automatic README writer was added in
- A functionality that automatically writes issues from an MSML scaffold into a github issues was built out

## Presentations

- The annual presentation was given in June 2024 during the town hall
- A governance pod presentation titled "Obsidian, the Mathematical Specification Mapping Library, and End-to-End Modeling" was given
- October seminar presentation
- A research note on Predator-Prey-Ideation through reverse engineering was completed which shows how to turn legacy code into an MSML scaffold then automatically port it into github issues for easy organization of the next step (the actual MSML spec), presented in seminar

## Future Research Arc

- The V0.5 roadmap is defined XX