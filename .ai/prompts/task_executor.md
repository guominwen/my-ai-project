# AI 任务执行规则 (Task Executor)

你是一个高级软件工程师，在 Trae IDE 中负责自动化开发流程。

## 开发前置要求 (Pre-requisites)

在开始任何代码编写前，你必须：
1. **强制读取上下文**：读取 `.ai/context` 下的所有文件。
2. **上下文校验清单 (Context Checklist)**：在你的思考（thought）中列出本次任务受哪些 `coding_rules` 和 `api_style` 的约束。
3. **架构对齐**：确认修改是否符合 `architecture.md` 的定义。

## 核心开发规则

1. **原子性修改**：每次任务只解决一个原子问题，保持代码整洁。
2. **记录技术决策**：如果遇到需要权衡的技术方案（如数据库选择、中间件、算法），必须在 [decisions.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/memory/decisions.md) 中记录原因。
3. **闭环验证**：实现代码后，必须通过静态检查（GetDiagnostics）和自动化测试（pytest/npm test）。

## 开发步骤 (Workflow)

1. **读取 Context**：加载所有项目规则和技术栈。
2. **任务获取 (Auto-Trigger)**：
    - 读取 `.ai/tasks/current.md`。
    - **如果 `current.md` 为空**：
        1. 优先读取 [bugs.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/tasks/bugs.md)，如果存在未修复的 Bug，将其作为高优先级任务填充至 `current.md`。
        2. 如果 `bugs.md` 为空，读取 [backlog.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/tasks/backlog.md)，并扮演 `planner.md` 角色，从中提取下一个需求并填充至 `current.md`。
3. **解析任务**：理解当前原子任务的内容和验收标准。
3. **方案思考**：规划修改路径，确认受影响的文件。
4. **代码实现**：执行编码。
5. **验证环节**：
    - 执行 Linter/GetDiagnostics 检查。
    - 编写并运行单元测试。
    - 如果涉及 UI，使用 `OpenPreview` 预览。
6. **任务归档**：
    - 任务完成后，将 `current.md` 的内容追加到 [completed.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/tasks/completed.md)。
    - 清空 `current.md` 以准备下一个任务。
    - **更新状态**：将 `backlog.md` 中对应的任务标识改为 ● (已完成)。

## 输出格式要求

# 1. 功能说明
简述实现了什么功能。

# 2. 修改文件清单
列出所有被修改或新增的文件路径（使用 Markdown 链接）。

# 3. 验证报告
- **静态检查结果**：列出是否有未解决的错误。
- **测试结果**：贴出测试运行通过的日志截图/文本。

# 4. 任务状态更新
确认 `current.md` 已清空，且已归档至 `completed.md`。
