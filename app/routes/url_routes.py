from fastapi import APIRouter, HTTPException, Request, Body
from fastapi.responses import RedirectResponse
from datetime import datetime

from app.services.url_service import create_short_url
from app.database import SessionLocal
from app.models import URL
from app.core.config import check_rate_limit, r   


router = APIRouter()


@router.post("/shorten")
def shorten_url(request: Request, data: dict = Body(...)):
    check_rate_limit(request)

    code, error = create_short_url(data)

    if error:
        raise HTTPException(status_code=400, detail=error)

    return {
        "short_url": f"http://127.0.0.1:8000/{code}"
    }


@router.get("/{code}")
def redirect_url(code: str):
    db = SessionLocal()

    url_entry = db.query(URL).filter(URL.short_code == code).first()

    if not url_entry:
        raise HTTPException(status_code=404, detail="URL not found")

    if url_entry.expires_at and datetime.utcnow() > url_entry.expires_at:
        raise HTTPException(status_code=410, detail="Link expired")

    url_entry.clicks += 1
    db.commit()

    return RedirectResponse(url=url_entry.original_url)


@router.get("/stats/{code}")
def get_stats(code: str):
    db = SessionLocal()

    url_entry = db.query(URL).filter(URL.short_code == code).first()

    if url_entry:
        return {
            "original_url": url_entry.original_url,
            "clicks": url_entry.clicks
        }
    else:
        raise HTTPException(status_code=404, detail="URL not found")