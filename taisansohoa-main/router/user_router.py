# user_router.py
from fastapi import APIRouter, HTTPException
from models import User
from process import user_auth

router = APIRouter()


@router.post("/register/")
async def register(user: User):
    user_auth.register(user.username, user.password)
    return {"message": "User registered successfully"}


@router.post("/login/")
async def login(user: User):
    try:
        if user_auth.login(user.username, user.password):
            return {"message": "Login successful."}
        else:
            raise HTTPException(
                status_code=401, detail="Incorrect username or password.")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")