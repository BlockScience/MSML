# MSML v0.3 Update

Updated through V0.3.6

## MSML Review

MSML is a library for standardizing the creation of mathematical specifications as JSON objects as well as aiding in the automation of report and visualization creation from these standardized JSON. Please see the [README](../README.md) for more information.

## Updates from to v0.3.0 to V0.4.0

A total of XX issues were closed out over the development cycle, which broadly fall into the following categories:

### Implementations / Executable Code Blocks

- Boundary actions are now added in as an implementation
- Full wiring runs are now working/executing
- New functionality for validation of state and params before running wiring or blocks
- Stateful metrics were implemented and now are passed in as a module in the state that implementations can access and use

### Metaprogramming

- Initial R&D into metaprogramming for Julia has yielded some success on metaprogramming for spaces and types in cadCAD.jl from MSML
- Boundary action metaprogramming has been started

### Canonical Examples

- Introduction of the retirement planning canonical example as a guided walk through example
- Introduction of the Rideshare Modeling canonical example for building a massive end-to-end model of a rideshare simulation
- Big improvements to the starter repo including adding in executable code blocks and better naming

## Research Notes

- A research note on metrics was created and worked through with stakeholders
- A research note on parameter class names and different ways that it could be implemented (plan is for a "bring your own ontology" approach moving forward)
- Development note on working through an issue with Latex escape characters
- Development research note for future proposals of changes to MSML

## Improvements and Convenience Functions

- A lot of bugs were discovered and fixed through dogfooding on client work and canonical examples
- Some major improvements across the board in terms of quality of life stuff; a lot of new assertions that are more descriptive added to easily see where the issues are
- New convenience functions such as one to remove dummy repo components after the starter repo scaffolding is no longer needed

## Future Research Arc

- The V0.5 roadmap is defined XX