from pydantic import BaseModel, EmailStr, Field, ConfigDict

class UserRegister(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=6)

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    username: str
    email: str

class UserLogin(BaseModel):
    account: str  # 可以是用户名或邮箱
    password: str
