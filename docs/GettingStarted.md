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

## 5. Bind Code to Components

- MSML has extended capabilities that allow for binding code to different components
- Go to the folder "src/Implementations/Python"
- For whichever components you want to define code for, move to that folder, for example "BoundaryActions.py"
- The "\_\_init\_\_" file looks like:

```python
from .Dummy import v1_dummy_boundary, v1_dummy_boundary2, v2_dummy_boundary2

boundary_action_options = {
    "Length-1 ABC Equal Weight Option": v1_dummy_boundary,
    "DUMMY Length-2 ABC Equal Weight Option": v1_dummy_boundary2,
    "DUMMY Length-2 ABC Equal Weight 2 Option": v2_dummy_boundary2,
}
```

- Each key here corresponds to the name of a boundary action option defined out in the specification, for any new boundary action options without functions you will simply add the key and a function representing it in the same format as the other functions (with three parameters of state, parameters and spaces)
- The only special cases are metrics and stateful metrics which have a slightly different set of arguments but are defined out the same way, by adding a key with the exact name of the metric/stateful metric
- Mechanisms also do not have options, so instead the key for these functions should be the mechanism name
- The "Implementation Playground.ipynb" can be used to test out the functions after creation
- Test cases can also be built up from these functions
- Wiring functionality is automatically created as long as every single component has a function definition (and if not a warning will be given when loading)
- You may need to update the base state and parameters to get the notebook running which is covered in the next section