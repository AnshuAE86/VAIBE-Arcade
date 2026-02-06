from fastapi import APIRouter, Request, HTTPException
from app.db.supabase import supabase

router = APIRouter(prefix="/profile", tags=["profile"])

@router.get("/me")
def me(request: Request):
    jwt = request.cookies.get("sb-access-token")

    if not jwt:
        raise HTTPException(status_code=401, detail="Not authenticated")

    user = supabase.auth.get_user(jwt)

    return {
        "id": user.user.id,
        "email": user.user.email,
        "name": user.user.email.split("@")[0],
        "role": "player"
    }
