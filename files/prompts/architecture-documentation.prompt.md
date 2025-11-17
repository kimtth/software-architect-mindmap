# Architecture Documentation Prompt

Generate two files for any repository:

1. **`mermaid.md`**: You are a Mermaid diagram expert. Generate Mermaid diagrams in this project for a system flow diagram and system architecture with core class level.

2. **`code-review-guide.md`**: Provide me with the know-how for reviewing the code of a large repository, similar to this codebase. Where is your starting point for a code review, and why? How do you determine which classes are core?

## Execution
1. List workspace → read docs → identify stack/layers/entry points
2. Semantic search: DI, handlers, orchestrators, state, middleware
3. Generate diagrams with `<<interface>>`, `+/-/#` visibility, relationships (`<|--`, `<|..`, `*--`, `-->`, `..>`)
4. After each diagram: append source file list (relative paths)
5. Tailor review guide to stack (Web/API/CLI/Library/Microservices/Data/Mobile)

## Core Principles
- Read code; don't guess
- Follow flow: entry → handler → orchestrator → data → response
- Quantify core: fan-in/out + lifecycle + risk
- Provide traceability: entities → files
