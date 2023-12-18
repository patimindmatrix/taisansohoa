from fastapi import APIRouter, HTTPException
import uuid
import process
from models import HD
from process import hd as hd_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[HD])
async def get_all_hd():
    try:
        all_hd = hd_model.get_all_hd()  # Replace this with your actual function to fetch all NV
        return all_hd
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/", response_model=HD)
async def create_hd(hd: HD):
    create_hd = hd_model.create_hd(hd)
    if create_hd:
        return create_hd
    raise HTTPException(status_code=500, detail="Error creating HĐ")


@router.get("/{mahd}", response_model=HD)
async def read_hd(mahd: str):
    hd = hd_model.get_hd(mahd)
    if hd:
        return hd
    raise HTTPException(status_code=404, detail="HĐ not found")


@router.put("/{mahd}", response_model=HD)
async def update_hd(mahd: str, hd: HD):
    update_hd = hd_model.update_hd(mahd, hd)
    if update_hd:
        return update_hd
    raise HTTPException(status_code=404, detail="HĐ not found")


@router.delete("/{mahd}", response_model=HD)
async def delete_hd(mahd: str):
    delete_hd = hd_model.delete_hd(mahd)
    if delete_hd:
        return delete_hd
    raise HTTPException(status_code=404, detail="HĐ not found")
