from typing import List, Optional

from pydantic import BaseModel, EmailStr

from models.items import Item


class User(BaseModel):
    email: EmailStr
    password: str
    items: Optional[List[Item]]

    class Config:
        json_schema_extra = {
            "example": {
                "email": "7dudtj@naver.com",
                "password": "helloworld",
                "items": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "7dudtj@naver.com",
                "password": "helloworld",
                "items": [],
            }
        }
