from fastapi import FastAPI
from src.backend.api.auth import router as auth_router
from src.backend.api.tasks import router as task_router
from src.backend.api.dashboard import router as dashboard_router
from src.backend.core.database import engine, Base
# 导入模型以确保 Base 知道它们的存在
from src.backend.models.user import User
from src.backend.models.task import Task

# 创建数据库表 (在实际生产环境中建议使用 Alembic 迁移)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Todo API")

# 包含路由
app.include_router(auth_router, prefix="/api/v1")
app.include_router(task_router, prefix="/api/v1")
app.include_router(dashboard_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to AI Todo API"}
