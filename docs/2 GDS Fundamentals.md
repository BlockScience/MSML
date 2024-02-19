# GDS Fundamentals

For more information with regards to the GDS fundamentals, one can look at this [repository](https://github.com/BlockScience/GDS-MSML-cadCAD). Below is abbreviated documentation describing the fundamentals of Generalized Dynamical Systems (GDS).

## Blocks

A Block is a parameterized operation that, for each Point in its Parameters Space, maps a Point in an input Space to a unique point in an output Space.	

Blocks are characterized by three things:

**Domain**: The space(s) that are taken in for the function
**Codomain**: The space(s) that are emitted out from the function
**Logic**: The logic that describes the transformation from domain to codomain

## Spaces

A space is a pointer to a collection of dimensions.	For example we might have a space such as cartesian coordinates with the schema {"x": float, "y": float}. Spaces are passed between domains and codomains of blocks.

## Wiring

A wiring is a block composed of other blocks with specific behaviors or orders of execution. For instance, there can be wirings that have blocks run one after another, passing their codomains to the next block's domain. There can also be wirings for blocks that all should run in parallel.