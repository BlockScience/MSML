# Parameter Class Naming Research Note

## Problem Statement

The MSML currently has the ability to add a parameter class attribute to parameters which describes the use of the parameter. These three, explained below, are behavioral, functional and system. The goals are to:

1. Align the vocabulary used so that is easily understood for most audiences
2. Define out any missing parameter classes
3. Figure out any changes to the functionalities listed

## Current MSML Method

The following are the three tags to be used:

### Behavioral

- These parameters would NOT be seen in a production system but instead denote any behavioral assumptions that would impact a simulation
- The purpose of segmenting them like this is easier views when working with the simulation and also an ability to filter them out if the MSML is being used for implementation of production software instead of a simulation
- An example would be parameters for the random return distribution for a given price

### System

- These are parameters that MUST be in a production system as they relate to certain system parameters set
- An example would be a parameter that denotes a fixed exchange rate between two assets (although if this exchange rate changes it is probably better put as a state variable)
- Another example might be something like maximum capacity of workers for a power plant, there might be a hard upper limit due to regulation and this would be put in to act as the boundary on a policy of adding more workers

### Functional

- These are parameters that impact the functional form in two ways:
    - Functional parameters that map which policy option or boundary action option is implemented in a simulation or production system
    - Possibly specific functions used such as what return distribution to use (by being a string representing normal distribution, normal distribution with a skew, etc.)
- These MAY OR MAY NOT be in a production system
- Part of the purpose is to extend modularity, if we have three implementations of a policy, the functional parameterization can allow for easy switching of the functions to be used in a simulation (or possibly production software)
- MSML has built in functions for the metaprogramming that allow for combining through all policies, boundary actions, and other components that contain "options" and creating the functional parameters for those which have more than one option, ensuring users know which functions are modifiable and need to be specified for specific implementations