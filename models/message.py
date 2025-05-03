
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from ..database import Base

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    sender_email = Column(String, index=True)
    recipient_email = Column(String, index=True)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
