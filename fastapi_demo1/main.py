from fastapi import FastAPI
from fastapi_demo1.routers.post import post_router
import uvicorn


app = FastAPI()
app.include_router(post_router)

