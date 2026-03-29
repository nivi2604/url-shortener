from sqlalchemy import Column, Integer, String, DateTime
from app.database import Base

class URL(Base):
    __tablename__ = "urls"

    id = Column(Integer, primary_key=True, index=True)
    short_code = Column(String, unique=True, index=True)
    original_url = Column(String)
    clicks = Column(Integer, default=0)
    expires_at = Column(DateTime, nullable=True)  # 🔥 NEW