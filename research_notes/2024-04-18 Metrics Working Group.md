# Metrics Working Group

## Executive Summary

The future of metrics in MSML has a few different paths that can be taken, and as such a call is being put together to discuss some of the finer points.

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

## Current Oustanding Issues

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

## Notes from Meeting

- To be filled in after 4/18