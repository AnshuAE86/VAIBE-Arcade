from fastapi import APIRouter

router = APIRouter(prefix="/pages/login", tags=["pages"])

@router.get("/methods")
def login_methods():
    return {
        "email": True,
        "magic_link": True,
        "google": True,
        "discord": True,
        "wallet": True,
        "guest": True
    }
