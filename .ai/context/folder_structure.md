# 项目目录结构 (Folder Structure)

所有代码开发必须严格遵循以下目录结构，严禁在根目录或非指定目录下创建新文件：

```text
src/
├── backend/            # FastAPI 后端代码 (Python)
│   ├── main.py         # 应用入口
│   ├── api/            # 路由定义 (Routes)
│   ├── models/         # 数据库模型 (SQLAlchemy/Pydantic)
│   ├── schemas/        # 数据传输对象 (DTOs)
│   ├── services/       # 业务逻辑层
│   ├── core/           # 配置与核心功能
│   └── tests/          # 后端 pytest 测试
└── frontend/           # Next.js 前端代码 (TypeScript/React)
    ├── app/            # App Router (页面与路由)
    ├── components/     # 公共组件
    ├── lib/            # 工具函数与 API 客户端
    ├── hooks/          # 自定义 React Hooks
    └── types/          # TypeScript 类型定义

.ai/                    # AI 自动开发系统配置
├── agents/             # Agent 角色定义
├── context/            # 项目上下文规则
├── memory/             # 决策与审计日志
├── tasks/              # 任务管理 (Backlog/Current/Completed)
└── workflow/           # 自动化工作流定义
```

## 强制规则
1. **禁止在根目录创建 Python/TS 文件**：所有代码必须位于 `src/`。
2. **测试隔离**：后端测试必须放在 `src/backend/tests/`。
3. **前端规范**：遵循 Next.js App Router 的目录约定。
