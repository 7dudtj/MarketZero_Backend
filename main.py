import uvicorn
from fastapi import FastAPI
from database.connection import Settings

from routes.items import item_router
from routes.users import user_router

app = FastAPI()
settings = Settings()

# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(item_router, prefix="/item")

# 어플리케이션 실행 시 몽고DB 초기화
@app.on_event("startup")
async def init_db():
    await settings.initialize_database()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
