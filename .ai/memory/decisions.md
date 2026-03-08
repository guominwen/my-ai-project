# 技术决策记录 (Technical Decisions)

## 2026-03-08: 数据库选型由 PostgreSQL 变更为 MySQL (8.0.45)
- **决策**: 将项目数据库由 PostgreSQL 更改为 MySQL (Version 8.0.45)。
- **原因**: 用户环境使用 MySQL，需适配现有环境。
- **凭据**: ID `root`, PW `root`。
- **影响**: 后续 SQLAlchemy 配置需使用 `mysql+pymysql` 驱动。

## 2026-03-08: 初始用户存储方案
- **决策**: 使用内存列表 (`users_db`) 作为临时存储。
- **原因**: 当前处于系统初始化阶段，尚未配置 PostgreSQL 数据库。
- **影响**: 重启应用后数据会丢失，后续任务（如用户登录）需依赖同一运行实例。
- **后续计划**: 在数据库集成任务中迁移至 SQLAlchemy + PostgreSQL。
