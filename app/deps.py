from fastapi.security import OAuth2PasswordBearer

from .database import SessionLocal

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl="/login/access-token")


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()