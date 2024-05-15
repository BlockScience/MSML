# V0.3.3+ Proposals Research Note

The following sets up a few proposals for improvements to MSML.

## Parameter Class Names/Descriptions

- There is a [research note](https://github.com/BlockScience/MSML/blob/main/research_notes/2024-05-03%20Parameter%20Class%20Naming.md) that was put together to describe the current issue
- If the following proposal is still lacking, one option is to add another issue for further research into parameters. For example looking up how other simulation frameworks break down parameters or looking into different taxonomies of parameters that are present in academic disciplines such as systems engineering.

## Metrics as Blocks Implementation

- Keep stateful metrics and metrics separate
- Metrics will be blocks that are specified in the wirings as they require a domain passed to them (think things like the trades that just happened or summary statistics inputs)

## New Features from Client Spec Review

- Both of these new features are not high priority at the moment but have been added to the issues backlog
- Issue 1: Look into codifying the $i \in I$ with global state to see if there is a way to automatically have lowercase and uppercase symbols line up for subscripting like user_i in the group of I users.
- Issue 2: Consider how MSML might be able to support relationship mappings. There is a lot of models that rely on this kind of thing and also there are two good follow-ups: allocation tables in SysML and how SQLAlchemy takes care of relationships.

## Latex Escape Characters

## FAQ Section

## Commentary
