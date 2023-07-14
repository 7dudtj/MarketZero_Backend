import uvicorn
from fastapi import FastAPI

from routes.items import item_router
from routes.users import user_router

app = FastAPI()

# 라우트 등록
app.include_router(user_router, prefix="/user")
app.include_router(item_router, prefix="/item")

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
