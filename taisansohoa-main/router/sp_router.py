from fastapi import APIRouter, HTTPException
import uuid
import process
from models import SP
from process import sp as sp_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[SP])
async def get_all_sp():
    try:
        all_sp = sp_model.get_all_sp()  # Replace this with your actual function to fetch all NV
        return all_sp
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/", response_model=SP)
async def create_sp(sp: SP):
    try:
        create_sp = sp_model.create_sp(sp)
        if create_sp:
            return create_sp
        raise HTTPException(status_code=500, detail="Error creating SP")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{masp}", response_model=SP)
async def read_sp(masp: str):
    try:
        sp = sp_model.get_sp(masp)
        if sp:
            return sp
        raise HTTPException(status_code=404, detail="SP not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{masp}", response_model=SP)
async def update_sp(masp: str, sp: SP):
    try:
        update_sp = sp_model.update_sp(masp, sp)
        if update_sp:
            return update_sp
        raise HTTPException(status_code=404, detail="SP not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{masp}", response_model=SP)
async def delete_sp(masp: str):
    try:
        delete_sp = sp_model.delete_sp(masp)
        if delete_sp:
            return delete_sp
        raise HTTPException(status_code=404, detail="SP not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")