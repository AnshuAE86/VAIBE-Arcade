from fastapi import APIRouter
from app.api.v1.auth.routes import router as auth_router
from app.api.v1.pages.login import router as login_page_router

api_router = APIRouter(prefix="/api/v1")

api_router.include_router(auth_router)
api_router.include_router(login_page_router)
