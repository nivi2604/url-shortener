from app.database import SessionLocal
from app.models import URL
from app.utils.helpers import generate_code
from datetime import datetime, timedelta

def create_short_url(data):
    db = SessionLocal()

    url = data.get("url")
    custom_code = data.get("custom_code")
    expiry_minutes = data.get("expiry_minutes")

    # 🔹 Handle custom code
    if custom_code:
        existing = db.query(URL).filter(URL.short_code == custom_code).first()
        if existing:
            return None, "Custom code already taken"
        code = custom_code
    else:
        # 🔹 Generate unique code
        while True:
            code = generate_code()
            existing = db.query(URL).filter(URL.short_code == code).first()
            if not existing:
                break

    # 🔹 Expiry logic
    expires_at = None
    if expiry_minutes:
        expires_at = datetime.utcnow() + timedelta(minutes=expiry_minutes)

    new_url = URL(
        short_code=code,
        original_url=url,
        expires_at=expires_at
    )

    db.add(new_url)
    db.commit()

    return code, None


def get_url(code):
    db = SessionLocal()
    return db.query(URL).filter(URL.short_code == code).first()

