# Concept Specs Ideation


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

#### Option 1:

1. Source: string, such as "BlockA-1" for second port of BlockA codomain
2. Target: string, such as "BlockB-0" for first port of BlockB domain

#### Option 2:

1. SourceBlock: ForeignKey to Block.Name, string
2. TargetBlock: ForeignKey to Block.Name, string
3. Source Port: Related to SourceBlock.Codomain as the index, integer
4. Target Port: Related to TargetBlock.Domain as the index, integer