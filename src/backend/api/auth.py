from fastapi import APIRouter
from src.backend.schemas.user import UserRegister, UserRead, UserLogin
from src.backend.schemas.response import BaseResponse
import logging

router = APIRouter(prefix="/auth", tags=["auth"])
logger = logging.getLogger(__name__)

# 临时内存数据库 (In-memory storage)
users_db = []
user_id_counter = 1

@router.post("/register", response_model=BaseResponse[UserRead])
async def register(user_in: UserRegister):
    global user_id_counter
    
    try:
        # 检查用户名和邮箱是否已存在
        if any(u["username"] == user_in.username for u in users_db):
            return BaseResponse.error(code=400, message="Username already registered")
        if any(u["email"] == user_in.email for u in users_db):
            return BaseResponse.error(code=400, message="Email already registered")
        
        # 创建新用户
        new_user = {
            "id": user_id_counter,
            "username": user_in.username,
            "email": user_in.email,
            "password": user_in.password  # 注意：实际项目中必须加盐哈希存储
        }
        users_db.append(new_user)
        user_id_counter += 1
        
        return BaseResponse.success(data=UserRead(**new_user))
    except Exception as e:
        logger.error(f"Register failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")

@router.post("/login", response_model=BaseResponse[UserRead])
async def login(user_in: UserLogin):
    try:
        # 查找用户（通过用户名或邮箱）
        user = next((u for u in users_db if u["username"] == user_in.account or u["email"] == user_in.account), None)
        
        if not user or user["password"] != user_in.password:
            return BaseResponse.error(code=401, message="Invalid account or password")
        
        return BaseResponse.success(data=UserRead(**user))
    except Exception as e:
        logger.error(f"Login failed: {str(e)}")
        return BaseResponse.error(code=500, message="Internal Server Error")
