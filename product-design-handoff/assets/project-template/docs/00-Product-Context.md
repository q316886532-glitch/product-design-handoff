# Product Context: {{PROJECT_NAME}}

Last updated: {{DATE}}

## 1. Design Flow Index

| Step | Document | Status | Notes |
| --- | --- | --- | --- |
| 00 | Product context | Draft | Entry document for every handoff. |
| 01 | PRD | Draft | Requirements and product rules. |
| 02 | UI Spec | Draft | Interaction and visual behavior. |
| 03 | Architecture Spec | Draft | Technical solution and system boundaries. |
| 04 | Acceptance Criteria | Draft | Product acceptance contract. |
| 05 | Decision Log | Active | Confirmed decisions. |
| 06 | Open Questions | Active | Pending decisions and blockers. |

## 2. Product Positioning

- 产品一句话:
- 解决的问题:
- 目标用户:
- 核心收益:
- 业务目标:
- 成功指标:

## 3. Target Users And Roles

| Role | Goal | Key Scenario | Permission Level | Notes |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 4. Core Scenarios

| Scenario | Primary Role | Trigger | Success Outcome | Priority |
| --- | --- | --- | --- | --- |
|  |  |  |  |  |

## 5. Product Boundary

### MVP In Scope

- 

### Explicit Non-Goals

- 

### Later Versions

- 

## 6. Level-1 Modules

| Module | Purpose | Owner Role | Related Docs | Status |
| --- | --- | --- | --- | --- |
|  |  |  | `01-PRD.md`, `02-UI-Spec.md`, `04-Acceptance-Criteria.md` | Draft |

## 7. Cross-Cutting Concerns

Track these topics across product, UI, architecture, and acceptance docs.

| Concern | Source Of Truth | Related Docs | Current Status |
| --- | --- | --- | --- |
| Permission model | `03-Architecture-Spec.md` | `02-UI-Spec.md`, `04-Acceptance-Criteria.md` | Draft |
| Business objects | `01-PRD.md` | `API-and-Data-Spec.md`, `03-Architecture-Spec.md` | Draft |
| Data integration | `03-Architecture-Spec.md` | `01-PRD.md`, `API-and-Data-Spec.md` | Draft |

## 8. Glossary

| Term | Meaning | Notes |
| --- | --- | --- |
|  |  |  |

## 9. Document Index

- `00-Product-Context.md`: 入口上下文、文档索引、边界、横切关注点。
- `01-PRD.md`: 完整需求规格、业务对象、功能模块、业务规则、版本规划。
- `User-Flows.md`: 详细用户流程、异常流程、状态转换。
- `02-UI-Spec.md`: 页面、组件、交互、设计 token、权限可见性、终端适配。
- `API-and-Data-Spec.md`: 数据实体、接口、权限、数据生命周期、集成细节。
- `03-Architecture-Spec.md`: 技术架构、系统边界、开源方案评估、安全和部署。
- `04-Acceptance-Criteria.md`: 模块级验收标准和验收结果记录。
- `05-Decision-Log.md`: 关键决策、原因、影响范围、已同步上下文。
- `06-Open-Questions.md`: 待确认问题、所属模块、影响、建议确认方式。

## 10. Context Rules

- Start every new design or development session by reading this document.
- Keep this document concise; move details into the numbered source documents.
- When a decision changes product scope, UI behavior, architecture, permissions, or acceptance criteria, update this document and `05-Decision-Log.md`.
- If an unresolved question blocks implementation, add it to `06-Open-Questions.md`.

## 11. Decision Summary

| Date | Decision | Related Detail |
| --- | --- | --- |
| {{DATE}} | Initialize product design handoff docs. | `05-Decision-Log.md` |

## 12. Open Question Summary

| ID | Question | Blocking? | Detail |
| --- | --- | --- | --- |
| Q-001 |  | Yes | `06-Open-Questions.md` |
