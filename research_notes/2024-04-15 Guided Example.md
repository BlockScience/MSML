# Executive Summary

This research note shows how to start building out a first mathematical specification with the MSML library. This research note will walk through a guide example with the following format:

1. Introduce the MSML
2. Introduce the Problem Statement
3. Iteratively Explain Components with Worked Examples

## What is the Mathematical Specification Mapping Library (MSML)?

MSML is a library for standardizing the creation of mathematical specifications as JSON objects as well as aiding in the automation of report and visualization creation from these standardized JSON. 

It uses block diagram wirings and spaces to represent the actions in complex systems in line with current BlockScience research on Generalized Dynamical Systems. It also adds some enhancements to the primitive blocks to represent richer sets of behaviors.

One good example is the [wiring report](https://github.com/SeanMcOwen/Root-Finding-Simulation/blob/main/MSML/reports/Simulation%20Block.md) for the Root Finding Simulation canonical example.

### Installing the library

To install the library, simply pip install by running "pip install math_spec_mapping"

### Why MSML?

Writing mathematical specifications can be a difficult process, especially when variable names are changed or new mechanisms are introduced. MSML seeks to streamline the process with automations as well as enhance the abilities of static math specs to deliver deeper insights. Because it is automated, one can write specifications at different levels of details or for different purposes.


### What are some of the solutions offered?

- **Automation**: Automate writing of a specification
- **Standardization**: Ensure standardization across teams working to spec out a system
- **Flexibility**: Allow for creating views on the fly and in multiple ways depending on what stakeholders find important
- **Trackability**: Keep a repository of a JSON file to track changes to the spec with the same enhancements git provides for projects already

### How does MSML work?


```mermaid
graph TD
A[JSON Object \n\n Each spec has a repo for tracking changes \n Must conform to the json specification \n Defines all aspects of the spec including blocks, spaces and actions] -->B[MSML Object \n\n JSON file is parsed, with validations and mappings along the way \n Can show different views on the fly]
    B --> C[Report Outputs \n\n Automatically build reports for the full spec or subviews \n Example: all blocks with an effect on variable XYZ]

```

### Generalized Dynamical Systems Basics

For more information with regards to the GDS fundamentals, one can look at this [repository](https://github.com/BlockScience/GDS-MSML-cadCAD). Below is abbreviated documentation describing the fundamentals of Generalized Dynamical Systems (GDS).

#### Blocks

A Block is a parameterized operation that, for each Point in its Parameters Space, maps a Point in an input Space to a unique point in an output Space.	

Basic blocks are characterized by three things:

**Domain**: The space(s) that are taken in for the function

**Codomain**: The space(s) that are emitted out from the function

**Logic**: The logic that describes the transformation from domain to codomain

#### Spaces

A space is a pointer to a collection of dimensions.	For example we might have a space such as cartesian coordinates with the schema {"x": float, "y": float}. Spaces are passed between domains and codomains of blocks.

#### Wiring

A wiring is a block composed of other blocks with specific behaviors or orders of execution. For instance, there can be wirings that have blocks run one after another, passing their codomains to the next block's domain. There can also be wirings for blocks that all should run in parallel.

### MSML Components

MSML extends GDS with multiple types of blocks and other enhancements. Below are the definitions of top level components.

#### Types & Spaces

- **Type**: This is for defining what a type might in its most basic form. These could be single typings or compound typings. The point here is to allow for changing typing in one single place and having it flow through anywhere else. I.e. if one were to define the currency type as USD, but then the project switched to using EUR, it would just require changing currency to be EUR.
- **Space**: Spaces are similar to types in that they define a schema for data and are used as the domain/codomain for different blocks. They can be thought of as typed dictionaries.

#### Entities, States, Parameters & Metrics

- **Entity**: Entities are any class of user or infrastructure that should have their own state and potentially ability to call boundary actions. Examples could be a customer or a company (for which a simulation might assume it is acting as one cohesive unit)
- **State**: The definition of states in the system. There is one global system state and then the rest of the definitions are local states, generally for recording what entity states there are.
- **Stateful Metric**: Variables that are not held directly in the state but can computed from the state & parameters.
- **Parameter**: Both local and global parameter sets in the system that could be set
- **Metric**: This component takes a variety of potential inputs and creates a metric from it. This can be used for defining out system success metrics or trying to modularize certain calculations that are needed across many other system components.

#### Blocks & Wiring

- **Boundary Action**: The definition of different actions that might happen outside of the system such as customers coming into a shop. Generally will be called by entities.
- **Control Action**: The definition of actions that the system might call, such as an action to refill the stock of an item when reserves run too low or something that could get triggered from a sensor. The key differentiator from boundary actions is that there is no entity calling it and it is not done with randomness.
- **Policy**: A definition of the policies that handle all logical things. This could be, for example, a policy which determines what price is paid given a boundary action of someone putting in a market buy order for a stock.
- **Mechanism**: Anything that updates state in the system, usually policies will call these with the outputs of logic. The reasoning to split them out is so that if at some point you want to add a recording variable every time an account is changed or do something like have a variable listener, you can just change the mechanism responsible for it in only one place.
- **Wiring**: A wiring is a block composed of other blocks with specific behaviors or orders of execution. For instance, there can be wirings that have blocks run one after another, passing their codomains to the next block's domain. There can also be wirings for blocks that all should run in parallel.

## Problem Statement

For this guided example, the following is the problem statement from which we will build the specification.

Investing for retirement is often modeled with monte carlo simulations because of how much path dependence there is. The following are the specific facts of the problem:
- There is only one person of interest in the model, the employee looking to retire.
- They only have control over the allocation percentages at any given time between bonds and stocks. This percentage will over time change, however, based on how the prices of the assets change!
- Any time a trade is conducted, we can assume no comissions or fees, although the model could be enriched by adding this.
- The returns of both stocks and bonds are assumed to be randomly distributed (although this could of course be extended to get more accurate measures), and can be parameterized by $\mu_s$, $\sigma_s$, $\mu_b$ and $\sigma_b$.


## Getting Started with a Base Directory

- We can begin by forking the [starter repo](https://github.com/BlockScience/MSML/tree/main/examples/StarterRepo) into a directory and removing the "model" folder since we are just doing a spec today.
- We will also clear out the reports folder to start fresh.

### The Initialization File

- The \_\_init\_\_.py is the entrypoint for all of components of our spec. You will note that in the example set up, each folder brings in a set of components to the spec json.

![init](init.png)

### Component Definitions

- If we dive deeper into the repository, we see that there are component definitions in the folders which just requires that there is a list with all components to be added.
- The following is what the policy definitions look like for the dummy repo in terms of the \_\_init\_\_.py file as well as the specific definitions (more on definition specifics later).

![policy_example](policy_example.png)

### Test Run on Functionality

- Before we begin to make any changes, we need to first make sure functionality works. We will take the "Build Starter Repo.ipynb" notebook and use it to make sure.
- We will update the code to be:
<pre><code>"""# For the production library
from math_spec_mapping import (load_from_json, write_all_markdown_reports, write_spec_tree)"""

# Development library loading
import sys
sys.path.append("/Users/seanmcowen/Dropbox/BlockScience")
from MSML.src.math_spec_mapping import (load_from_json, write_all_markdown_reports, write_spec_tree)

from src import math_spec_json
from copy import deepcopy
ms = load_from_json(deepcopy(math_spec_json))

d = "reports/Markdown"
write_all_markdown_reports(ms, d, clear_folders=True)
write_spec_tree(ms, path=d, linking=True)</code></pre>
- If using the development library make sure to update the path to the MSML folder
- Make sure the you create the Markdown folder in the reports folder
- The notebook will look like this and be able to be run:

![notebook](notebook.png)
- The markdown folder can now be opened up in Obsidian and should look like the following:
![obsidian1](obsidian1.png)

### Updating the Spec

- We now are going to move into updating the spec, which we will do iteratively while going through each component and what it means
- The dummy components will be taken out at the very end because they can be very helpful for understanding how the format works

## Types

### Definitions

**Types**: This is for defining what a type might in its most basic form. These could be single typings or compound typings. The point here is to allow for changing typing in one single place and having it flow through anywhere else. I.e. if one were to define the currency type as USD, but then the project switched to using EUR, it would just require changing currency to be EUR.

### JSON Spec

The schema is defined [here](../docs/JSON-Specification/schema-definitions-type.md)

### Adding our First Types

- The first types we can infer from reading the problem statement is that we are going to have a USD type to denote dollar amounts, as well as two types for number of shares in bonds and number of shares in stocks. 
- What we want to do is create a file called "Investments.py" in the types folder which we will use to host these three new types.
- For now we will ignore what the "type" as it will be covered how MSML maps types into different programming languages in a later section.
- The following type definitions can be written into the python file to give us our first three types:

<pre><code>USDType = {"name": "USD Type", "type": "USDType", "notes": "A dollar amount"}
StockSharesType = {
    "name": "Stock Shares Type",
    "type": "StockSharesType",
    "notes": "The number of shares of stock. Note that in this current spec, it is assumed that fractional shares can be held.",
}
BondSharesType = {
    "name": "Bond Shares Type",
    "type": "BondSharesType",
    "notes": "The number of shares of bonds. Note that in this current spec, it is assumed that fractional shares can be held.",
}</code></pre>

- And the \_\_init\_\_.py file can be updated to be:

<pre><code>from .Dummy import DummyCompoundType, DummyType1, DummyType2
from .Investments import USDType, BondSharesType, StockSharesType

types = [
    DummyType1,
    DummyType2,
    DummyCompoundType,
    USDType,
    BondSharesType,
    StockSharesType,
]</code></pre>

## Entities & State

### Definitions

- **Entity**: Entities are any class of user or infrastructure that should have their own state and potentially ability to call boundary actions. Examples could be a customer or a company (for which a simulation might assume it is acting as one cohesive unit)
- **State**: The definition of states in the system. There is one global system state and then the rest of the definitions are local states, generally for recording what entity states there are.

### JSON Spec

The specific schemas for entities and states are defined here:

- [Entity](../docs/JSON-Specification/schema-definitions-entity.md)
- [State](../docs/JSON-Specification/schema-definitions-state.md)

### Adding Entity & State

- Our first starting point will be to define out what entities we have in our system.
- We have the global entity which we will not modify right now but represents the global system and has the associated global state
- Besides the global state, we can see from the problem statement that there should be a Person entity representing the person who is saving for retirement.
- To add the person entity, we define out the following in a new file we will name "Person.py" in the Entities folder.
<pre><code>person_entity = {
    "name": "Person",
    "notes": "A person who is trying to save up for retirement in the simulation.",
    "state": "Person State",
}</code></pre>
- Then modify the \_\_init\_\_.py in the entities folder like so:

<pre><code>from .Dummy import dummy_entity
from .Global import global_entity
from .Person import person_entity

entities = [dummy_entity, global_entity, person_entity]</code></pre>
- This could would fail if we ran it right away because it is missing the "Person State" referenced.
- We create the "Person.py" file in the State folder to define out our state for the person as follows below:
<pre><code>person_state = {
    "name": "Person State",
    "notes": "A person's state in the simulation",
    "variables": [
        {
            "type": "Bond Shares Type",
            "name": "Bond Shares",
            "description": "The number of shares of bonds that a person has.",
            "symbol": "$S_{B}$",
            "domain": "$\mathbb{R}_{>=0}$",
        },
        {
            "type": "Stock Shares Type",
            "name": "Stock Shares",
            "description": "The number of shares of stock that a person has.",
            "symbol": "$S_{S}$",
            "domain": "$\mathbb{R}_{>=0}$",
        },
    ],
}</code></pre>
- The \_\_init\_\_.py also gets updated but we will no longer show the code updates since they are relatively straightforward imports.
- You will notice that for the domain and symbol latex is used. This gets rendered nicely in markdown and can be seen below.

![markdown](markdown.png)



## Boundary Action & First Space

- We have defined out some very basic pieces of the spec, and now we can begin to think through the problem statement and what it would mean for a person to change their allocation.
- The first thing to think about in regards to this boundary action, is what space should be coming out of it.
    - We know that the investment allocation is supposed to be in terms of percentage of stocks vs. bonds, so we want to define our space out like that.
    - We can think of the spaces as having a component for each (technically only one is needed, and 1 - that value equals the other, but we will show it with both and using constraints to ensure they add up to 100%)
- Before we can write the space out, we need to define how we show the percentages. Some people might prefer to use a percentage, i.e. 60% or 60 corresponds to 60%, while others may prefer to use decimals, i.e. .60 means 60%. We will add a new type called "Decimal Type" to denote that we are using decimals in this simulation.
- The following is added to the "Investments.py" file in the Types folder:
<pre><code>DecimalType = {
    "name": "Decimal Type",
    "type": "DecimalType",
    "notes": "The type which denotes a percentage as a decimal, i.e. .60 means 60%.",
}</code></pre>
- Now that we have defined out this new type that we needed to add, we move on to the spaces and boundary actions.

### Definitions

- **Space**: Spaces are similar to types in that they define a schema for data and are used as the domain/codomain for different blocks. They can be thought of as typed dictionaries.
- **Boundary Action**: The definition of different actions that might happen outside of the system such as customers coming into a shop. Generally will be called by entities.

### JSON Spec

The specific schemas for entities and states are defined here:

- [Space](../docs/JSON-Specification/schema-definitions-space.md)
- [Boundary Action](../docs/JSON-Specification/schema-definitions-boundary-action.md)

### Adding the Percentage Allocation Space
- Our first space will be called the percentage allocation space and will be used to denote the space that our boundary action will output.
- We add "Investments.py" to the Spaces folder and the following defines out what our space should look like:
<pre><code>investment_allocation_percentage_space = {
    "name": "Investment Allocation Percentage Space",
    "schema": {
        "percentage_bonds": "Decimal Type",
        "percentage_stocks": "Decimal Type",
    },
}


investment_spaces = [investment_allocation_percentage_space]</code></pre>
- Notice the schema defines out the two variables that are part of the space which are meant to denote the allocation choices of the person.

### Adding the Investment Allocation Boundary Action

- This boundary action should represent a user sending an updated allocation decision.
- We will add in a constraint that the codomain space must sum to 1, meaning 100%.
- This allocation decision is called by the Person entity.
- No parameters are used.
- The codomain will be the newly defined "Investment Allocation Space"
- We won't define out the boundary action options yet
- The following code defines out, in "Investment.py" within the BoundaryActions folder, what the boundary action should be.
<pre><code>portfolio_allocation_boundary_action = {
    "name": "Portfolio Allocation Boundary Action",
    "description": "The boundary action for a user looking to rebalance their portfolio.",
    "constraints": [
        "CODOMAIN[0].percentage_bonds + CODOMAIN[0].percentage_stocks == 1"
    ],
    "boundary_action_options": [],
    "called_by": ["Person"],
    "codomain": [
        "Investment Allocation Percentage Space",
    ],
    "parameters_used": [],
}</code></pre>

### Adding a Boundary Action Option

- The boundary action options are meant to represent actual implementations of a boundary action that we might see in the simulation.
- We will define one and update our code to include a boundary action option where the user always balances to a 60% stock/40% bond portfolio.
- The code is updated like so:
<pre><code>portfolio_allocation_boundary_action_option1 = {
    "name": "60/40 Portfolio",
    "description": "An option where the person always rebalances to a target allocation of 60/40 stocks/bonds.",
    "logic": "Return a codomain of {'percentage_bonds': .4, 'percentage_stocks': .6}",
}

portfolio_allocation_boundary_action = {
    "name": "Portfolio Allocation Boundary Action",
    "description": "The boundary action for a user looking to rebalance their portfolio.",
    "constraints": [
        "CODOMAIN[0].percentage_bonds + CODOMAIN[0].percentage_stocks == 1"
    ],
    "boundary_action_options": [portfolio_allocation_boundary_action_option1],
    "called_by": ["Person"],
    "codomain": [
        "Investment Allocation Percentage Space",
    ],
    "parameters_used": [],
}</code></pre>

This then allows us to create this nice boundary action markdown file automatically:

![boundary_action](boundary_action.png)

## Portfolio Allocation Policy

- What would come after this boundary action is a policy which converts the percentages to the correct number of shares.
- The output being the correct number of shares tells us that we need to first create a new space to represent the output of the policy.
- We also will realize when going through this process that our global state needs two new variables, one for the stock price and one for the bond price.

### Investment Allocation Space

- We update "Investments.py" in the Spaces folder to be the following:
<pre><code>investment_allocation_percentage_space = {
    "name": "Investment Allocation Percentage Space",
    "schema": {
        "percentage_bonds": "Decimal Type",
        "percentage_stocks": "Decimal Type",
    },
}

investment_allocation_space = {
    "name": "Investment Allocation Space",
    "schema": {
        "bond_shares": "Bond Shares Type",
        "stock_shares": "Stock Shares Type",
    },
}


investment_spaces = [
    investment_allocation_percentage_space,
    investment_allocation_space,
]</code></pre>
- With our newly created space we are ready to define out the portfolio allocation policy

### Global State Update

- The global state gets updated like so to add in the price of bonds and stocks
<pre><code>global_state = {
    "name": "Global State",
    "notes": "",
    "variables": [
        {
            "type": "USD Type",
            "name": "Bond Price",
            "description": "The current price of the bond (per share).",
            "symbol": "$P_{B}$",
            "domain": "$\mathbb{R}_{>=0}$",
        },
        {
            "type": "USD Type",
            "name": "Stock Price",
            "description": "The current price of the stock (per share).",
            "symbol": "$P_{S}$",
            "domain": "$\mathbb{R}_{>=0}$",
        },
    ],
}</code></pre>

### Definitions

**Policy**: A definition of the policies that handle all logical things. This could be, for example, a policy which determines what price is paid given a boundary action of someone putting in a market buy order for a stock.

### JSON Spec

The schema is defined [here](../docs/JSON-Specification/schema-definitions-policy.md)

### Creating the Portfolio Allocation Policy
- This time we will create the policy option at the same time as the policy. Similar to boundary actions it is what represents possible specific implementations.
- Notice the domain and codomain are different here
- There is a reference to "portfolio_value" which is a stateful metric to be defined next, for now just take it as the total value of our portfolio at the given time.
- The code is as follows:
<pre><code>portfolio_allocation_policy_option1 = {
    "name": "Portfolio Allocation Policy V1",
    "description": "Simple policy to convert percentages to shares",
    "logic": """1. Grab the portfolio_value metric at the current time.
2. Define stock_shares as the portfolio_value * DOMAIN[0].percentage_stocks / STATE["Global"].stock_price
3. Define bond_shares as the portfolio_value * DOMAIN[0].percentage_bonds / STATE["Global"].bond_price
4. Return a space of {"bond_shares": bond_shares, "stock_shares": stock_shares}""",
}

portfolio_allocation_policy = {
    "name": "Portfolio Allocation Policy",
    "description": "The policy which maps a percentage allocation to a shares allocation.",
    "constraints": ["DOMAIN[0].percentage_bonds + DOMAIN[0].percentage_stocks == 1"],
    "policy_options": [portfolio_allocation_policy_option1],
    "domain": [
        "Investment Allocation Percentage Space",
    ],
    "codomain": [
        "Investment Allocation Space",
    ],
    "parameters_used": [],
    "metrics_used": [],
}

investment_policies = [portfolio_allocation_policy]</code></pre>
- And our outputted policy component in markdown looks like:
![policy](policy.png)

## Portfolio Value Stateful Metric

- We will add in a stateful metric now to represent the total portfolio value at a given time.

**Stateful Metric**: Variables that are not held directly in the state but can computed from the state & parameters.

### JSON Spec

The schema is defined [here](../docs/JSON-Specification/schema-definitions-stateful-metric.md)

### Adding the Portfolio Value Stateful Metric

- We create an "Investments.py" file in the StatefulMetrics folder and use it to craft our set of investment stateful metrics.
- Notice that we define metrics in sets, so we create the "Investment Stateful Metrics" set
- We also can denote that variables used with tuples where the first element is the state and the second element is the state variable.
- The definition of the stateful metric is done like this:
<pre><code>investment_stateful_metric = {
    "name": "Investment Stateful Metrics",
    "notes": "Stateful metrics related to investments",
    "metrics": [
        {
            "type": "USD Type",
            "name": "portfolio_value",
            "description": "The total portfolio value as measured by the shares a person has times their prices, and then summed.",
            "variables_used": [
                ("Global State", "Stock Price"),
                ("Global State", "Bond Price"),
                ("Person State", "Stock Shares"),
                ("Person State", "Bond Shares"),
            ],
            "parameters_used": [],
            "symbol": "$V$",
            "domain": "$\mathbb{R}_{>=0}$",
        }
    ],
}

investment_stateful_metric_sets = [investment_stateful_metric]</code></pre>

## Update Shares Mechanism

- The last piece of the puzzle for updating the allocation is a mechanism which updates the shares for the user. We will define this below.

### Definitions

**Mechanism**: Anything that updates state in the system, usually policies will call these with the outputs of logic. The reasoning to split them out is so that if at some point you want to add a recording variable every time an account is changed or do something like have a variable listener, you can just change the mechanism responsible for it in only one place.

### JSON Spec

The schema is defined [here](../docs/JSON-Specification/schema-definitions-mechanism.md)

### Creating the Update Shares Mechanism

- The implementation is fairly straight-forward, except that it is important to explain the schema for the updates attribute.
    - The format is (Entity Name, Variable Name, Boolean for whether or not it is optional)
- We create "Investments.py" in the Mechanisms folder and add the following:
<pre><code>update_shares_mechanism = {
    "name": "Update Shares Mechanism",
    "description": "The mechanism which updates the amount of shares that a person has",
    "constraints": [],
    "logic": "The values from the domain space are mapped into the person's state",
    "domain": [
        "Investment Allocation Space",
    ],
    "parameters_used": [],
    "updates": [("Person", "Stock Shares", False), ("Person", "Bond Shares", False)],
}

investment_mechanisms = [update_shares_mechanism]</code></pre>

## Portfolio Allocation Wiring

- Now we get to tie it all together! We are creating a wiring which will illustrate the flow of the portfolio allocation process.

### Definitions

**Wiring**: A wiring is a block composed of other blocks with specific behaviors or orders of execution. For instance, there can be wirings that have blocks run one after another, passing their codomains to the next block's domain. There can also be wirings for blocks that all should run in parallel.

### JSON Spec

The schema is defined [here](../docs/JSON-Specification/schema-definitions-wiring.md)

### Creating the Portfolio Allocation Wiring
- The component order matters here, and we are going to put the three previously defined components
- The MSML library does checking on spaces to ensure that domains and codomains match up
- In this case we use the type of "Stack" because the blocks are each running one after another, passing their spaces
- The implementation in the newly created "Investments.py" file in the Wiring folder is:
<pre><code>investments_wiring = []

investments_wiring.append(
    {
        "name": "Portfolio Allocation Wiring",
        "components": [
            "Portfolio Allocation Boundary Action",
            "Portfolio Allocation Policy",
            "Update Shares Mechanism",
        ],
        "description": "This wiring takes care of all logic around a person updating their portfolio allocation",
        "constraints": [],
        "type": "Stack",
    }
)</code></pre>

And this is how the markdown component looks:

![wiring1](wiring1.png)
![wiring2](wiring2.png)

## Advance Time Control Action

- We use control actions for those actions that might trigger behaviors but are not related to a specific entity
- In our case, we will make a control action that is meant to represent a certain amount of time being advanced
- Before we begin there are two things we need to add, a type for number of years and then a space for the time advance.

### Adding the new Type and Space

- For the year type, we add in "TimeProgression.py" to Types with the following simple type definition:
<pre><code>YearsType = {"name": "Years Type", "type": "YearType", "notes": "A number of years"}</code></pre>
- Then we can add in "TimeProgression.py" to the spaces folder with the following definition to represent a space that says some number or fraction of years passed.
<pre><code>advance_time_space = {
    "name": "Advance Time Space",
    "schema": {
        "delta_years": "Years Type",
    },
}


time_progression_spaces = [advance_time_space]</code></pre>

### Definitions

**Control Action**: The definition of actions that the system might call, such as an action to refill the stock of an item when reserves run too low or something that could get triggered from a sensor. The key differentiator from boundary actions is that there is no entity calling it and it is not done with randomness.

### JSON Spec

The schema is defined [here](../docs/JSON-Specification/schema-definitions-controlaction.md)

### Creating the Advance Time Control Action

We build the "TimeProgression.py" file in the ControlActions folder with this code:

<pre><code>advance_time_control_action_option1 = {
    "name": "Quarter Time Progression",
    "description": "Control action option which simply pushes time forward by a quarter.",
    "logic": "Return a codomain space of {'time_delta': .25}",
}

advance_time_control_action = {
    "name": "Advance Time Control Action",
    "description": "The control action which pushes forward the simulation time",
    "constraints": [],
    "control_action_options": [advance_time_control_action_option1],
    "codomain": [
        "Advance Time Space",
    ],
    "parameters_used": [],
}</code></pre>

## Parameters & Advance Time Policy
- One thing we will need before creating this policy is a new space for transmitting the new prices of the bond and stock, defined below

### Definitions

**Parameter**: Both local and global parameter sets in the system that could be set

### JSON Spec

The schema is defined [here](../docs/JSON-Specification/schema-definitions-parameter.md)


### Asset Prices Space
- Updating the "TimeProgression.py" file in the spaces folder:
<pre><code>advance_time_space = {
    "name": "Advance Time Space",
    "schema": {
        "delta_years": "Years Type",
    },
}

asset_prices_space = {
    "name": "Asset Prices Space",
    "schema": {
        "stock_price": "USD Type",
        "bond_price": "USD Type",
    },
}


time_progression_spaces = [advance_time_space, asset_prices_space]
</code></pre>

### Parameters

- We define out the parameters below in "TimeAdvancement.py" within the Parameters folder.
- All the parameters are of the behavioral type because they have to do with behaviors of the system
<pre><code>time_advancement_parameter_set = {
    "name": "Time Advancement Parameter Set",
    "notes": "",
    "parameters": [
        {
            "variable_type": "Decimal Type",
            "name": "stock_return_mu",
            "description": "The average yearly return of stocks",
            "symbol": "$r_s$",
            "domain": "$\mathbb{R}$",
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Decimal Type",
            "name": "stock_return_std",
            "description": "The average yearly standard deviation of stock returns",
            "symbol": "$\sigma_s$",
            "domain": "$\mathbb{R}$",
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Decimal Type",
            "name": "bond_return_mu",
            "description": "The average yearly return of bonds",
            "symbol": "$r_b$",
            "domain": "$\mathbb{R}$",
            "parameter_class": "Behavioral",
        },
        {
            "variable_type": "Decimal Type",
            "name": "bond_return_std",
            "description": "The average yearly standard deviation of bond returns",
            "symbol": "$\sigma_b$",
            "domain": "$\mathbb{R}$",
            "parameter_class": "Behavioral",
        },
    ],
}


time_advancement_parameter_set = [time_advancement_parameter_set]
</code></pre>

### Implementing the Advance Time Policy

- For this policy we have two spaces from the codomain, this is because we are going to be calling one mechanism for updating the time and another for updating the asset prices.
- We are using the parameters feature for the first time here too!
<pre><code>advance_time_policy_option1 = {
    "name": "Advance Time Policy V1",
    "description": "Simple policy to advance time and use the normal distribution for price movements.",
    "logic": """1. Take the current stock price and multiply it by (1+NORMAL_RANDOM(PARAMS["stock_return_mu"], PARAMS["stock_return_std"])) ** (DOMAIN["delta_time"]), define it as new_stock_price
2. Take the current bond price and multiply it by (1+NORMAL_RANDOM(PARAMS["bond_return_mu"], PARAMS["bond_return_std"])) ** (DOMAIN["delta_time"]), define it as new_bond_price
3. Return (DOMAIN[0], {
        "stock_price": new_stock_price,
        "bond_price": new_bond_price,
    })""",
}

advance_time_policy = {
    "name": "Advance Time Policy",
    "description": "The policy which pushes forward time and determines any changes in asset prices.",
    "constraints": [],
    "policy_options": [advance_time_policy_option1],
    "domain": [
        "Advance Time Space",
    ],
    "codomain": ["Advance Time Space", "Asset Prices Space"],
    "parameters_used": [
        "stock_return_mu",
        "stock_return_std",
        "bond_return_mu",
        "bond_return_std",
    ],
    "metrics_used": [],
}

time_progression_policies = [advance_time_policy]
</code></pre>

## New Mechanisms

- We define out the two mechanisms that get called after the latest policy, one for updating the time and one for updating the asset prices
- We also need to add in a state variable for the time in the system to global state.

### Global State Update

<pre><code>global_state = {
    "name": "Global State",
    "notes": "",
    "variables": [
        {
            "type": "USD Type",
            "name": "Bond Price",
            "description": "The current price of the bond (per share).",
            "symbol": "$P_{B}$",
            "domain": "$\mathbb{R}_{>=0}$",
        },
        {
            "type": "USD Type",
            "name": "Stock Price",
            "description": "The current price of the stock (per share).",
            "symbol": "$P_{S}$",
            "domain": "$\mathbb{R}_{>=0}$",
        },
        {
            "type": "Years Type",
            "name": "Time",
            "description": "The time in the system, in terms of the years passed",
            "symbol": "$t$",
            "domain": "$\mathbb{R}_{>=0}$",
        },
    ],
}</code></pre>

### Mechanism Definitions
- Defined in TimeAdvancement.py
<pre><code>update_asset_prices_mechanism = {
    "name": "Update Asset Prices Mechanism",
    "description": "The mechanism which updates the amount of shares that a person has",
    "constraints": [],
    "logic": "The values from the domain space are mapped into the global state variables of stock_price and bond_price",
    "domain": [
        "Asset Prices Space",
    ],
    "parameters_used": [],
    "updates": [
        ("Global", "Stock Price", False),
        ("Global", "Bond Price", False),
    ],
}

increment_time_mechanism = {
    "name": "Increment Time Mechanism",
    "description": "The mechanism which increments the time passed",
    "constraints": [],
    "logic": "The time attribute of the global state is incremented by DOMAIN[0].delta_time",
    "domain": [
        "Advance Time Space",
    ],
    "parameters_used": [],
    "updates": [
        ("Global", "Time", False),
    ],
}

time_advancement_mechanisms = [update_asset_prices_mechanism, increment_time_mechanism]</code></pre>



## Mechanisms Parallel Wiring

- We are going to demonstrate how to use a parallel block with the last two mechanisms we made
- This makes it so that their domains/codomains are concatonated together and they can be run as one large block where the inner blocks run at the same time
- In "TimeAdvancement.py" in the wiring folder, we write:
<pre><code>time_advancement_wiring = []

time_advancement_wiring.append(
    {
        "name": "Time Advancement Mechanisms Wiring",
        "components": [
            "Increment Time Mechanism",
            "Update Asset Prices Mechanism",
        ],
        "description": "This wiring takes care of the mechanisms from the time advancement wiring",
        "constraints": [],
        "type": "Parallel",
    }
)</code></pre>

And we can see the markdown file display of the new wiring we have added
![wiring3](wiring3.png)

## Time Advancement Wiring

- Now we bring together the control action, the policy, and the parallel mechanism wiring
- We actually have a wiring within a wiring now highlighting the idea of composability
- The code added:

<pre><code>time_advancement_wiring = []

time_advancement_wiring.append(
    {
        "name": "Time Advancement Mechanisms Wiring",
        "components": [
            "Increment Time Mechanism",
            "Update Asset Prices Mechanism",
        ],
        "description": "This wiring takes care of the mechanisms from the time advancement wiring",
        "constraints": [],
        "type": "Parallel",
    }
)

time_advancement_wiring.append(
    {
        "name": "Time Advancement Wiring",
        "components": [
            "Advance Time Control Action",
            "Advance Time Policy",
            "Time Advancement Mechanisms Wiring",
        ],
        "description": "This wiring takes care of time advancement",
        "constraints": [],
        "type": "Stack",
    }
)</code></pre>
- Which produces a wiring diagram like so:
![wiring4](wiring4.png)

## Conclusion

- Through this guided example we created one boundary action and one control action which served as the two actions that initiated wirings.
- Along the way, all the other components naturally fell into place as needed for finishing the spec.
- To create a model from this spec, one would need to decide on the frequency of the boundary and control actions firing. One example would be alternating between the two for some set number of iterations. I.e. a quarter of a year would pass, a rebalance would happen, repeat.