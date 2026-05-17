---
name: product-design-handoff
description: End-to-end product design handoff workflow for turning vague product ideas, early requirement notes, uploaded planning docs, PRD requests, UI/interaction planning, architecture planning, or Codex-ready development handoff requests into a structured product document package. Use when Codex should clarify positioning, users, MVP scope, feature modules, business flows, UI specifications, technical architecture, open-source solution choices, tests, acceptance criteria, and project constraints before implementation.
---

# Product Design Handoff

## Overview

Use this skill to guide a product idea from unclear input to a development-ready document package for Codex implementation. Default to Chinese正文 with English file names, and keep the output practical enough for another Codex agent to build from.

## Operating Rules

- Start with discovery, not implementation. Do not write production code while the product, flows, UI states, data model, or acceptance criteria are still materially unclear.
- Preserve user intent. Separate facts, assumptions, inferred requirements, conflicts, and open questions.
- Ask focused questions in small batches. Prefer questions that decide positioning, scope, workflow, UI behavior, architecture, or acceptance criteria.
- Keep a visible project memory. Use `docs/00-Product-Context.md` as the handoff entry point, record decisions in `docs/05-Decision-Log.md`, and track unresolved blockers in `docs/06-Open-Questions.md`.
- Track three cross-cutting concerns across documents: permission model, business objects, and data integration. Do not leave these topics isolated in only one document when they affect product, UI, architecture, or acceptance.
- Confirm at least one complete business loop before deep UI design or architecture planning. A complete loop includes the entry point, primary role, goal, preconditions, happy path, alternate/error paths, key business objects, completion state, and acceptance signal.
- Treat external technical choices as current-state decisions. When selecting open-source frameworks, hosted services, model providers, pricing-sensitive tools, or active libraries, verify current options with official or primary sources when browsing is available.
- Use the existing codebase when one exists. Inspect repository structure, stack, conventions, and constraints before proposing architecture or templates.

## Workflow

### 1. Synthesize Input

Read the user's prompt and any provided documents. Produce a concise synthesis before asking questions:

- 已知事实
- 隐含假设
- 目标用户和场景线索
- 可能冲突或风险
- 缺失决策
- 建议的下一步问题

If uploaded documents already contain usable sections, map them to the document package instead of asking the user to repeat information.

### 2. Confirm Product Positioning

Before detailed design, confirm:

- 产品是什么
- 解决谁的什么问题
- 用户获得的核心收益
- 业务目标或成功指标
- 主要用户角色
- 第一版 MVP 范围
- 明确不做的 non-goals

Do not initialize the full document package until the user has either approved the positioning or explicitly asked for scaffolding first.

### 3. Initialize The Project Workspace

When the user wants a project document package, run:

```bash
python3 <skill-dir>/scripts/init_product_workspace.py <project-dir> --project-name "<name>"
```

Use `--overwrite` only when the user explicitly allows replacing existing files. The script must be treated as the preferred way to create the standard package.

### 4. Maintain Product Context First

After scaffolding, keep `docs/00-Product-Context.md` current before deep-diving into other docs. It should remain the concise entry document for:

- design flow index
- product positioning
- target users and roles
- core scenarios
- product boundary
- level-1 modules
- glossary
- document index
- context rules
- decision and open-question summaries

Move implementation details to the numbered source docs instead of bloating the context entry.

### 5. Elaborate Product Docs Iteratively

Advance the package in this order unless the user's context clearly demands a different route:

1. `docs/00-Product-Context.md`: entry context, document index, product boundary, level-1 modules, cross-cutting concern status.
2. `docs/01-PRD.md`: positioning, users, business objects, scope, feature modules, business rules, version plan.
3. `docs/User-Flows.md`: main flows, role paths, exception paths, state transitions.
4. `docs/02-UI-Spec.md`: pages, navigation, components, states, design tokens, permission visibility, terminal adaptation.
5. `docs/API-and-Data-Spec.md`: entities, data ownership, permissions, API needs, integrations.
6. `docs/03-Architecture-Spec.md`: system boundary, stack, module breakdown, data model, permission model, security, deployment, open-source evaluation.
7. `docs/04-Acceptance-Criteria.md`: module-level normal, exception, boundary, permission, and non-functional acceptance.
8. `docs/05-Decision-Log.md` and `docs/06-Open-Questions.md`: update continuously.

Do not proceed from step 3 into detailed UI specification or architecture planning until at least one MVP-critical business loop is complete enough to implement and validate. If the loop is unclear, pause and ask only the questions needed to complete that loop.

Keep each document implementation-oriented. Avoid filling templates with generic prose that does not constrain development.

### 6. Run The Readiness Gate

Before saying development can start, verify:

- `docs/00-Product-Context.md` gives a concise, current entry point for the whole project.
- The MVP scope is explicit and bounded.
- Every primary user role has at least one complete happy path.
- At least one MVP-critical business loop is fully specified in `docs/User-Flows.md` before UI and architecture depend on it.
- Critical empty, loading, error, permission, and edge states are specified.
- Permission model, business objects, and data integration are reflected in product, UI, architecture, and acceptance docs where relevant.
- Required data entities, integrations, and permissions are clear enough to implement.
- Architecture choices include rationale and known tradeoffs.
- `docs/04-Acceptance-Criteria.md` functions as an acceptance contract, not just a loose test list.
- Open questions are either resolved or explicitly marked as non-blocking.

If the gate fails, state what is blocking development and ask only the next highest-impact questions.

## Bundled Resources

- `scripts/init_product_workspace.py`: create the standard docs package and project constraint files without overwriting existing files by default.
- `assets/project-template/`: source templates copied by the initialization script.
- `references/product-discovery-question-bank.md`: read when selecting the next clarification questions.
- `references/document-maturity-checklist.md`: read when judging whether documents are specific enough.
- `references/development-readiness-checklist.md`: read before development handoff.
- `references/architecture-evaluation-rubric.md`: read when selecting architecture, open-source projects, services, or frameworks.
