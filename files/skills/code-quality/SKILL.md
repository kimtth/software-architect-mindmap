---
name: code-quality
description: Implement, fix, or refactor code with minimal scope, clear reasoning, and verification proportional to the change. Use when asked to improve code quality, resolve a defect, implement a feature, or make a focused refactor while following project conventions.
---

# Code Quality

## When to Use

Use this skill for implementation, bug fixes, and focused refactoring in an existing codebase.

## Workflow

1. Inspect the relevant code, documentation, and project conventions.
2. Define the expected outcome and identify the root cause or required behavior.
3. Resolve material ambiguity, then make the smallest complete change.
4. Verify the outcome with the relevant tests, builds, integration checks, and runtime or visual checks.
5. Update directly related documentation and report the result and known limitations.

## Development Guidelines

- **Simplicity First:** Write the minimum code required to solve the problem. Nothing speculative.
- **Think Before Coding:** Don't assume. Don't hide confusion. Surface trade-offs.
- **Surgical Changes:** Modify only what is necessary. Clean up only your own changes.
- **Goal-Driven Execution:** Define success criteria and iterate until verified.
- Do not add complexity to handle edge cases.
- Do not consider backward compatibility.
- Regularly clean the codebase to identify contradictions, obsolete files, and outdated documents.

## Documentation and Working Memory

Create five Markdown files for working memory and user guidance:

1. `README.md` — Developer information.
2. `Architecture.md` — Architecture and white paper.
3. `troubleshooting.md` — Time- and token-intensive issues, unexpected errors, and their resolutions to prevent recurrence.
4. `Artifacts.md` — List all artifacts created in the codebase.
5. `Assumptions.md` — Distinguish between your assumptions and decisions shared by me.

## Testing and Verification

- **Test Approach — Avoid Relying on TDD Alone:** Unit tests alone do not ensure that the task is fully completed. Verify the results through end-to-end (E2E) testing and visual testing from the user's perspective.
- **Very Important:** Do not stop after unit tests pass. Verify the solution with builds, integration checks, and focused runtime smoke checks.

## Code Quality

- **Very Important:** Keep the codebase compact, lean, concise, and clean.

---

## Principles
- Prefer simplicity, clarity, and correctness.
- Make the smallest change that fully solves the problem.
- Avoid overengineering, unnecessary abstractions, and speculative complexity.
- Follow existing project conventions and architecture.
- Do not introduce backward compatibility unless explicitly required.

## Implementation
- Inspect relevant code before making changes.
- Identify root causes; avoid superficial fixes.
- Reuse existing components and dependencies.
- Avoid unrelated refactoring or modifications.
- Do not add dependencies without clear justification.
- Preserve existing behavior outside the requested scope.

## Execution
- Act autonomously; do not stop at planning when implementation is requested.
- Make reasonable assumptions and proceed.
- Ask questions only when ambiguity materially affects correctness.
- Prefer direct implementation over unnecessary discussion.

## Verification
- Run relevant tests and checks proportional to the change.
- Add tests when they provide meaningful regression coverage.
- Fix issues introduced by your changes.
- Never claim verification that was not performed.

## Completion
- Ensure the implementation satisfies the request.
- Update documentation when necessary.
- Report changes, verification results, and known limitations concisely.