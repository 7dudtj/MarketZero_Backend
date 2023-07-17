from typing import List, Optional

from pydantic import BaseModel, EmailStr

from models.items import Item


# 회원 정보
class User(BaseModel):
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


# 회원가입 정보
class UserSignIn(BaseModel):
    email: EmailStr  # 회원 email
    password: str  # 회원 비밀번호

    class Config:
        json_schema_extra = {
            "example": {
                "email": "7dudtj@naver.com",
                "password": "helloworld",
                "items": [],
            }
        }
