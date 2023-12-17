from fastapi import APIRouter, HTTPException
import uuid
import process
from models import BB

router = APIRouter()


@router.post("/", response_model=BB)
async def create_bb(bb: BB):
    bb.MABB = str(uuid.uuid4())  # Generate a unique ID
    create_bb = process.create_bb(bb)
    if create_bb:
        return create_bb
    raise HTTPException(status_code=500, detail="Error creating BB")


@router.get("/{mabb}", response_model=BB)
async def read_bb(mabb: str):
    bb = process.get_bb(mabb)
    if bb:
        return bb
    raise HTTPException(status_code=404, detail="BB not found")


@router.put("/{mabb}", response_model=BB)
async def update_bb(mabb: str, bb: BB):
    update_bb = process.update_bb(mabb, bb)
    if update_bb:
        return update_bb
    raise HTTPException(status_code=404, detail="BB not found")


@router.delete("/{mabb}", response_model=BB)
async def delete_bb(mabb: str):
    delete_bb = process.delete_bb(mabb)
    if delete_bb:
        return delete_bb
    raise HTTPException(status_code=404, detail="BB not found")
