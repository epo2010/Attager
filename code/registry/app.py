# app.py
from fastapi import FastAPI
from routes import register, discover, unregister

app = FastAPI(title="Agent Registry")

# 라우터 등록
app.include_router(register.router)
app.include_router(discover.router)
app.include_router(unregister.router)

