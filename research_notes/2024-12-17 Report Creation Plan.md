# Report Creation Plan

## Executive Summary

- The report plan below details the current and desired future state of reporting in MSML
- Feedback from users is encouraged as all plans are only loosely defined and meant to potentially be changed to be more useful

## Current Reporting Architecture

- There are a handful of files such as mechanisms.py, policies.py, etc. that have mostly depcreated functions from the HTML writer version.
- All of the main abilities are housed in the markdown.py file that has each markdown file type broken down as functions, for example one for mechanisms, one for policies, etc.
- All the writer functions create markdown files which when opened in Obsidian create a nicely linked documentation system.

## Desired Future Reporting Architecture

- [Switching to atomized functions](https://github.com/BlockScience/MSML/issues/165) will help to improve the ongoing maintenance of code
- There is an aim to have a "plug and play" feel to the reporting modules that allow for flexibility and choosing exactly how you want reports
    - Creating [style dictionaries](https://github.com/BlockScience/MSML/issues/251) is one way that reports can become flexible
- There will be a desire to have multiple output avenues
    - Standard markdown
    - Markdown with wikilinks for use in Obsidian
    - [PDFs of markdown](https://github.com/BlockScience/MSML/issues/600)
- I want to also [create a mermaid graph](https://github.com/BlockScience/MSML/issues/601) or similar of the reporting architecture for both developer documentation as well as organizing thoughts on the best way to structure the codebase

## Outputs

1. Obsidian vault of markdown files (currently implemented)
2. [Individual markdown reports](https://github.com/BlockScience/MSML/issues/602) of components based on style dictionary (for things such as how deep to go in terms of just saying what domain is versus actually listing out the domain objects such as {"name": "Space 1", "schema": {....}} for giving stakeholders the entire picture)
    - And the option to PDF it
3. [Specialized reports](https://github.com/BlockScience/MSML/issues/603) such as the parameter effects style whereby you can see every single block that is impacted downstream by parameters
4. Potential for future engine extensions to support things such as stock & flow diagrams (although it can be shifted in terms of the priority)

## Issue Log

- The table below are all the open issues that can be prioritized in the upcoming milestones
- I will plan to begin moving the issues to broad milestones such as V0.5, V0.6, V0.7, etc. to give rough estimates of when things will be implemented
- There are quite a few improvement style issues which are good to also consider such as whether or not it is important that a user can add metrics and stateful metrics to the mermaid graphs

|                 | Reporting                                                                                                                                                                 |
|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| High Priority   | [Create plan for specialized reports](https://github.com/BlockScience/MSML/issues/603)                                                                                    |
|                 | [Create plan for individual markdown reports](https://github.com/BlockScience/MSML/issues/602)                                                                            |
|                 | [Create a mermaid graph or similar of the reporting architecture](https://github.com/BlockScience/MSML/issues/601)                                                        |
|                 | [Revive PDF Writing Abilities for Reporting](https://github.com/BlockScience/MSML/issues/600)                                                                             |
|                 | [Add something for displaying source code for wiring](https://github.com/BlockScience/MSML/issues/570)                                                                    |
|                 | [For policies/mechanisms/etc add in a section for markdown reporting that says wirings that it is involved in](https://github.com/BlockScience/MSML/issues/258)           |
|                 | [Switch legacy reporting to be using mermaid + markdown](https://github.com/BlockScience/MSML/issues/155)                                                                 |
|                 | [Add Table comparing policy options, boundary options, etc](https://github.com/BlockScience/MSML/issues/148)                                                              |
| Medium Priority | [Obsidian Canvas Creator for Wirings](https://github.com/BlockScience/MSML/issues/541)                                                                                    |
|                 | [Add Metrics and Stateful Metrics used to Mermaid Charts](https://github.com/BlockScience/MSML/issues/540)                                                                |
|                 | [Stock and Flow generator](https://github.com/BlockScience/MSML/issues/498)                                                                                               |
|                 | [Idea: Auto-displays](https://github.com/BlockScience/MSML/issues/280)                                                                                                    |
|                 | [Convert action chain report to markdown](https://github.com/BlockScience/MSML/issues/254)                                                                                |
|                 | [Convert entity report to markdown](https://github.com/BlockScience/MSML/issues/253)                                                                                      |
|                 | [Make write basic report markdown](https://github.com/BlockScience/MSML/issues/252)                                                                                       |
|                 | [Atomize Writing Functions](https://github.com/BlockScience/MSML/issues/165)                                                                                              |
|                 | [Add Policy Report](https://github.com/BlockScience/MSML/issues/159)                                                                                                      |
|                 | [Add parameters impacting to policy, behaviors, etc. in report write out](https://github.com/BlockScience/MSML/issues/89)                                                 |
|                 | [Make a type of report that is a parameter report](https://github.com/BlockScience/MSML/issues/74)                                                                        |
|                 | [Replicate Something like write_full_state_section from the alpha version](https://github.com/BlockScience/MSML/issues/58)                                                |
| Low Priority    | [Add obsidian plugins to starter repos and have a function that also can populate them](https://github.com/BlockScience/MSML/issues/387)                                  |
|                 | [Add ability to de-emphasize certain wirings by marking them with a flag that puts their reports into an "extra" wiring](https://github.com/BlockScience/MSML/issues/381) |
|                 | [Figure out how to force CSS snippets used](https://github.com/BlockScience/MSML/issues/322)                                                                              |
|                 | [Idea: Top level tag for wirings](https://github.com/BlockScience/MSML/issues/281)                                                                                        |
|                 | [Add images assets functionality](https://github.com/BlockScience/MSML/issues/260)                                                                                        |
|                 | [Mermaid graph assets functionality](https://github.com/BlockScience/MSML/issues/259)                                                                                     |
|                 | [Style Dictionary options](https://github.com/BlockScience/MSML/issues/251)                                                                                               |
|                 | [Consider a format dictionary for MSML that allows you to override certain formatting options](https://github.com/BlockScience/MSML/issues/246)                           |
|                 | [Add metric linkages to the reporting for components](https://github.com/BlockScience/MSML/issues/233)                                                                    |
|                 | [Metric report](https://github.com/BlockScience/MSML/issues/231)                                                                                                          |
|                 | [Exclude Dictionary Feature](https://github.com/BlockScience/MSML/issues/79)                                                                                              |
|                 | [Add Parameters to Graph Option](https://github.com/BlockScience/MSML/issues/53)                                                                                          |

## Oustanding Questions

1. How urgent is the style dictionary kind of customizability to people?
2. Are there any other formats besides markdown and PDF that people are interested in having?
3. What other kinds of reports would be desired?
4. Are there any improvements to the current reporting that would be nice?

## An Aside on Stock & Flow
- I think stock & flow would add even more requirements on the JSON spec to have things such as a field for state variables used in the block
- This, however, could also be kept as an optional field
- And if code is bound to the component, then there might even be automation to actually read that data in automatically or create a specialized function for imputing it when you are feeling lazy but have the code bindings defined out already
- It seems like a quite often used chart so I am curious to hear if others believe it is worth it to invest the time into this as it would also be a somewhat decent lift
