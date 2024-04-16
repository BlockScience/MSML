# Metrics Working Group

## Executive Summary

## The Role and Use of Metrics in MSML and Beyond

Metrics as KPIs and/or inputs to KPIs?
Metrics as loggers?
Metrics as modular functionality and nothing more?

## Current Implementation

## Current Oustanding Issues

### Issues for Discussion

[Consider rolling stateful metrics into general metrics](https://github.com/BlockScience/MSML/issues/237) - The only difference is that stateful metrics are supposed to only be based on the state and parameters, but it may make sense to merge
[Should metrics have metric options?](https://github.com/BlockScience/MSML/issues/240) - Would allow for different metric definitions i.e. different versions of volatility or something related to a success criteria
[Consider how to create a KPI / if it should be added](https://github.com/BlockScience/MSML/issues/308) - Metrics could be utilized for the purpose of KPIs in PSUU.
[Metric Logger Implementation](https://github.com/BlockScience/MSML/issues/338) - Need to decide if metrics should be used for logging information

### Issues Ready for Development

[Metric report](https://github.com/BlockScience/MSML/issues/231) - Creating the markdown report for a given metric
[Link metrics to the different components, i.e. having what state is used in what metrics](https://github.com/BlockScience/MSML/issues/232) - Need to figure out what linkages would be good to have then it is straightforward to map
[Add metric linkages to the reporting for components](https://github.com/BlockScience/MSML/issues/233) - After prior issue, just adding metrics into the reports where they should be featured will be easy
[Metric python code integration](https://github.com/BlockScience/MSML/issues/319) - Ready to put in python bindings
[Python Metaprogramming Metrics](https://github.com/BlockScience/MSML/issues/337) - Ready to build out the metaprogramming for writing cadCAD models
[Stateful metrics not being allowed in metrics_used for policies](https://github.com/BlockScience/MSML/issues/357) - Bug to sort out

## Notes from Meeting

- To be filled in after 4/18