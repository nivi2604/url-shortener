from fastapi import FastAPI, Request, HTTPException

from app.database import engine
from app.models import URL
from app.routes.url_routes import router
from app.core.config import r, check_rate_limit
from app.core.config import check_rate_limit, r
app = FastAPI()

URL.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "URL Shortener Running 🚀"}


# 🔥 THIS LINE FIXES YOUR ISSUE
app.include_router(router)