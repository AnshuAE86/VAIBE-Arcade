from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.auth.routes import router as auth_router
from app.api.v1.profile.routes import router as profile_router

app = FastAPI(title="VAIBE Arcade API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(profile_router, prefix="/api/v1")

@app.get("/")
def health():
    return {"status": "ok"}
