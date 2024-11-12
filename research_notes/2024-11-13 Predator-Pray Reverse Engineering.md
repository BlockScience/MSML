# Predator-Prey Reverse Engineering Example

## Executive Summary

- As part of an effort to make high quality canonical examples, a predator-prey model is being iterated on to show a full end-to-end modeling workflow and the repository can be found [here](https://github.com/BlockScience/Predator-Prey-Canonical-Example)
- Today we will go through the process of reverse engineering a past repository of code and updating it to be an MSML-compliant spec
- This specific type of ideation is often done when presented with a system that is already in a production enviroment but needs to be modeled through simulations or digital twins

## Predator-Prey Background

- The Predator-Prey model is often used as an example in mathematics classes to illustrate equilibrium behaviors and modeling for it
- Generally, the model is for representing the Lotka–Volterra equations, which are first order, non-linear differential equations
- However, for our purposes, and purposes of the legacy model, we impose a discrete time to the system and model it instead as an agent-based simulation
- The legacy model used comes from the [cadCAD demos repository](https://github.com/cadCAD-org/demos/tree/master/demos/Agent_Based_Modeling/prey_predator_abm) and is ported into Obsidian