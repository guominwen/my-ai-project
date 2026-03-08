from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

T = TypeVar("T")

class BaseResponse(BaseModel, Generic[T]):
    code: int = 0
    message: str = "success"
    data: Optional[T] = None

    @classmethod
    def success(cls, data: Any = None, message: str = "success"):
        return cls(code=0, message=message, data=data)

    @classmethod
    def error(cls, code: int = 1, message: str = "error", data: Any = None):
        return cls(code=code, message=message, data=data)
