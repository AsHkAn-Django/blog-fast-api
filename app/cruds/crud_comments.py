from sqlalchemy.orm import Session
from sqlalchemy import select
from app.db import schemas, models
from app.core.dependencies import get_current_user


def create_comment(db: Session, comment: schemas.CommentCreate):
    cm = models.Comment(
        body=comment.body,
        post_id=comment.post_id,
        owner_id=1
    )
    db.add(cm)
    db.commit()
    db.refresh(cm)
    return cm


def list_comment(db: Session):
    return db.query(models.Comment).all()
