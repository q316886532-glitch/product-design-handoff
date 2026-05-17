# Codex Development Constraints

## Source Of Truth

- Treat `docs/` as the product and technical source of truth.
- Start every product or implementation session with `docs/00-Product-Context.md`.
- Read `docs/01-PRD.md`, `docs/User-Flows.md`, `docs/02-UI-Spec.md`, `docs/API-and-Data-Spec.md`, `docs/03-Architecture-Spec.md`, and `docs/04-Acceptance-Criteria.md` before implementation.
- If documentation conflicts, prefer newer entries in `docs/05-Decision-Log.md` and ask for clarification when behavior would materially change.
- Treat permission model, business objects, and data integration as cross-cutting concerns that must stay consistent across product, UI, architecture, and acceptance docs.

## Implementation Rules

- Do not expand MVP scope without an explicit product decision.
- Record requirement-impacting decisions in `docs/05-Decision-Log.md`.
- Record unresolved implementation blockers in `docs/06-Open-Questions.md`.
- Update `docs/00-Product-Context.md` when a decision changes product scope, module boundaries, permissions, data integration, or development readiness.
- Preserve existing project conventions once code exists.
- Prefer mature, maintained libraries for domain-specific engines, parsers, auth, payments, charts, editors, or other complex subsystems.

## Quality Bar

- Implement loading, empty, error, permission, success, and edge states described in `docs/02-UI-Spec.md`.
- Add focused tests for core user flows and business rules.
- Before handoff, verify the module-level acceptance contract in `docs/04-Acceptance-Criteria.md`.
