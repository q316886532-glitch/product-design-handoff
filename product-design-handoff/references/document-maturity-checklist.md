# Document Maturity Checklist

Use this checklist to judge whether the docs are useful for implementation, not merely complete-looking.

## 00 Product Context

- It is the first document another Codex agent should read.
- Product positioning, target users, product boundary, level-1 modules, glossary, and document index are current.
- Decision and open-question summaries point to the detailed records.
- Permission model, business objects, and data integration have clear cross-document source-of-truth links.

## 01 PRD

- Product positioning is specific enough to reject unrelated features.
- MVP scope and non-goals are explicit.
- Each primary role has clear goals and permissions.
- Business objects are defined before detailed feature decomposition.
- Feature modules include priority, rules, business objects, UI surface, and acceptance links.
- Core scenarios, exception scenarios, data sources, and version plan are explicit.

## User Flows

- Each critical flow has preconditions, happy path, alternate paths, and completion state.
- Failure modes are represented where they affect product behavior.
- State transitions are clear for important entities.

## 02 UI Spec

- Every main page has purpose, actions, content, navigation, and states.
- Empty, loading, error, permission, validation, and success states are specified where relevant.
- Permission visibility is specified for role-sensitive actions and components.
- Design tokens cover the tokens the implementation must preserve.
- Terminal/device adaptation is explicit enough for desktop, tablet, and mobile expectations.
- Responsive and accessibility expectations are practical.

## API And Data

- Core entities and relationships are named.
- Permission-sensitive actions are explicit.
- API/actions include request, response, auth, and error expectations where needed.
- External integrations include failure handling.

## 03 Architecture

- System boundaries are explicit.
- Stack choices match product needs and team/project constraints.
- Open-source/service decisions use the 8-dimension evaluation table for high-impact dependencies.
- Permission model, security design, deployment architecture, and technical risks are explicit.
- Non-functional requirements are concrete enough to guide implementation.

## 04 Acceptance Criteria

- Acceptance is organized by module, not only by generic test type.
- Normal, exception, boundary, permission, and non-functional cases are covered for core modules.
- Acceptance criteria are testable with clear expected behavior.
- Acceptance result records can capture date, result, evidence, issues, and owner.

## 05 Decision Log And 06 Open Questions

- Decisions include rationale, alternatives, impact scope, and synced context.
- Open questions include module, impact, suggested confirmation method, blocking status, owner, and status.
