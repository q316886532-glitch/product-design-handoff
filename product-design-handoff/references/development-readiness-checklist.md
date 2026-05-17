# Development Readiness Checklist

Use this before handing a project to Codex for implementation.

## Ready

- `docs/00-Product-Context.md` is current and can serve as the first-read entry document.
- The first development milestone can be implemented without product invention.
- The core user journey has start, end, success, and failure states.
- At least one MVP-critical business loop is complete before the UI and architecture specs rely on it.
- Required pages/components and their states are listed.
- Permission model, business objects, and data integrations are clear and consistent across PRD, UI, architecture, and acceptance docs.
- Architecture choices are documented with rationale.
- `docs/04-Acceptance-Criteria.md` defines module-level normal, exception, boundary, permission, and non-functional acceptance.
- Remaining open questions are marked non-blocking or deferred.

## Not Ready

Treat the project as not ready if any of these are true:

- The project lacks a current `00-Product-Context.md` or it does not match the detailed docs.
- MVP scope is a feature wishlist rather than a bounded release.
- No MVP-critical business loop has a clear entry point, role, goal, happy path, alternate/error paths, business objects, completion state, and acceptance signal.
- User roles or permissions are unknown but affect implementation.
- Business objects are not defined before feature decomposition.
- UI behavior depends on unstated product rules.
- Data ownership, persistence, or integration boundaries are unclear.
- A critical technology choice requires current research and has not been verified.
- Acceptance criteria are too vague to test or omit permission/boundary behavior for core modules.

## Handoff Output

When ready, provide:

- Development objective
- Docs reviewed
- Key constraints
- First implementation milestone
- Acceptance expectations
- Non-blocking open questions
