from pydantic import BaseModel, ConfigDict, EmailStr, Field
from typing import List, Optional, Dict, Annotated


# -------------- User -------------
class UserCreate(BaseModel):
    username: Annotated[
        str,
        Field(min_length=6, max_length=100, example="Killer94")
    ]
    email: EmailStr
    password: Annotated[str, Field(min_length=8)]


class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# ------------ Comment -----------
class CommentCreate(BaseModel):
    body: str
    post_id: int


class CommentResponse(BaseModel):
    id: int
    body: str
    post_id: int
    owner_id: int
    owner: Optional[UserOut] = None

    model_config = ConfigDict(from_attributes=True)


# ------------ Post -----------
class PostCreate(BaseModel):
    title: Annotated[str, Field(max_length=250)]
    body: str


class PostUpdate(PostCreate):
    pass


class PostResponse(BaseModel):
    id: int
    title: str
    body: str
    owner_id: int
    owner: Optional[UserOut] = None
    comments: List[CommentResponse] = []

    model_config = ConfigDict(from_attributes=True)


CommentCreate.model_rebuild()
UserOut.model_rebuild()
PostResponse.model_rebuild()
