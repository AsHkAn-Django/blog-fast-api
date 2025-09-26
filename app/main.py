from fastapi import FastAPI

from app.db.session import Base, engine
from app.routers import router_comments, router_posts, router_users
from app.core.config import settings


Base.metadata.create_all(bind=engine)
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG
)


app.include_router(router_posts.router)
app.include_router(router_comments.router)