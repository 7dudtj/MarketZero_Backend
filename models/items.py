from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    price: int

    class Config:
        json_schema_extra = {
            "example": {
                "title": "롯데칠성음료 펩시제로슈거 라임향 355ml",
                "image": "https://shopping-phinf.pstatic.net/main_3374125/33741256619.20220728160715.jpg?type=f640",
                "description": "사람들이 선호하는 대표적인 zero 음료입니다.",
                "tags": ["recommend", "zero-sugar"],
                "price": 310,
            }
        }
