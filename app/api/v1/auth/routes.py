from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from app.core.config import settings

router = APIRouter(prefix="/auth", tags=["auth"])


# -------------------------
# EMAIL MAGIC LINK
# -------------------------
@router.get("/email")
def login_with_email(email: str = Query(...)):
    from app.db.supabase import supabase

    supabase.auth.sign_in_with_otp({
        "email": email,
        "options": {
            "email_redirect_to": settings.FRONTEND_URL
        }
    })

    return {"message": "Magic link sent"}


# -------------------------
# GOOGLE OAUTH
# -------------------------
@router.get("/google")
def login_google():
    url = (
        f"{settings.SUPABASE_URL}/auth/v1/authorize"
        f"?provider=google"
        f"&redirect_to={settings.FRONTEND_URL}"
    )
    return RedirectResponse(url)


# -------------------------
# DISCORD OAUTH
# -------------------------
@router.get("/discord")
def login_discord():
    url = (
        f"{settings.SUPABASE_URL}/auth/v1/authorize"
        f"?provider=discord"
        f"&redirect_to={settings.FRONTEND_URL}"
    )
    return RedirectResponse(url)
