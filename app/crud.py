from sqlalchemy.orm import Session
from typing import List

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    # hashed_password = security.get_password_hash(user.password)
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# def authenticate_user(db: Session, email: str, password: str):
#     user = get_user_by_email(db=db, email=email)
#     if not user:
#         return None
#     return user

def get_cats(db: Session, category: List[str]):
    return db.query(models.JobCategory).filter(models.JobCategory.category == category).all()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.JobCategory).offset(skip).limit(limit).all()


def create_user_category(db: Session, category: schemas.JobCategoryCreate, user_id: int):
    db_category = models.JobCategory(**category.dict(), owner_id=user_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category
