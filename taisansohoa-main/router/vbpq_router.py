from fastapi import APIRouter, HTTPException
import uuid
import process
from models import VBPQ
from process import vbpq as vbpq_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[VBPQ])
async def get_all_tl():
    try:
        all_vbpq = vbpq_model.get_all_vbpq()  # Replace this with your actual function to fetch all NV
        return all_vbpq
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
@router.post("/", response_model=VBPQ)
async def create_vbpq(vbpq: VBPQ):
    try:
        create_vbpq = vbpq_model.create_vbpq(vbpq)
        if create_vbpq:
            return create_vbpq
        raise HTTPException(status_code=500, detail="Error creating VBPQ")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{mavbpq}", response_model=VBPQ)
async def read_vbpq(mavbpq: str):
    try:
        vbpq = vbpq_model.get_vbpq(mavbpq)
        if vbpq:
            return vbpq
        raise HTTPException(status_code=404, detail="VBPQ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{mavbpq}", response_model=VBPQ)
async def update_vbpq(mavbpq: str, vbpq: VBPQ):
    try:
        update_vbpq = vbpq_model.update_vbpq(mavbpq, vbpq)
        if update_vbpq:
            return update_vbpq
        raise HTTPException(status_code=404, detail="VBPQ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{mavbpq}", response_model=VBPQ)
async def delete_vbpq(mavbpq: str):
    try:
        delete_vbpq = vbpq_model.delete_vbpq(mavbpq)
        if delete_vbpq:
            return delete_vbpq
        raise HTTPException(status_code=404, detail="VBPQ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")