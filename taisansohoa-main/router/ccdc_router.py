from fastapi import APIRouter, HTTPException
import uuid
import process
from models import CCDC
from process import ccdc as ccdc_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[CCDC])
async def get_all_ccdc():
    try:
        all_ccdc = ccdc_model.get_all_ccdc()  # Replace this with your actual function to fetch all NV
        return all_ccdc
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/", response_model=CCDC)
async def create_ccdc(ccdc: CCDC):
    create_ccdc = ccdc_model.create_ccdc(ccdc)
    if create_ccdc:
        return create_ccdc
    raise HTTPException(status_code=500, detail="Error creating CCDC")


@router.get("/{maccdc}", response_model=CCDC)
async def read_tscd(maccdc: str):
    ccdc = ccdc_model.get_ccdc(maccdc)
    if ccdc:
        return ccdc
    raise HTTPException(status_code=404, detail="CCDC not found")


@router.put("/{maccdc}", response_model=CCDC)
async def update_ccdc(maccdc: str, ccdc: CCDC):
    update_ccdc = ccdc_model.update_ccdc(maccdc, ccdc)
    if update_ccdc:
        return update_ccdc
    raise HTTPException(status_code=404, detail="CCDC not found")


@router.delete("/{maccdc}", response_model=CCDC)
async def delete_ccdc(maccdc: str):
    delete_ccdc = ccdc_model.delete_ccdc(maccdc)
    if delete_ccdc:
        return delete_ccdc
    raise HTTPException(status_code=404, detail="CCDC not found")
