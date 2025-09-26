from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db import models, schemas
from app.core.dependencies import get_current_user


def create_post(db: Session, post: schemas.PostCreate):
    ps = models.Post(
        title=post.title,
        body=post.body,
        owner_id=1
    )
    db.add(ps)
    db.commit()
    db.refresh(ps)
    return ps


def list_post(db: Session):
    return db.query(models.Post).all()
