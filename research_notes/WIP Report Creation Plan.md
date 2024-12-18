# Report Creation Plan

## Current Reporting Architecture

- There are a handful of files such as mechanisms.py, policies.py, etc. that have mostly depcreated functions from the HTML writer version.
- All of the main abilities are housed in the markdown.py file that has each markdown file type broken down as functions, for example one for mechanisms, one for policies, etc.
- All the writer functions create markdown files which when opened in Obsidian create a nicely linked documentation system.

## Desired Future Reporting Architecture

- [Switching to atomized functions](https://github.com/BlockScience/MSML/issues/165) will help to improve the ongoing maintenance of code
- There is an aim to have a "plug and play" feel to the reporting modules that allow for flexibility and choosing exactly how you want reports
    - Creating [style dictionaries](https://github.com/BlockScience/MSML/issues/251) is one way that reports can become flexible
- Style dictionaries for determining
- Multiple output avenues including PDF
- Create a mermaid chart to visualize what the future architecure will look like

## Outputs

- Current and future outputs of the reporting modules
- Will be the primary goals for iteration

## Issue Log

- Putting together the issues of reporting from github
- Potentially can begin sorting them into larger milestones such as V0.5, V0.6, etc

## Oustanding Questions

1. How urgent is the style dictionary kind of customizability to people?