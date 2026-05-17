# {{PROJECT_NAME}}

本文档包用于把产品需求推进到 Codex 可开发状态。

## 文档入口

每次接手项目时，先读 `docs/00-Product-Context.md`。

核心文档：

- `docs/00-Product-Context.md`: 入口上下文、文档索引、产品边界、一级模块、横切关注点
- `docs/01-PRD.md`: 产品定位、目标用户、业务对象、MVP 范围、功能模块、版本规划
- `docs/02-UI-Spec.md`: 页面、组件、交互、Design Token、权限可见性、终端适配
- `docs/03-Architecture-Spec.md`: 系统边界、技术选型、权限模型、安全设计、部署架构、开源方案评估
- `docs/04-Acceptance-Criteria.md`: 模块级正常/异常/边界/权限/非功能验收和验收结果记录
- `docs/05-Decision-Log.md`: 已确认的关键决策
- `docs/06-Open-Questions.md`: 未决问题和阻塞项

支撑文档：

- `docs/User-Flows.md`: 核心业务流程、角色路径、异常流程、状态转换
- `docs/API-and-Data-Spec.md`: 数据实体、接口、权限、集成、数据生命周期

## 开发就绪规则

只有当 MVP 范围、核心流程、UI 状态、权限模型、业务对象、数据集成、技术架构和验收合同均明确后，才开始实现。
