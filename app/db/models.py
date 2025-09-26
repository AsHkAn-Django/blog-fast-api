from sqlalchemy import (
    Column, Integer, String, ForeignKey, Text, DateTime, func, Boolean, JSON
)
from sqlalchemy.orm import relationship

from app.db.session import Base


class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())


class User(TimestampMixin, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    # Relationship (backref to ...)
    posts = relationship("Post", back_populates="owner", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="owner", cascade="all, delete-orphan")


class Post(TimestampMixin, Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String(250), nullable=False)
    body = Column(Text, nullable=False)

    # ForeignKey column (like Djnago's models.ForeginKey)
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    # Relationship (points back to ...)
    owner = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class Comment(TimestampMixin, Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    body = Column(Text, nullable=False)

    # ForeignKey column
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))

    # Relationship
    post = relationship("Post", back_populates="comments")
    owner = relationship("User", back_populates="comments")