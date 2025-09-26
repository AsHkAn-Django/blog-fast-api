from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import Response

from sqlalchemy.orm import Session

from app.db import schemas
from app.db.session import get_db
from app.cruds import crud_posts


router = APIRouter(prefix="/posts", tags=['posts'])


@router.post(
    "/",
    summary="Create a new post",
    description="This endpoint creates a new post item with a title and "
    "body which can take comments too.",
    response_model=schemas.PostResponse,
    status_code=201
)
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud_posts.create_post(db=db, post=post)


@router.get(
    "/",
    response_model=list[schemas.PostResponse],
    summary="Get post list",
    description="This endpoint brings the list of all the posts."
)
def list_post(db: Session = Depends(get_db)):
    return crud_posts.list_post(db=db)