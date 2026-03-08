# 技术栈 (Tech Stack)

## 核心开发环境
- **后端 (Backend)**: Python 3.10+
    - **框架**: [FastAPI](https://fastapi.tiangolo.com/)
    - **测试**: [pytest](https://docs.pytest.org/)
- **前端 (Frontend)**: [Next.js](https://nextjs.org/) (TypeScript)
- **数据库 (Database)**: [MySQL](https://www.mysql.com/) (Version 8.0.45)
    - **ID**: `root`
    - **PW**: `root`

## 开发约束
1. **API 开发**:
    - 必须严格遵循 `api_style.md` 定义的响应格式。
    - 每一个新增的 API 必须附带对应的 `pytest` 测试。
2. **代码质量**:
    - 必须通过静态检查 (`GetDiagnostics`)。
    - 遵循 `coding_rules.md`。
3. **Bug 修复**:
    - 修复前必须先阅读错误日志，并在修复后增加回归测试。
