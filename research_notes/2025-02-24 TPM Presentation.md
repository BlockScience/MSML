# TPM Pod Presentation

## Executive Summary

- This research note covers the important aspects of MSML as they relate to the technical project manager pod at BlockScience
- The primary question is how can TPMs support building of an MSML spec

## Internal Communications

- The primary way that MSML can aid internal communications is through having one working copy of the current specification of the system
    - It is highly recommended to use a git repository so that changes can be tracked easily for the different components
- The "Documentation & Reporting Outputs" covers the ways in which the spec itself can be put into many representations depending on the depth one wants to go in understanding the system generally or specific wirings and blocks
- Also important to note, the spec can be iteratively filled in - for example one could scaffold out only the blocks and spaces first, present the current wirings for confirmation to team members and only then begin to iterate on describing each component
- The example flow will make it clear how all these things could play out together

## External Communications

- The pieces from "Documentation & Reporting Outputs" are also meant to be client facing, but one can decide what is shown
- For example, a session with a client might revolve around one specific wiring in which case the obsidian vault could be utilized to show the wiring but also have the ability to poke into the components

## Documentation & Reporting Outputs

- **Obsidian Vault**: An obsidian vault can automatically be created to have all system components written as markdown files with linking between them. They are best viewed in Obsidian, but this document can be used to quickly jump between high level wirings and atomic components to align either internally or externally. An example of it is the [predator-prey vault](https://github.com/BlockScience/Predator-Prey-MSML/tree/main/reports/obsidian).
- **Glossary Report**: MSML can write markdown files and then translate them into PDFs. One of those reports is the glossary report which just gives the overall inventory of all components and their descriptions. An example is [here on the MSML template](https://github.com/BlockScience/MSML-Template/blob/main/reports/Glossary.pdf).
- **Additional Work-in-Progress Reports**: There are many other PDF reports in progress including ones that wrap everything needed to understand a wiring into one single report.

## Design, Modeling & Simulation

- Without going too into technical details, there are two ways to use MSML for simulations, both require binding code to the blocks, but are slightly different
- MSML's engine for running a simulation allows for defining out in great detail all the experiments to run, for example, this [notebook](https://github.com/BlockScience/MSML-Template/blob/main/notebooks/Experiment%20Simulations.ipynb) shows how in the template a bunch of simulations can be run
- The other option is to create a cadCAD export model which then gives a data scientist an object to use for testing that just needs a state space and parameter space but has all the logic bound into it, for example the template has an example of how to build it [here](https://github.com/BlockScience/MSML-Template/blob/main/notebooks/Build%20cadCAD.ipynb)
- The documentation covers a lot of what needs to be done for running these so we won't dive into details any further

## Where TPMs can be Involved

- Information sourcing
- Validation

## An Example TPM Aided Flow

- We will work through an example of how we might break down a simple project with iteration loops involving TPMs
- We will leverage the current canonical example in progress - the Predator Prey model

- I will add the following symbol to denote where TPMs especially could help out: 

### Phase 1 - Information Sourcing & Requirements Engineering


## A Future Flow: BDP -> MSML -> Code Enabled Specs -> MSML Simulations / cadCAD Simulations


## Additional Resource

- MSML Website