# Annual Presentation

Presented during BlockScience Town Hall on 6/26/2024
Author: Sean McOwen

## Executive Summary

## The Evolving Objectives of the Mathematical Specification Mapping Library Project

### Prior Objectives

- "Writing mathematical specifications can be a difficult process, especially when variable names are changed or new mechanisms are introduced. MSML seeks to streamline the process with automations as well as enhance the abilities of static math specs to deliver deeper insights. Because it is automated, one can write specifications at different levels of details or for different purposes."
- Ideation Tool for Client + R&D Work
- Accelerates cadCAD Modeling
- Bridges GDS and Software Implementation

```mermaid
graph TD
A[JSON Object \n\n Each spec has a repo for tracking changes \n Must conform to the json specification \n Defines all aspects of the spec including blocks, spaces and actions] -->B[MSML Object \n\n JSON file is parsed, with validations and mappings along the way \n Can show different views on the fly]
    B --> C[Report Outputs \n\n Automatically build reports for the full spec or subviews \n Example: all blocks with an effect on variable XYZ]

```

### Evolving Objectives

- MSML as a Rosetta Stone between groups, programming languages and paradigms
- MSML as a tool to enhance iterative development in end-to-end / full life-cycle systems engineering

## Year in Review, by the Numbers

- Current production repository started on December 2023, old repository disregarded in these counts as POC work
- 244 Issues Closed
- 619 Commits of Code
- 28 releases on pypi over the last year

## Year in Review, by the Topics

## Client Deployment Retrospective

- There were 4 client projects where MSML was utilized for creating a mathematical specification and 1 which is currently using it for specification plus the new executable blocks functionality for running simulations before moving to a cadCAD model
- Overall the deployments went well but there is room for improvement with:
    - Improving clarity, especially for less technical stakeholders
    - Improving onboarding for those using the library
    - Improving the GUI and interfaces for easier development of specs
    - Improving documentation and boilerplate "Introduction to MSML" materials for those not familiar with GDS or MSML


## Research Notes Roster

## Canonical Examples Roster

## Future Plans

## A Thank You to All Supporters

## Questions?