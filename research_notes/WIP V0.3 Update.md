# MSML v0.3 Update


## MSML Review

MSML is a library for standardizing the creation of mathematical specifications as JSON objects as well as aiding in the automation of report and visualization creation from these standardized JSON. Please see the [README](../README.md) for more information.

## Updates from to v0.2.2 to V0.3.0

A total of XX issues were closed out over the development cycle, which broadly fall into the following categories:

### Upgrading Types

- Now one enters a type name and there are different files that will designate the type across different programming languages i.e. python vs. typescript
- This feature loading is now language agonistic for putting together the JSON spec, one more step closer to not even needing to write the spec in python!
- Wiki links were added for the types in the spaces reporting
- Python, Typescript, and Julia type parsing is now supported!

### Metaprogramming

- Code mapping for python is completed allowing for beginning to metaprogram

### Metrics Updates

- For any "metrics_used" attributes, stateful_metrics are now allowed to be used as a metrics_used input
- Metrics used is now added to the policies so that they can be referenced as an input into how the policy is working
- Symbols used for when state variables/parameters are referenced in a metric are now mapped/displayed

### Displays

- There is now a displays object/mode that allows for wiring reports that put multiple wirings side by side, which is nice if you want to say have a group called "Monetary Policy Wirings" and you display all wirings related to monetary policy

### Wiring Improvements
- A new feature that recursively finds all state updates which occur at any point in the wiring and adds this to the reports
- A new feature that finds all unique spaces used at any point in the wiring and lists all of these out in the reports
- The entities and state variables that are impacted by mechanisms have now been added into the mermaid graphics

### Bug Fixes & Small Improvements

- Bug fix on control action report writing
- Now the arrows between blocks scale to the number of spaces being passed
- Any blocks which do not have an output space (meaning all mechanisms) are no longer linked to the codomain as it was getting too cluttered like that
- New sections added to the markdown reports + cleaning up of loose ends
- A whole bunch of updates to the JSON spec for:
    - Expanding it for places that were not defined including nested components
    - Adding descriptions for a whole lot of the components and subcomponents

### Documentation and Artifacts

- Everything except for the coffee shop example has been ported from HackMD to the github repository
- New functionality that can take the JSON spec descriptions and map them into a markdown table for easy display in READMEs or presentations
- Revisions to the V0.2.2 report from typos + broken links that I discovered after the presentation

## Future Research Arc

- The V0.4 roadmap is defined [here](https://github.com/BlockScience/MSML/blob/main/research_notes/2024-03-31%20V0.4%20Roadmap.md)