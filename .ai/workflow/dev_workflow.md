# AI 自动开发工作流 (Dev Workflow)

这是一个标准化的开发生命周期流程，旨在实现代码交付的闭环验证。

## 流程阶段 (Stages)

### 阶段 1: 规划 (Planning & Auto-Dispatch)
- **执行角色**: [planner.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/agents/planner.md)
- **任务**: 
    1. 扫描 [backlog.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/tasks/backlog.md)。
    2. 如果 `current.md` 为空，自动拆解最高优先级需求并填充 `current.md`。
    3. 更新 `backlog.md` 状态。

### 阶段 2: 开发 (Implementation)
- **执行角色**: [coder.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/agents/coder.md)
- **输入**: `current.md` 及项目上下文。
- **任务**: 
    1. 按照 `task_executor.md` 执行编码。
    2. 实现业务逻辑。
    3. **自检**: 执行 `GetDiagnostics` 修复语法错误。

### 阶段 3: 验证 (Verification)
- **执行角色**: [tester.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/agents/tester.md)
- **输入**: 被修改的代码。
- **任务**: 
    1. 使用 [test_writer.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/prompts/test_writer.md) 编写单元测试。
    2. 运行测试并确保 100% 通过。
    3. 如果是 UI 任务，执行冒烟测试并使用 `OpenPreview`。

### 阶段 4: 审查 (Review)
- **执行角色**: [reviewer.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/agents/reviewer.md)
- **输入**: 代码变更 (diff) + 测试报告。
- **任务**: 
    1. 检查代码是否符合 `coding_rules.md`。
    2. 评估架构设计是否符合 `architecture.md`。
    3. 生成 `review_report.md`。如有不通过项，打回“阶段 2”。

### 阶段 5: 归档 (Archive)
- **执行角色**: [task_executor.md](file:///c:/Users/63438/OneDrive/デスクトップ/guo/02_副業/my-project/.ai/prompts/task_executor.md)
- **任务**: 
    1. 将 `current.md` 追加到 `completed.md`。
    2. 清空 `current.md`。
    3. 更新 `backlog.md` 进度。
