# 系统架构 (System Architecture)

## 核心架构模式
- **前后端分离**: 采用标准的 C/S 架构，前端与后端通过 RESTful API 进行通信。
- **分层设计**: 遵循典型的三层架构（表现层、业务逻辑层、数据访问层）。

## 技术栈定义
- **前端 (Frontend)**: [Next.js](https://nextjs.org/) (React 框架)
- **后端 (Backend)**: [FastAPI](https://fastapi.tiangolo.com/) (Python 高性能 Web 框架)
- **数据库 (Database)**: [MySQL 8.0.45](https://www.mysql.com/)

## 数据流向
1. **用户请求**: 前端 Next.js 发起 API 请求。
2. **业务处理**: 后端 FastAPI 接收请求，执行 `services/` 中的业务逻辑。
3. **数据持久化**: 通过 SQLAlchemy ORM 与 MySQL 进行交互。
4. **响应返回**: 后端按照 `api_style.md` 规范返回 JSON 数据。