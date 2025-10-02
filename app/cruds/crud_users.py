from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.db import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    us = models.User(
        username=user.username,
        email = user.email,
        hashed_password=user.hashed_password
    )
    db.add(us)
    db.commit()
    db.refresh(us)
    return us
