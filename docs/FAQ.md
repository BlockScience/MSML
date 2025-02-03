---
title: FAQ
layout: page
nav_order: 6
---

The following are frequently asked questions with regards to MSML.

## What structure or paradigm is MSML based off of?

- The structure is based off of Generalzied Dynamical Systems but with some semantic additions mainly coming out of past specs that were built at BlockScience
- This, however, may soon change to be an ontology based version where there is the super class of "Block" and then users bring their own ontologies instead of having blocks defined out as boundary actions, control actions, policies, mechanisms and wirings

## What are the capabilities of MSML?

- Writing a spec that has automated reporting attached to it in the form of an obsidian vault
- Binding code and trying out running blocks of logic
- Mini simulations
- Future capabilities that are in flight including more reporting styles, meta-programming to cadCAD, bigger simulation running and canonical examples

## What deliverables can MSML produce?

- The short answer is the main deliverables can be seen in the [MSML template](https://github.com/BlockScience/MSML-Template), otherwise below are some of the main deliverables
- Obsidian vault creation for internal development in the beginning and then eventually easily interfacing with clients, markdown files are created for every component for easily zooming in and out of the system
- Notebooks and paradigms for internal dev of testing and playgrounds for testing out bound code on specs
- Single simulation and simulation sweep notebooks for creating interfaces that clients can easily modify for running their own experiments as well as setting up experiment notebooks for client deliverables

## What is the difference between MSML and cadCAD?

- The underlying paradigm of GDS is the same but right now cadCAD only does the general block approach and not the semantic enhancements of things like boundary action, but because all the blocks in MSML are still the same block base class they all will function the same in cadCAD
- Spaces are the same (but with respect to cadCAD 1.0 and not cadCAD legacy)
- cadCAD should be for running large scale simulations optimized for speed, versus MSML can be used for scaffolding
- MSML should be better suited for ideation and working through “bread-boarding” before moving on to a stricter paradigm of cadCAD for more optimized simulations


## What level of customization does MSML provide?

- The actual writing of specs is very flexible as one can encode nearly anything into them
- There are future issues to tackle on expanding the customizability of reporting outputs