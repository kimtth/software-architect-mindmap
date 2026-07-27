# Architecture Docs

Generate three files for this repository:

- `mermaid.md`: system flow and architecture diagrams, down to core class level.
- `code-review-guide.md`: practical guide for reviewing a large repo like this one.
- `feature.md`: a complete, evidence-based inventory of all available user-facing and operational features.

Read the code first. Do not guess.

## Method

1. List workspace. Read README, docs, config, package/build files.
2. Identify stack, layers, entry points, runtime shape.
3. Trace the main path: entry -> handler -> orchestrator -> state/data -> response.
4. Search for DI, handlers, middleware, orchestrators, state, persistence, external calls.
5. Pick core classes by fan-in/out, lifecycle ownership, state ownership, and failure risk.
6. Write outputs tailored to repo type: Web/API/CLI/Library/Microservices/Data/Mobile.

## Feature Inventory

In `feature.md`, list every available feature discovered from the code, documentation, configuration, CLI help, routes, and tests. Do not infer features that are not implemented.

For each feature, include:

- Feature name and a concise description.
- How users access it (UI, API route, CLI command, library API, configuration, or background workflow).
- Main source files that implement it, using relative paths only.
- Important inputs, outputs, limitations, prerequisites, and feature flags where applicable.

Group related features by area. Distinguish implemented features from experimental, preview, disabled-by-default, or planned capabilities. Include administrative, observability, integration, and error-handling capabilities when they are available to users or operators.

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
