from fastapi import APIRouter, HTTPException
import uuid
import process
from models import VBPQ

router = APIRouter()


@router.post("/", response_model=VBPQ)
async def create_vbpq(vbpq: VBPQ):
    try:
        vbpq.MAVBPQ = str(uuid.uuid4())  # Generate a unique ID
        create_vbpq = process.create_vbpq(vbpq)
        if create_vbpq:
            return create_vbpq
        raise HTTPException(status_code=500, detail="Error creating VBPQ")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{mavbpq}", response_model=VBPQ)
async def read_vbpq(mavbpq: str):
    try:
        vbpq = process.get_vbpq(mavbpq)
        if vbpq:
            return vbpq
        raise HTTPException(status_code=404, detail="VBPQ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{mavbpq}", response_model=VBPQ)
async def update_vbpq(mavbpq: str, vbpq: VBPQ):
    try:
        update_vbpq = process.update_vbpq(mavbpq, vbpq)
        if update_vbpq:
            return update_vbpq
        raise HTTPException(status_code=404, detail="VBPQ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{mavbpq}", response_model=VBPQ)
async def delete_vbpq(mavbpq: str):
    try:
        delete_vbpq = process.delete_vbpq(mavbpq)
        if delete_vbpq:
            return delete_vbpq
        raise HTTPException(status_code=404, detail="VBPQ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")