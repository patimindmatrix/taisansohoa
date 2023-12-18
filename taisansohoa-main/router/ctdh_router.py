from fastapi import APIRouter, HTTPException
import uuid
import process
from models import CTDH
from process import ctdh as ctdh_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[CTDH])
async def get_all_ctdh():
    try:
        all_ctdh = ctdh_model.get_all_ctdh()  # Replace this with your actual function to fetch all NV
        return all_ctdh
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/", response_model=CTDH)
async def create_ctdh(ctdh: CTDH):
    create_ctdh = ctdh_model.create_ctdh(ctdh)
    if create_ctdh:
        return create_ctdh
    raise HTTPException(status_code=500, detail="Error creating CTDH")


@router.get("/{mactdh}", response_model=CTDH)
async def read_ctdh(mactdh: str):
    ctdh = ctdh_model.get_ctdh(mactdh)
    if ctdh:
        return ctdh
    raise HTTPException(status_code=404, detail="CTDH not found")


@router.put("/{mactdh}", response_model=CTDH)
async def update_ctdh(mactdh: str, ctdh: CTDH):
    update_ctdh = ctdh_model.update_ctdh(mactdh, ctdh)
    if update_ctdh:
        return update_ctdh
    raise HTTPException(status_code=404, detail="CTDH not found")


@router.delete("/{mactdh}", response_model=CTDH)
async def delete_ctdh(mactdh: str):
    delete_ctdh = ctdh_model.delete_ctdh(mactdh)
    if delete_ctdh:
        return delete_ctdh
    raise HTTPException(status_code=404, detail="CTDH not found")
