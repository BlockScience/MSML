# Report Creation Plan

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

- Putting together the issues of reporting from github
- Potentially can begin sorting them into larger milestones such as V0.5, V0.6, etc

## Oustanding Questions

1. How urgent is the style dictionary kind of customizability to people?
2. Are there any other formats besides markdown and PDF that people are interested in having?
3. What other kinds of reports would be desired?

## An Aside on Stock & Flow
- I think stock & flow would add even more requirements on the JSON spec to have things such as a field for state variables used in the block
- This, however, could also be kept as an optional field
- And if code is bound to the component, then there might even be automation to actually read that data in automatically or create a specialized function for imputing it when you are feeling lazy but have the code bindings defined out already
- It seems like a quite often used chart so I am curious to hear if others believe it is worth it to invest the time into this as it would also be a somewhat decent lift