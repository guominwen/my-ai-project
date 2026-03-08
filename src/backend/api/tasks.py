from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.backend.core.database import get_db
from src.backend.models.task import Task
from src.backend.schemas.task import TaskCreate, TaskRead, TaskUpdate
from src.backend.schemas.response import BaseResponse
import logging

router = APIRouter(prefix="/tasks", tags=["tasks"])
logger = logging.getLogger(__name__)

@router.post("/", response_model=BaseResponse[TaskRead])
async def create_task(task_in: TaskCreate, owner_id: int, db: Session = Depends(get_db)):
    """
    创建任务 (暂时手动传入 owner_id，后续集成 JWT 后从 token 获取)
    """
    try:
        new_task = Task(
            title=task_in.title,
            description=task_in.description,
            completed=task_in.completed,
            owner_id=owner_id
        )
        db.add(new_task)
        db.commit()
        db.refresh(new_task)
        return BaseResponse.success(data=new_task)
    except Exception as e:
        db.rollback()
        logger.error(f"Create task failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")

@router.get("/", response_model=BaseResponse[List[TaskRead]])
async def read_tasks(owner_id: int, db: Session = Depends(get_db)):
    """
    获取当前用户的所有任务
    """
    try:
        tasks = db.query(Task).filter(Task.owner_id == owner_id).all()
        return BaseResponse.success(data=tasks)
    except Exception as e:
        logger.error(f"Read tasks failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")

@router.put("/{task_id}", response_model=BaseResponse[TaskRead])
async def update_task(task_id: int, task_in: TaskUpdate, db: Session = Depends(get_db)):
    """
    更新任务
    """
    try:
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if not db_task:
            return BaseResponse.error(code=404, message="Task not found")
        
        update_data = task_in.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_task, key, value)
        
        db.commit()
        db.refresh(db_task)
        return BaseResponse.success(data=db_task)
    except Exception as e:
        db.rollback()
        logger.error(f"Update task failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")

@router.delete("/{task_id}", response_model=BaseResponse[bool])
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    """
    删除任务
    """
    try:
        db_task = db.query(Task).filter(Task.id == task_id).first()
        if not db_task:
            return BaseResponse.error(code=404, message="Task not found")
        
        db.delete(db_task)
        db.commit()
        return BaseResponse.success(data=True)
    except Exception as e:
        db.rollback()
        logger.error(f"Delete task failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")
