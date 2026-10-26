# Development Guidelines

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
