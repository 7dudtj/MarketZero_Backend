from beanie import init_beanie, PydanticObjectId
from motor.motor_asyncio import AsyncIOMotorClient
from typing import Any, List, Optional
from pydantic import BaseSettings, BaseModel

from models.users import User
from models.items import Item


class Database:
    # 초기화 시 모델을 인수로 받음
    def __init__(self, model):
        self.model = model
    
    # 레코드 하나를 데이터베이스 컬렉션에 추가
    async def save(self, document) -> None:
        await document.create()
        return
    
    # 데이터베이스 컬렉션에서 단일 레코드 불러오기
    async def get(self, id: PydanticObjectId) -> Any:
        doc = await self.model.get(id)
        if doc:
            return doc
        return False
    
    # 데이터베이스 컬렉션에서 전체 레코드 불러오기
    async def get_all(self) -> List[Any]:
        docs = await self.model.find_all().to_list()
        return docs
    
    # 기존 레코드 변경
    async def update(self, id: PydanticObjectId, body: BaseModel) -> Any:
        doc_id = id
        des_body = body.dict()
        des_body = {k:v for k, v in des_body.items() if v is not None}
        update_query = {"$set": {
            field: value for field, value in des_body.items()
        }}
        
        doc = await self.get(doc_id)
        if not doc:
            return False
        await doc.update(update_query)
        return doc
    
    # 데이터베이스에서 레코드를 삭제
    async def delete(self, id: PydanticObjectId) -> bool:
        doc = await self.get(id)
        if not doc:
            return False
        await doc.delete()
        return True


class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    
    async def initialize_database(self):
        client = AsyncIOMotorClient(self.DATABASE_URL)
        await init_beanie(database=client.get_default_database(), 
                            document_models=[Item, User])
        
    class Config:
        env_file = ".env.prod"