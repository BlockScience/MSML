# Metrics Working Group 4/18/2024

## Executive Summary

The future of metrics in MSML has a few different paths that can be taken, and as such a call is being put together to discuss some of the finer points. The majority of these ideas and issues are subject to change if strong arguments are presented for or against something.

## The Possible Roles and Uses of Metrics in MSML and Beyond

Metrics can take on a few different functions depending on their context, making it important to distinguish the mandate of the MSML metrics:

- They can simply be used to denote repeatable computations such as in the case of stateful metrics where we want to get the summation of some number of values, perhaps all currency holdings of simulated entities in a simulation.
- Another possible purpose of metrics can be to use them as information logging tools.
    - For example: If we were modeling the return of a portfolio, a metric for the trading cost could log each days accumulated trading cost for further analysis in the post-simulation phase.
    - It could also be used to reference when we want to log things like state variables (as opposed to the stage game approach where state is being logged at every substep)
- Finally, they could be used as either KPIs or the inputs to KPIs for parameter selection under uncertainty workflows. 
    - For example, a KPI could pull from many metrics to compute a success criteria over a simulation
    - Or a metric could represent a rolling cummulative return on a portfolio and the success criteria is determined upon passing a certain threshold.

## Current Implementation

- Currently there are stateful metrics and regular metrics, where stateful have the only difference of being ones that use only state variables and parameters in computation (although they may get merged together)
- The JSON spec for stateful metrics is [here](../docs/JSON-Specification/schema-definitions-stateful-metric.md)
- The JSON spec for metrics is [here](../docs/JSON-Specification/schema-definitions-metric.md)

### Examples

1. We might use a stateful metric for a system with N users that have currency holdings state variables to calculate a metric for total system holdings
2. We might use a metric which takes a domain input of a space describing total fees to keep track of fees accumulated in a system
3. We might have a metric for error in a root finding simulation which gives us the divergence from the optimal solution

## Current Oustanding Issues

- The issues for discussion are the most important ones to talk through
- All are linked to their respective github issues

### Issues for Discussion

- [Consider rolling stateful metrics into general metrics](https://github.com/BlockScience/MSML/issues/237) - The only difference is that stateful metrics are supposed to only be based on the state and parameters, but it may make sense to merge
- [Should metrics have metric options?](https://github.com/BlockScience/MSML/issues/240) - Would allow for different metric definitions i.e. different versions of volatility or something related to a success criteria
- [Consider how to create a KPI / if it should be added](https://github.com/BlockScience/MSML/issues/308) - Metrics could be utilized for the purpose of KPIs in PSUU.
- [Metric Logger Implementation](https://github.com/BlockScience/MSML/issues/338) - Need to decide if metrics should be used for logging information

### Issues Ready for Development

- [Metric report](https://github.com/BlockScience/MSML/issues/231) - Creating the markdown report for a given metric
- [Link metrics to the different components, i.e. having what state is used in what metrics](https://github.com/BlockScience/MSML/issues/232) - Need to figure out what linkages would be good to have then it is straightforward to map
- [Add metric linkages to the reporting for components](https://github.com/BlockScience/MSML/issues/233) - After prior issue, just adding metrics into the reports where they should be featured will be easy
- [Metric python code integration](https://github.com/BlockScience/MSML/issues/319) - Ready to put in python bindings
- [Python Metaprogramming Metrics](https://github.com/BlockScience/MSML/issues/337) - Ready to build out the metaprogramming for writing cadCAD models
- [Stateful metrics not being allowed in metrics_used for policies](https://github.com/BlockScience/MSML/issues/357) - Bug to sort out

## Discussion

Moving into the discussion, the following points would be very helpful to consider during:
1. What should the roles of metrics be, and should any of the possible functionalities such as logging be offloaded to something else?
2. Are there any frameworks or past works that can be utilized as supporting documentation or literature review?
3. What does success look like for metrics? Is it better to have a more flexible but tougher to fully understand solution?

## Notes from Meeting

- We can think about blocks as potentially having different ports to metrics, that are not always necessarily used but are there
- It's important to think about "what can we peek into", and what might we want to eventually peek into
- Leaving KPIs out of MSML and as a component of PSUU probably makes sense
- We might be better off not explicitly having a spec define out what is logged
    - Instead, if we have metaprogramming and at that time want to say Metric A, Metric D, Metric F are sent as logging, it could be passed an an array or something that says which metrics should be logged
    - I also could see some people wanting to have the option to define it in the spec instead of passing. In that case, there might be a secret / optional field that could be added that allows for defining out in the spec which metrics are going to be logged
- There was a description that I gave that might be worth codifying as a research note or into the wiki, there really are a few phases for the MSML
    - Concept Spec: Define out just the abstractions, domains, codomains, policies, etc.
    - Implementation Spec: Add in policy options, control action options, etc. that describe in pseudocode / logical explanations some of the different implementations that say a policy could take on.
    - Exploratory Modeling Spec: Add in the code for blocks, allow for playing with different wirings and seeing results, possibly doing integration testing (there is a separate issue to define out a research note on how MSML could aim implementation testing)
    - Metraprogrammed Model: Use the metaprogramming features of the MSML to write out the actual model for use in production simulation software (cadCAD)
- The metrics are a very similar concept to sensors
- It might be best to actually have metrics as block representations, i.e. if we have a metric for a wiring we could define it out to show how the wiring actually passes a domain to it potentially, and how if we have metrics that depend on other metrics they work similar to composed blocks
- Keeping stateful metrics and metrics separate from a UX perspective probably makes a lot of sense to re-inforce the idea they are different
- The issue of whether or not to use metric options really depends on how we think people will use this
    - Will they define out one metric for say volatility and be happy?
    - Will they define out a normal distribution volatility, but then change it to be one with outlier removal and so they are just modifying not adding an option
    - Or will the user want the ability to say hey I have 4 possible implementations on distance metrics, I actually want to display this ability to swap out metric definitions