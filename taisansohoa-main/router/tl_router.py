from fastapi import APIRouter, HTTPException
import uuid
import process
from models import TL
from process import tl as tl_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[TL])
async def get_all_tl():
    try:
        all_tl = tl_model.get_all_tl()  # Replace this with your actual function to fetch all NV
        return all_tl
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/", response_model=TL)
async def create_tl(tl: TL):
    try:
        create_tl = tl_model.create_tl(tl)
        if create_tl:
            return create_tl
        raise HTTPException(status_code=500, detail="Error creating TL")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{matl}", response_model=TL)
async def read_tl(matl: str):
    try:
        tl = tl_model.get_tl(matl)
        if tl:
            return tl
        raise HTTPException(status_code=404, detail="TL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{matl}", response_model=TL)
async def update_tl(matl: str, tl: TL):
    try:
        update_tl = tl_model.update_tl(matl, tl)
        if update_tl:
            return update_tl
        raise HTTPException(status_code=404, detail="TL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{matl}", response_model=TL)
async def delete_tl(matl: str):
    try:
        delete_tl = tl_model.delete_tl(matl)
        if delete_tl:
            return delete_tl
        raise HTTPException(status_code=404, detail="TL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")