from fastapi import APIRouter, HTTPException
import uuid
import process
from models import NV
from process import nv as nv_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[NV])
async def get_all_nv():
    try:
        all_nv = nv_model.get_all_nv()  # Replace this with your actual function to fetch all NV
        return all_nv
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/", response_model=NV)
async def create_nv(nv: NV):
    try:
        nv.MANV = str(uuid.uuid4())  # Generate a unique ID
        create_nv = nv_model.create_nv(nv)
        if create_nv:
            return create_nv
        raise HTTPException(status_code=500, detail="Error creating NV")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.get("/{manv}", response_model=NV)
async def read_nv(manv: str):
    try:
        nv = nv_model.get_nv(manv)
        if nv:
            return nv
        raise HTTPException(status_code=404, detail="NV not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{manv}", response_model=NV)
async def update_nv(manv: str, nv: NV):
    try:
        update_nv = nv_model.update_nv(manv, nv)
        if update_nv:
            return update_nv
        raise HTTPException(status_code=404, detail="NV not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{manv}", response_model=NV)
async def delete_nv(manv: str):
    try:
        delete_nv = nv_model.delete_nv(manv)
        if delete_nv:
            return delete_nv
        raise HTTPException(status_code=404, detail="NV not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")