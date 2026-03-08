from fastapi import FastAPI
from src.backend.api.auth import router as auth_router

app = FastAPI(title="AI Todo API")

# 包含路由
app.include_router(auth_router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Welcome to AI Todo API"}
