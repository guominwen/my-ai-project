from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.backend.schemas.user import UserRegister, UserRead, UserLogin
from src.backend.schemas.response import BaseResponse
from src.backend.core.database import get_db
from src.backend.models.user import User
import logging

router = APIRouter(prefix="/auth", tags=["auth"])
logger = logging.getLogger(__name__)

@router.post("/register", response_model=BaseResponse[UserRead])
async def register(user_in: UserRegister, db: Session = Depends(get_db)):
    try:
        # 检查用户名和邮箱是否已存在
        if db.query(User).filter(User.username == user_in.username).first():
            return BaseResponse.error(code=400, message="Username already registered")
        if db.query(User).filter(User.email == user_in.email).first():
            return BaseResponse.error(code=400, message="Email already registered")
        
        # 创建新用户
        new_user = User(
            username=user_in.username,
            email=user_in.email,
            password=user_in.password  # 注意：实际项目中必须加盐哈希存储
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return BaseResponse.success(data=new_user)
    except Exception as e:
        db.rollback()
        logger.error(f"Register failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")

@router.post("/login", response_model=BaseResponse[UserRead])
async def login(user_in: UserLogin, db: Session = Depends(get_db)):
    try:
        # 查找用户（通过用户名或邮箱）
        user = db.query(User).filter(
            (User.username == user_in.account) | (User.email == user_in.account)
        ).first()
        
        if not user or user.password != user_in.password:
            return BaseResponse.error(code=401, message="Invalid account or password")
        
        return BaseResponse.success(data=user)
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")
