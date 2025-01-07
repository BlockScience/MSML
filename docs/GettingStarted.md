---
title: Getting Started
nav_order: 2
layout: page
---

Getting started with your first MSML specification can seem like a daunting task but this short guide will hopefully make it easier.

## 1. Review the Concepts

- Within this documentation, you can find specific technical documentation including the background theory and the components under "Technical Documentation"
- Feel free to go as deep into it as you feel necessary; if you prefer just jumping straight in you can move on to step 2 or step 3

## 2. Review Canonical Examples & Tutorials

- Within this documentation, you can find a section "Canonical Examples" which has links to examples and tutorials on how to use MSML
- The MSML template is the easiest to grasp and also is what is forked to start a new MSML specification so it is recommended above all the others to first review

## 3. Fork the MSML Template

- The [MSML Template](https://github.com/BlockScience/MSML-Template) can be forked by pushing the green button labeled "Use this template"
- The template comes with starter "DUMMY" components to show the format of a repository

## 4. Write New Components

- The core functionality for MSML is writing new components without code attatched, the recommended flow is to add components and then every time restart the kernel and run the "Build Obsidian.ipynb" notebook
    - This notebook will flag any errors that might have been introduced
    - If there are no errors, the Obsidian vault will be updated with your components which you can look through
    - You **must** restart the python kernel each time to make sure that the notebook pulls the latest components in
- To add a component, go into the src folder and then locate the sub-folder which is the new component you are adding first
    - For example, if it is spaces, go into the "Spaces" folder
- To add a new component to a file already existing, go into that file, such as "Dummy.py", the code in this file of the template looks like:

```python
dummy_abcedf_space = {
    "name": "DUMMY ABCDEF Space",
    "schema": {
        "string": "DUMMY ABCDEF Type",
    },
}


dummy_string_length_space = {
    "name": "DUMMY String Length Space",
    "schema": {
        "string": "DUMMY ABCDEF Type",
        "length": "DUMMY Integer Type",
        "unique_length": "DUMMY Integer Type",
    },
}

dummy_spaces = [dummy_abcedf_space, dummy_string_length_space]
```
- Add in a new component with the same schema, and then add that to "dummy_spaces" list
- It is recommended to add separate files for sets of components such as "User.py" for spaces that are related to users and eventually delete "Dummy.py" in favor of specifically named files
- When adding a new file, make sure to update the "\_\_init\_\_.py" file, which looks like:

```python
from .Dummy import dummy_spaces

spaces = []
spaces.extend(dummy_spaces)
```

- You would import something like user_spaces from .User and then add "spaces.extend(user_spaces)" to make sure the new spaces are integrated in
- After adding a new component, kernel restart and re-run the Obsidian creation notebook and make sure it runs successfully