from fastapi import APIRouter, HTTPException
import uuid
import process
from models import KH
from process import kh as kh_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[KH])
async def get_all_kh():
    try:
        all_kh = kh_model.get_all_kh()  # Replace this with your actual function to fetch all NV
        return all_kh
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
@router.post("/", response_model=KH)
async def create_kh(kh: KH):
    try:
        created_kh = kh_model.create_kh(kh)
        if created_kh:
            return created_kh
        raise HTTPException(status_code=500, detail="Error creating KH")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{makh}", response_model=KH)
async def read_kh(makh: str):
    try:
        kh = kh_model.get_kh(makh)
        if kh:
            return kh
        raise HTTPException(status_code=404, detail="KH not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{makh}", response_model=KH)
async def update_kh(makh: str, kh: KH):
    try:
        update_kh = kh_model.update_kh(makh, kh)
        if update_kh:
            return update_kh
        raise HTTPException(status_code=404, detail="KH not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{makh}", response_model=KH)
async def delete_kh(makh: str):
    try:
        delete_kh = kh_model.delete_kh(makh)
        if delete_kh:
            return delete_kh
        raise HTTPException(status_code=404, detail="KH not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")