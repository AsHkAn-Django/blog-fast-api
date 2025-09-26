from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response

from sqlalchemy.orm import Session

from app.db import schemas
from app.db.session import get_db
from app.cruds import crud_comments


router = APIRouter(prefix="/comments", tags=['comments'])


@router.post(
    "/",
    summary="Create a new comment",
    description="Creates a new comment for a post by a user.",
    response_model=schemas.CommentResponse,
    status_code=201
)
def create_comment(comment: schemas.CommentCreate, db: Session = Depends(get_db)):
    return crud_comments.create_comment(comment=comment, db=db)


@router.get(
    "/",
    response_model=list[schemas.CommentResponse],
    summary="Get comment list",
    description="This endpoint brings the list of all the comments"
)
def list_comment(db:Session = Depends(get_db)):
    return crud_comments.list_comment(db=db)