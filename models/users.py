from typing import List, Optional
from beanie import Document, Link
from pydantic import EmailStr, BaseModel
from models.items import Item


# 회원 정보
class User(Document):
    email: EmailStr  # 회원 email
    password: str  # 회원 비밀번호
    items: Optional[List[Item]]  # 회원의 아이템 목록. 추후 결정

    class Config:
        json_schema_extra = {
            "example": {
                "email": "7dudtj@naver.com",
                "password": "helloworld",
                "items": [],
            }
        }
        
    class Settings:
        name = "users"


# 회원가입 정보
class UserSignIn(BaseModel):
    email: EmailStr  # 회원 email
    password: str  # 회원 비밀번호

    class Config:
        json_schema_extra = {
            "example": {
                "email": "7dudtj@naver.com",
                "password": "helloworld",
            }
        }
