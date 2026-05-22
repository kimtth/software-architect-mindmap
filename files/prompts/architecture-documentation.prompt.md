# Architecture Docs

Generate two files for this repository:

- `mermaid.md`: system flow and architecture diagrams, down to core class level.
- `code-review-guide.md`: practical guide for reviewing a large repo like this one.

Read the code first. Do not guess.

## Method

1. List workspace. Read README, docs, config, package/build files.
2. Identify stack, layers, entry points, runtime shape.
3. Trace the main path: entry -> handler -> orchestrator -> state/data -> response.
4. Search for DI, handlers, middleware, orchestrators, state, persistence, external calls.
5. Pick core classes by fan-in/out, lifecycle ownership, state ownership, and failure risk.
6. Write outputs tailored to repo type: Web/API/CLI/Library/Microservices/Data/Mobile.

## Diagrams

- Use Mermaid.
- Include `<<interface>>` where relevant.
- Use visibility markers: `+`, `-`, `#`.
- Use relationships: `<|--`, `<|..`, `*--`, `-->`, `..>`.
- After each diagram, list source files used. Relative paths only.

## Review Guide

Answer:

- Where to start a code review, and why.
- How to find core classes/modules.
- Which flows carry the most risk.
- What files prove each claim.
