# MSML Best Practices

This guide provides opinionated recommendations for building effective, maintainable mathematical specifications with MSML.

## Table of Contents

- [Core Principles](#core-principles)
- [Component Design](#component-design)
- [Naming Conventions](#naming-conventions)
- [Specification Organization](#specification-organization)
- [Common Pitfalls](#common-pitfalls)
- [Scaling Considerations](#scaling-considerations)

## Core Principles

### 1. Single Responsibility

Each component (Block, Space, State variable) should have one clear purpose.

**Good:**
- `CalculateReward` - Computes reward based on performance
- `UpdateBalance` - Updates user balance from transaction
- `ValidateTransaction` - Checks transaction validity

**Bad:**
- `ProcessEverything` - Does multiple unrelated operations
- `UpdateAndValidate` - Mixes validation and state updates

### 2. Explicit Over Implicit

Make dependencies and data flows explicit through proper domain/codomain declarations.

**Good:**
```json
{
  "name": "CalculateInterest",
  "domain": ["Balance", "InterestRate"],
  "codomain": ["InterestAmount"]
}
```

**Bad:**
```json
{
  "name": "CalculateInterest",
  "domain": [],  // Missing dependencies
  "codomain": []
}
```

### 3. Composability

Design components to be composable and reusable across different contexts.

**Good:**
- Small, focused blocks that can be combined
- Generic spaces that work with multiple blocks
- Reusable metrics across policies

**Bad:**
- Large monolithic blocks that can't be decomposed
- Tightly coupled components
- Context-specific implementations that can't be reused

## Component Design

### Blocks

**Blocks represent atomic operations in your system.**

#### Design Guidelines

1. **Focus**: One clear transformation or computation
2. **Size**: Aim for 3-7 inputs/outputs (cognitive load limit)
3. **Stateless**: Blocks should be pure functions when possible
4. **Testable**: Clear inputs/outputs make testing straightforward

#### Good Block Design

```json
{
  "name": "CalculateVotingPower",
  "description": "Calculates voting power based on token balance and lock duration",
  "domain": ["TokenBalance", "LockDuration"],
  "codomain": ["VotingPower"],
  "parameters_used": ["VotingPowerMultiplier"],
  "constraints": ["TokenBalance > 0", "LockDuration >= MinLockDuration"]
}
```

#### Poor Block Design

```json
{
  "name": "ProcessVote",
  "description": "Does everything related to voting",
  "domain": ["Everything"],  // Too broad
  "codomain": ["Results"],   // Too vague
  // Unclear what this block actually does
}
```

### Spaces

**Spaces define the types and structure of data flowing between blocks.**

#### Design Guidelines

1. **Type Safety**: Clearly specify variable types
2. **Validation**: Include domain constraints
3. **Documentation**: Explain the meaning and units of variables
4. **Granularity**: One space per logical data group

#### Good Space Design

```json
{
  "name": "TokenBalance",
  "schema": {
    "amount": {
      "type": "float",
      "description": "Token amount in base units",
      "constraints": "amount >= 0"
    },
    "locked": {
      "type": "boolean",
      "description": "Whether tokens are locked"
    }
  }
}
```

### State Variables

**State represents the persistent data in your system.**

#### Design Guidelines

1. **Minimal**: Only include truly persistent state
2. **Normalized**: Avoid redundant or derivable state
3. **Clear Ownership**: Each state variable should have clear update rules
4. **Versioned**: Consider versioning for evolving state structures

#### State Organization

```json
{
  "state": [
    {
      "name": "UserBalances",
      "type": "Dict[Address, Balance]",
      "description": "Mapping of user addresses to token balances",
      "updated_by": ["Transfer", "Mint", "Burn"]
    },
    {
      "name": "TotalSupply",
      "type": "float",
      "description": "Total token supply",
      "updated_by": ["Mint", "Burn"]
    }
  ]
}
```

### Policies vs Mechanisms

**Policies** = *What* to do (decision logic)
**Mechanisms** = *How* to update state (state transitions)

#### Policy Guidelines

- Focus on decision-making logic
- Return action parameters, not state changes
- Can be parameterized by user preferences
- Multiple policy options for different strategies

#### Mechanism Guidelines

- Focus on state update logic
- Deterministic given inputs
- Validate inputs before updating state
- Document update semantics clearly

## Naming Conventions

### General Rules

1. **Descriptive**: Names should clearly indicate purpose
2. **Consistent**: Use consistent patterns across the spec
3. **Avoid Abbreviations**: Unless universally understood
4. **CamelCase**: For multi-word names

### Component Naming Patterns

| Component | Pattern | Example |
|-----------|---------|---------|
| Blocks | Verb + Noun | `CalculateReward`, `ValidateTransaction` |
| Spaces | Noun | `TokenBalance`, `UserProfile` |
| States | Noun (plural if collection) | `Balances`, `CurrentEpoch` |
| Parameters | Descriptive noun | `InterestRate`, `MaxSupply` |
| Policies | Verb + Context | `SelectValidator`, `DetermineReward` |
| Mechanisms | Update + Target | `UpdateBalance`, `TransferTokens` |

### Variable Naming

```python
# Good
user_balance
total_supply
interest_rate
transaction_amount

# Bad
ub      # Too short
x1      # Meaningless
tmp     # Generic
data    # Too vague
```

## Specification Organization

### File Structure

Organize complex specs into multiple files:

```
spec/
├── main.json           # Top-level spec with references
├── types/
│   ├── tokens.json
│   └── users.json
├── state/
│   ├── balances.json
│   └── governance.json
├── mechanisms/
│   ├── transfer.json
│   └── minting.json
└── policies/
    ├── fee_policy.json
    └── reward_policy.json
```

### Modular Design

Break large systems into logical modules:

1. **By Domain**: Group related functionality
   - Token economics
   - Governance
   - Staking

2. **By Layer**: Separate concerns
   - Data layer (state, types)
   - Logic layer (policies, mechanisms)
   - Presentation layer (displays)

3. **By Lifecycle**: Separate temporal concerns
   - Initialization
   - Regular operations
   - Cleanup/finalization

## Common Pitfalls

### 1. Over-coupling

**Problem**: Components depend on too many other components

**Solution**: Use intermediate spaces to decouple

```json
// Bad: Mechanism depends on multiple unrelated state variables
{
  "domain": ["UserBalance", "SystemConfig", "MarketPrice", "TimeOfDay"],
  ...
}

// Good: Introduce focused intermediate spaces
{
  "domain": ["TransactionContext"],  // Aggregates what's needed
  ...
}
```

### 2. God Blocks

**Problem**: Single block does too much

**Solution**: Decompose into smaller blocks

```json
// Bad
{
  "name": "ProcessTransaction",
  "description": "Validates, executes, logs, and notifies"
}

// Good - Split into pipeline
[
  {"name": "ValidateTransaction"},
  {"name": "ExecuteTransaction"},
  {"name": "RecordTransaction"},
  {"name": "EmitNotification"}
]
```

### 3. Implicit Dependencies

**Problem**: Hidden dependencies make reasoning difficult

**Solution**: Make all dependencies explicit

```json
// Bad
{
  "parameters_used": []  // Actually uses parameters internally
}

// Good
{
  "parameters_used": ["InterestRate", "CompoundingFrequency"]
}
```

### 4. Leaky Abstractions

**Problem**: Implementation details leak into specification

**Solution**: Focus on *what*, not *how*

```json
// Bad
{
  "description": "Uses binary search to find the optimal value"
}

// Good
{
  "description": "Finds the optimal fee value given constraints"
}
```

### 5. Inconsistent Granularity

**Problem**: Some blocks are atomic, others are coarse-grained

**Solution**: Maintain consistent level of abstraction

- Either stay high-level (conceptual)
- Or go detailed (implementation-ready)
- Don't mix both in same spec

## Scaling Considerations

### Small Systems (< 10 blocks)

- Single file is fine
- Focus on clarity over optimization
- Inline documentation sufficient

### Medium Systems (10-50 blocks)

- Split into logical modules
- Use wiring diagrams to show composition
- Maintain glossary of terms
- Consider versioning strategy

### Large Systems (50+ blocks)

- Multi-file organization essential
- Formal documentation system (Obsidian vault)
- Clear ownership of components
- Automated validation in CI
- Version control for spec evolution
- Regular refactoring to reduce complexity

### Handling Complexity

When systems grow too complex:

1. **Introduce Layers**: Separate high-level and detailed views
2. **Use Composition**: Build complex behaviors from simple blocks
3. **Abstract Patterns**: Extract common patterns into reusable components
4. **Hierarchical Organization**: Group related components
5. **Progressive Disclosure**: Show detail only when needed

## Testing Your Specification

### Validation Checklist

- [ ] All blocks have clear domain/codomain
- [ ] All dependencies are explicit
- [ ] State update paths are documented
- [ ] Naming is consistent and descriptive
- [ ] No circular dependencies
- [ ] Constraints are specified
- [ ] Types are defined
- [ ] Parameters are documented

### Review Questions

1. Can a new contributor understand each component's purpose?
2. Are data flows clear without reading implementation?
3. Can components be tested independently?
4. Is the spec at consistent level of detail?
5. Are there obvious redundancies or inefficiencies?

## Continuous Improvement

### Refactoring Indicators

Signs your spec needs refactoring:

- Adding new features is difficult
- Many components change together
- Difficulty explaining data flows
- Lots of special cases
- Growing parameter lists
- Naming becomes unclear

### Evolution Strategies

1. **Backward Compatibility**: Version major changes
2. **Deprecation Path**: Mark old components before removal
3. **Migration Guides**: Document how to adapt to changes
4. **Changelog**: Track specification evolution
5. **Git Tags**: Mark stable versions

## Additional Resources

- [Architectural Patterns](ArchitecturalPatterns.md) - Common design patterns
- [Usage Guidelines](UsageGuidelines.md) - When and how to use MSML
- [Examples](CanonicalExamples.md) - Annotated examples
- [FAQ](FAQ.md) - Common questions and answers
