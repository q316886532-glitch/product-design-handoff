# Product Design Handoff Skill

一个用于 Codex 的产品设计移交 skill：把模糊产品想法、早期需求或已有文档，逐步整理成可交给编码智能体开发的产品文档包。

## 适合场景

- 你只有一个模糊产品想法，需要先澄清定位、用户和 MVP 范围。
- 你已有部分需求文档，希望整理成 PRD、UI Spec、Architecture Spec 和验收标准。
- 你想让 Codex 在开发前先建立稳定的产品上下文，减少边聊边改造成的需求漂移。

## 核心能力

- 输入归纳：提取已知事实、隐含假设、冲突点、风险和缺失决策。
- 产品定位：确认产品解决什么问题、服务哪些用户、带来什么收益。
- 文档脚手架：生成编号文档包，包括 Product Context、PRD、UI Spec、Architecture Spec、Acceptance Criteria 等。
- 横切关注点：跨文档跟踪权限模型、业务对象、数据集成。
- 开发就绪检查：在编码前确认需求、交互、数据、架构和验收标准足够明确。

## 仓库内容

- `product-design-handoff-skill-2026-05-17.zip`：完整 skill 压缩包，可直接交给编码智能体解析。
- 解压后得到 `product-design-handoff/`，这是可安装的 Codex skill 目录。

## 安装方式

将 `product-design-handoff/` 目录放入你的 Codex skills 目录，例如：

```bash
~/.codex/skills/product-design-handoff
```

或者解压 zip 后，把其中的 `product-design-handoff` 文件夹复制到 Codex skills 目录。

## 使用方式

在 Codex 中这样调用：

```text
使用 $product-design-handoff，帮我把下面这个产品想法设计到可以交给 Codex 开发：

我想做一个……
```

基于已有文档也可以：

```text
使用 $product-design-handoff，基于这些文档整理产品定位、需求、UI、架构和验收标准：
/path/to/idea.md
/path/to/research.md
```

## 初始化项目文档包

```bash
python3 product-design-handoff/scripts/init_product_workspace.py /path/to/project --project-name "项目名"
```

默认不会覆盖已有文件。想预览将生成的文件：

```bash
python3 product-design-handoff/scripts/init_product_workspace.py /path/to/project --project-name "项目名" --dry-run
```

## 默认文档结构

```text
docs/00-Product-Context.md
docs/01-PRD.md
docs/02-UI-Spec.md
docs/03-Architecture-Spec.md
docs/04-Acceptance-Criteria.md
docs/05-Decision-Log.md
docs/06-Open-Questions.md
docs/User-Flows.md
docs/API-and-Data-Spec.md
AGENTS.md
README.md
```

## 语言

文档正文默认中文，文件名保持英文，便于人类阅读和编码智能体解析。
