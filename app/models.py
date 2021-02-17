import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    is_active = Column(Boolean, default=True)
    categories = relationship("JobCategory", back_populates="owner")
    created_date = Column(DateTime, default=datetime.datetime.utcnow)


class JobCategory(Base):
    __tablename__ = "job_categories"

    id = Column(Integer, primary_key=True, index=True)
    category = Column(String, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    created_date = Column(DateTime, default=datetime.datetime.utcnow)

    owner = relationship("User", back_populates="categories")