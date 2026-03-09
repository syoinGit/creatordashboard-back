from fastapi import FastAPI
from app.api import media_assets

app = FastAPI()

app.include_router(media_assets.router)