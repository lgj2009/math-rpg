"""POST /api/auth/register, /login, /logout, GET /me"""
from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel, Field
from services import auth_service

router = APIRouter(prefix="/api/auth", tags=["auth"])


class RegisterBody(BaseModel):
    email: str = Field(..., min_length=3, max_length=100)
    username: str = Field(..., min_length=1, max_length=30)
    password: str = Field(..., min_length=4, max_length=100)


class LoginBody(BaseModel):
    email: str
    password: str


@router.post("/register")
def register(body: RegisterBody):
    result = auth_service.register(body.email.strip(), body.username.strip(), body.password)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result


@router.post("/login")
def login(body: LoginBody):
    result = auth_service.login(body.email.strip(), body.password)
    if "detail" in result:
        raise HTTPException(401, result["detail"])
    return result


@router.post("/logout")
def logout(authorization: str = Header(None)):
    token = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:]
    if token:
        auth_service.logout(token)
    return {"ok": True}


class ForgotBody(BaseModel):
    email: str


class ResetPasswordBody(BaseModel):
    token: str
    new_password: str = Field(..., min_length=4, max_length=100)


@router.post("/forgot-password")
def forgot_password(body: ForgotBody):
    """Initiate password reset — sends email with reset link."""
    result = auth_service.forgot_password(body.email.strip())
    return result


@router.post("/reset-password")
def reset_password(body: ResetPasswordBody):
    """Complete password reset with token from email."""
    result = auth_service.reset_password(body.token, body.new_password)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result


class ChangePasswordBody(BaseModel):
    old_password: str
    new_password: str = Field(..., min_length=4, max_length=100)


@router.post("/change-password")
def change_password(body: ChangePasswordBody, authorization: str = Header(None)):
    token = authorization[7:] if authorization and authorization.startswith("Bearer ") else None
    if not token:
        raise HTTPException(401, "Not authenticated")
    user = auth_service.validate_session(token)
    if not user:
        raise HTTPException(401, "Invalid session")
    result = auth_service.change_password(user["user_id"], body.old_password, body.new_password)
    if "detail" in result:
        raise HTTPException(400, result["detail"])
    return result


@router.get("/me")
def me(authorization: str = Header(None)):
    token = None
    if authorization and authorization.startswith("Bearer "):
        token = authorization[7:]
    if not token:
        raise HTTPException(401, "Not authenticated")
    user = auth_service.validate_session(token)
    if not user:
        raise HTTPException(401, "Invalid or expired session")
    # Include full player data
    from services.player_service import get_player
    player = get_player(user["player_id"])
    return {**user, "player": player}
