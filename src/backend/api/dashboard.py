from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.backend.core.database import get_db
from src.backend.models.task import Task
from src.backend.schemas.dashboard import DashboardStats
from src.backend.schemas.response import BaseResponse
import logging

router = APIRouter(prefix="/dashboard", tags=["dashboard"])
logger = logging.getLogger(__name__)

@router.get("/stats", response_model=BaseResponse[DashboardStats])
async def get_dashboard_stats(owner_id: int, db: Session = Depends(get_db)):
    """
    获取看板统计数据
    """
    try:
        # 获取总数、已完成数
        total = db.query(func.count(Task.id)).filter(Task.owner_id == owner_id).scalar() or 0
        completed = db.query(func.count(Task.id)).filter(
            Task.owner_id == owner_id, Task.completed == True
        ).scalar() or 0
        
        pending = total - completed
        rate = round((completed / total * 100), 2) if total > 0 else 0.0
        
        stats = DashboardStats(
            total_tasks=total,
            completed_tasks=completed,
            pending_tasks=pending,
            completion_rate=rate
        )
        
        return BaseResponse.success(data=stats)
    except Exception as e:
        logger.error(f"Get dashboard stats failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")
