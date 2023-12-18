import uuid
from fastapi import APIRouter, HTTPException
from models import PB
import process
from process import pb as pb_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[PB])
async def get_all_pb():
    try:
        all_pb = pb_model.get_all_pb()  # Replace this with your actual function to fetch all NV
        return all_pb
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/", response_model=PB)
async def create_pb(pb: PB):
    try:
        created_pb = pb_model.create_pb(pb)
        if created_pb:
            return created_pb
        raise HTTPException(status_code=500, detail="Error creating PB")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{mapb}", response_model=PB)
async def get_pb( mapb: str):
    try:
        pb = pb_model.get_pb(mapb)
        if pb:
            return pb
        raise HTTPException(status_code=404, detail="PB not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{mapb}", response_model=PB)
async def update_pb(mapb: str, pb: PB):
    try:
        update_pb = pb_model.update_pb(mapb, pb)
        if update_pb:
            return update_pb
        raise HTTPException(status_code=404, detail="PB not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{mapb}")
async def delete_pb(mapb: str):
    try:
        delete_pb = pb_model.delete_pb(mapb)
        if delete_pb:
            return delete_pb
        raise HTTPException(status_code=404, detail="PB not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")