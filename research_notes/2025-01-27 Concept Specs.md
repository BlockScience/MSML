# Concept Math Specs Ideation

## Executive Summary

- The following research note defines out the most parsimonious schemas and relations for a concept math spec
- The idea is that this can be further enhanced and plugged into other interoperable workflows
- For example, schemas for the spaces can be added in at a further point and potentially have specified types

## Proposed JSON Schema

### Space

1. Name: PrimaryKey, string
2. Description: Optional, string

### Block

1. Name: PrimaryKey, string
2. Description: Optional, string
3. Domain: ForeignKeys to Space.Name, List[string]
4. Codomain: ForeignKeys to Space.Name, List[string]

### Wiring

- Might need a name or something for IDs
- Might want to consider allowing multiple target and source ports

#### Option 1:

1. Source: string, such as "BlockA-1" for second port of BlockA codomain
2. Target: string, such as "BlockB-0" for first port of BlockB domain

#### Option 2:

1. SourceBlock: ForeignKey to Block.Name, string
2. TargetBlock: ForeignKey to Block.Name, string
3. Source Port: Related to SourceBlock.Codomain as the index, integer
4. Target Port: Related to TargetBlock.Domain as the index, integer


### Systems

1. Name: PrimaryKey, string
2. Description: Optional, string
3. Wirings: ForeignKeys to Wiring, List[strings]


## Current MSML Wiring & Comparison

- Currently a wiring needs two components - the type (either stack or parallel) and the components, a list of blocks or wirings (there is a recursive wiring builder that makes sure the wirings get created in the right order)
- For a stack block, all adjacent blocks have validations that domain and codomain map
- Internally, all the port wirings are automatically built out for both mapping as well as execution
- Wirings in this way can be built out to automatically map to the proposed "Wiring" schema in concept specs or potentially changed
- The wirings are similar to a DAG
- A stack block wiring has domain of the first component and codomain of the last component
- A parallel block has the summation of component domains and component codomains
- There are future potential wiring types such as a looping block or having a notation for multiple outputs of the spaces, i.e. similar to if we have 1-N outputs that are variable between a block but they all follow the same codomain space schema


## Proposed Relational Schema V2

### Space

1. ID: PrimaryKey
2. Name: string
3. Description: Optional, string

### Block

1. ID: PrimaryKey
2. Name: string
3. Description: Optional, string

### Ports

1. ID: PrimaryKey
2. Name: string
3. Index: Integer
4. Space: ForeignKey to Space.Name, string

### Terminals

1. ID: PrimaryKey
2. Name: string
3. Index: Integer
4. Space: ForeignKey to Space.Name, string

## Proposed Schema V2

### Space

{"ID": PrimaryKey,
"Name": string,
"Description": string}

### Block

{"ID": PrimaryKey,
"Name": string,
"Description": string,
"Domain": List[Space.ID],
"Codomain": List[Space.ID]}

## Concrete Block

{"ID": PrimaryKey,
"Name": string,
"Description": string,
"Parent": Block.ID}

- It is legal to have many to one concrete blocks of abstract blocks

## Wire (Concrete Space)

{"ID": PrimaryKey,
"Parent": Space.ID,
"SourceBlock": ConcreteBlock.ID,
"TargetBlock": ConcreteBlock.ID,
"SourceIndex": int,
"TargetIndex": int}

- Check matches up

## System

{"ConcreteBlocks": List[ConcreteBlock.ID],
"Wires": List[Wire.ID]}

- Check that:
    - All of the ports/domain need to be filled
    - All domain ports only get one input
    - Terminals can go 0...N ports (and they would just be sending replicas of the same output)