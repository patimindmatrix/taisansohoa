from fastapi import APIRouter, HTTPException
import uuid
import process
from models import BB
from typing import List
from process import bb as bb_model

router = APIRouter()

@router.get("/", response_model=List[BB])
async def get_all_bb():
    try:
        all_bb = bb_model.get_all_bb()  # Replace this with your actual function to fetch all NV
        return all_bb
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.post("/", response_model=BB)
async def create_bb(bb: BB):
    bb.MABB = str(uuid.uuid4())  # Generate a unique ID
    create_bb = bb_model.create_bb(bb)
    if create_bb:
        return create_bb
    raise HTTPException(status_code=500, detail="Error creating BB")


@router.get("/{mabb}", response_model=BB)
async def read_bb(mabb: str):
    bb = bb_model.get_bb(mabb)
    if bb:
        return bb
    raise HTTPException(status_code=404, detail="BB not found")


@router.put("/{mabb}", response_model=BB)
async def update_bb(mabb: str, bb: BB):
    update_bb = bb_model.update_bb(mabb, bb)
    if update_bb:
        return update_bb
    raise HTTPException(status_code=404, detail="BB not found")


@router.delete("/{mabb}", response_model=BB)
async def delete_bb(mabb: str):
    delete_bb = bb_model.delete_bb(mabb)
    if delete_bb:
        return delete_bb
    raise HTTPException(status_code=404, detail="BB not found")
