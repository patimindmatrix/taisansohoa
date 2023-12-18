from fastapi import APIRouter, HTTPException
import uuid
import process
from models import DH
from process import dh as dh_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[DH])
async def get_all_dh():
    try:
        all_dh = dh_model.get_all_dh()  # Replace this with your actual function to fetch all NV
        return all_dh
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/", response_model=DH)
async def create_dh(dh: DH):
    dh.MADH = str(uuid.uuid4())  # Generate a unique ID
    create_dh = dh_model.create_dh(dh)
    if create_dh:
        return create_dh
    raise HTTPException(status_code=500, detail="Error creating DH")


@router.get("/{madh}", response_model=DH)
async def read_dh(madh: str):
    dh = dh_model.get_dh(madh)
    if dh:
        return dh
    raise HTTPException(status_code=404, detail="DH not found")


@router.put("/{madh}", response_model=DH)
async def update_dh(madh: str, dh: DH):
    update_dh = dh_model.update_dh(madh, dh)
    if update_dh:
        return update_dh
    raise HTTPException(status_code=404, detail="DH not found")


@router.delete("/{madh}", response_model=DH)
async def delete_dh(madh: str):
    delete_dh = dh_model.delete_dh(madh)
    if delete_dh:
        return delete_dh
    raise HTTPException(status_code=404, detail="DH not found")
