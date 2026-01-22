# Architectural Patterns in MSML

This guide presents common architectural patterns for structuring MSML specifications. These patterns help solve recurring design challenges and promote consistency.

## Table of Contents

- [Pipeline Pattern](#pipeline-pattern)
- [Fan-Out/Fan-In Pattern](#fan-outfan-in-pattern)
- [State Machine Pattern](#state-machine-pattern)
- [Repository Pattern](#repository-pattern)
- [Observer Pattern](#observer-pattern)
- [Strategy Pattern](#strategy-pattern)
- [Adapter Pattern](#adapter-pattern)

## Pipeline Pattern

### Intent

Process data through a sequence of transformations, where each stage's output becomes the next stage's input.

### When to Use

- Sequential data processing
- Multi-step validation
- Graduated transformations
- Clear stage boundaries

### Structure

```
Input → Stage1 → Stage2 → Stage3 → Output
```

### MSML Implementation

```json
{
  "blocks": [
    {
      "name": "ValidateInput",
      "domain": ["RawTransaction"],
      "codomain": ["ValidatedTransaction"]
    },
    {
      "name": "EnrichTransaction",
      "domain": ["ValidatedTransaction"],
      "codomain": ["EnrichedTransaction"]
    },
    {
      "name": "ExecuteTransaction",
      "domain": ["EnrichedTransaction"],
      "codomain": ["TransactionResult"]
    }
  ],
  "wiring": [
    {
      "name": "TransactionPipeline",
      "components": [
        {"name": "ValidateInput"},
        {"name": "EnrichTransaction"},
        {"name": "ExecuteTransaction"}
      ]
    }
  ]
}
```

### Benefits

- Clear data flow
- Easy to test each stage
- Simple to add/remove stages
- Natural parallelization opportunities

### Considerations

- Error handling between stages
- Pipeline breakage on validation failure
- Performance of chained operations

## Fan-Out/Fan-In Pattern

### Intent

Distribute work across multiple parallel operations, then combine results.

### When to Use

- Independent parallel computations
- Aggregating multiple data sources
- Load distribution
- Parallel validation checks

### Structure

```
           ┌→ Operation1 ─┐
Input ────→┼→ Operation2 ─┼→ Combine → Output
           └→ Operation3 ─┘
```

### MSML Implementation

```json
{
  "blocks": [
    {
      "name": "CalculateMetric1",
      "domain": ["SystemState"],
      "codomain": ["Metric1"]
    },
    {
      "name": "CalculateMetric2",
      "domain": ["SystemState"],
      "codomain": ["Metric2"]
    },
    {
      "name": "CalculateMetric3",
      "domain": ["SystemState"],
      "codomain": ["Metric3"]
    },
    {
      "name": "AggregateMetrics",
      "domain": ["Metric1", "Metric2", "Metric3"],
      "codomain": ["OverallScore"]
    }
  ],
  "wiring": [
    {
      "name": "ParallelMetrics",
      "components": [
        ["CalculateMetric1", "CalculateMetric2", "CalculateMetric3"],
        ["AggregateMetrics"]
      ]
    }
  ]
}
```

### Benefits

- Parallel execution potential
- Modular metric calculation
- Easy to add new metrics
- Clear aggregation point

### Considerations

- Synchronization of parallel paths
- Handling partial failures
- Combining heterogeneous results

## State Machine Pattern

### Intent

Model system behavior as explicit states with defined transitions.

### When to Use

- Clear lifecycle phases
- Status-dependent behavior
- Workflow management
- Approval processes

### Structure

```
State A →[Event1]→ State B →[Event2]→ State C
   ↑                                      ↓
   └──────────[Event3]────────────────────┘
```

### MSML Implementation

```json
{
  "state": [
    {
      "name": "ProposalStatus",
      "type": "enum",
      "values": ["Pending", "Active", "Approved", "Rejected", "Executed"]
    }
  ],
  "mechanisms": [
    {
      "name": "TransitionToActive",
      "domain": ["Proposal"],
      "codomain": ["UpdatedProposal"],
      "constraints": ["Proposal.status == 'Pending'"],
      "updates": [{"state": "ProposalStatus", "to": "Active"}]
    },
    {
      "name": "ApproveProposal",
      "domain": ["Proposal", "VoteResults"],
      "codomain": ["UpdatedProposal"],
      "constraints": [
        "Proposal.status == 'Active'",
        "VoteResults.approved > VoteResults.threshold"
      ],
      "updates": [{"state": "ProposalStatus", "to": "Approved"}]
    }
  ]
}
```

### Benefits

- Explicit state transitions
- Validation of valid transitions
- Clear business logic
- Audit trail of state changes

### Considerations

- State explosion with complex workflows
- Transition validation
- Concurrent state modifications

## Repository Pattern

### Intent

Centralize data access and state management behind a well-defined interface.

### When to Use

- Multiple access patterns to same data
- Complex queries on state
- Abstraction over storage details
- Separation of data access from business logic

### MSML Implementation

```json
{
  "state": [
    {
      "name": "UserRepository",
      "type": "Dict[Address, User]",
      "description": "Central user data store"
    }
  ],
  "blocks": [
    {
      "name": "GetUser",
      "description": "Retrieve user by address",
      "domain": ["Address", "UserRepository"],
      "codomain": ["User"]
    },
    {
      "name": "QueryActiveUsers",
      "description": "Find all active users",
      "domain": ["UserRepository"],
      "codomain": ["List[User]"]
    },
    {
      "name": "UpdateUser",
      "description": "Update user data",
      "domain": ["Address", "UserData", "UserRepository"],
      "codomain": ["UpdatedRepository"]
    }
  ]
}
```

### Benefits

- Centralized data access
- Consistent query interface
- Easier to optimize
- Clear data ownership

### Considerations

- Repository complexity growth
- Query performance
- State mutation coordination

## Observer Pattern

### Intent

Notify interested components when state changes occur.

### When to Use

- Event-driven architectures
- Loose coupling between components
- Audit logging
- Reactive updates

### MSML Implementation

```json
{
  "boundary_actions": [
    {
      "name": "BalanceChanged",
      "description": "Emitted when balance updates",
      "codomain": ["BalanceChangeEvent"]
    }
  ],
  "mechanisms": [
    {
      "name": "UpdateBalance",
      "domain": ["Address", "NewBalance"],
      "codomain": ["UpdatedBalance"],
      "updates": [
        {"state": "Balances", "target": "Address"}
      ],
      "emits": ["BalanceChanged"]
    }
  ],
  "policies": [
    {
      "name": "OnBalanceChanged",
      "description": "React to balance changes",
      "domain": ["BalanceChangeEvent"],
      "codomain": ["Action"]
    }
  ]
}
```

### Benefits

- Decoupled components
- Easy to add observers
- Event history tracking
- Reactive behavior

### Considerations

- Event ordering
- Observer management
- Circular dependencies
- Event storm potential

## Strategy Pattern

### Intent

Define a family of interchangeable algorithms/policies that can be selected at runtime.

### When to Use

- Multiple ways to perform an operation
- A/B testing different approaches
- User-configurable behavior
- Parameterized decision-making

### MSML Implementation

```json
{
  "policies": [
    {
      "name": "FeePolicy",
      "description": "Calculate transaction fee",
      "domain": ["Transaction", "FeeParameters"],
      "codomain": ["FeeAmount"],
      "policy_options": [
        {
          "name": "FlatFee",
          "description": "Fixed fee per transaction",
          "logic": "return fee_parameters.flat_rate"
        },
        {
          "name": "PercentageFee",
          "description": "Percentage of transaction amount",
          "logic": "return transaction.amount * fee_parameters.percentage"
        },
        {
          "name": "TieredFee",
          "description": "Fee based on amount tiers",
          "logic": "return calculate_tiered_fee(transaction.amount, fee_parameters.tiers)"
        }
      ]
    }
  ]
}
```

### Benefits

- Algorithm flexibility
- Easy to add strategies
- Testable alternatives
- Clear strategy interface

### Considerations

- Strategy selection logic
- Parameter compatibility
- Performance differences
- Testing all strategies

## Adapter Pattern

### Intent

Convert between incompatible interfaces or data formats.

### When to Use

- Integrating external systems
- Legacy compatibility
- Format transformations
- Protocol translation

### MSML Implementation

```json
{
  "blocks": [
    {
      "name": "ExternalDataAdapter",
      "description": "Convert external API format to internal format",
      "domain": ["ExternalAPIResponse"],
      "codomain": ["InternalDataFormat"]
    },
    {
      "name": "LegacySystemAdapter",
      "description": "Adapt legacy state structure to new format",
      "domain": ["LegacyState"],
      "codomain": ["ModernState"]
    }
  ]
}
```

### Benefits

- External system integration
- Format flexibility
- Backward compatibility
- Isolated conversions

### Considerations

- Conversion overhead
- Data loss in translation
- Versioning adapters
- Testing mappings

## Combining Patterns

### Example: Transaction Processing System

Combines Pipeline, Strategy, and Observer patterns:

```json
{
  "wiring": [
    {
      "name": "TransactionProcessing",
      "components": [
        "ValidateTransaction",      // Pipeline step 1
        "ApplyFeePolicy",           // Strategy pattern
        "ExecuteTransaction",       // Pipeline step 2
        "EmitTransactionEvent",     // Observer pattern
        "UpdateBalances"            // Pipeline step 3
      ]
    }
  ]
}
```

### Example: Governance System

Combines State Machine, Repository, and Fan-Out patterns:

```json
{
  "wiring": [
    {
      "name": "ProposalLifecycle",
      "components": [
        "CreateProposal",           // State Machine: → Pending
        ["ValidateProposal",        // Fan-out validation
         "CheckEligibility",
         "AssessRisks"],
        "AggregateValidation",      // Fan-in
        "ActivateProposal",         // State Machine: → Active
        "StoreInRepository"         // Repository pattern
      ]
    }
  ]
}
```

## Anti-Patterns to Avoid

### 1. The Big Ball of Mud

**Problem**: No clear structure, everything depends on everything

**Solution**: Apply separation of concerns, use clear patterns

### 2. Premature Abstraction

**Problem**: Over-engineering before understanding requirements

**Solution**: Start simple, refactor when patterns emerge

### 3. Pattern Obsession

**Problem**: Forcing patterns where they don't fit

**Solution**: Use patterns to solve problems, not for their own sake

### 4. Tight Coupling

**Problem**: Components too dependent on internal details

**Solution**: Use interfaces (spaces), depend on abstractions

### 5. God Object

**Problem**: One component does everything

**Solution**: Single responsibility principle, decompose

## Pattern Selection Guide

| Scenario | Recommended Pattern |
|----------|---------------------|
| Sequential processing | Pipeline |
| Parallel computations | Fan-Out/Fan-In |
| Lifecycle management | State Machine |
| Data access | Repository |
| Event notifications | Observer |
| Algorithm variants | Strategy |
| External integration | Adapter |

## Further Reading

- [Best Practices](BestPractices.md) - General design guidelines
- [Usage Guidelines](UsageGuidelines.md) - When to use MSML
- [Examples](CanonicalExamples.md) - Annotated examples
