from fastapi import FastAPI
from sqlalchemy.orm import Session
from app import crud, models, schemas
from app.api import users, job_categories
from app.database import SessionLocal, engine
from app.settings import settings

app = FastAPI()

app.include_router(users.router, tags=["users"])
app.include_router(job_categories.router, tags=["job_categories"])

#
# @app.on_event("startup")
# def startup_event():
#     models.Base.metadata.create_all(bind=engine)
#     db: Session = SessionLocal()
#     user = crud.get_user_by_email(db, settings.super_user_email)
#     if not user:
#         user_in = schemas.UserCreate(
#             email=settings.super_user_email, password=settings.super_user_password
#         )
#         crud.create_user(db, user_in)
#     db.close()


# @app.post("/login/access-token", response_model=schemas.Token)
# def login_access_token(
#     db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()
# ):
#     """
#     OAuth2 compatible token login, get an access token for future requests.
#     """
#     user = crud.authenticate_user(
#         db, email=form_data.username, password=form_data.password
#     )
#     if not user:
#         raise HTTPException(status_code=400, detail="Incorrect email or password")
#     return {
#         "access_token": security.create_access_token(subject=user.id),
#         "token_type": "bearer",
#     }
