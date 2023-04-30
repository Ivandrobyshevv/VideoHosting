from fastapi import FastAPI
from video.router import router as video_router

app = FastAPI()

app.include_router(router=video_router)
