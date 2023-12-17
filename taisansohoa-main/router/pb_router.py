import uuid
from fastapi import APIRouter, HTTPException
from models import PB
import process

router = APIRouter()


@router.post("/", response_model=PB)
async def create_pb(pb: PB):
    try:
        pb.MAPB = str(uuid.uuid4())
        created_pb = process.create_pb(pb)
        if created_pb:
            return created_pb
        raise HTTPException(status_code=500, detail="Error creating PB")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{mapb}", response_model=PB)
async def get_pb( mapb: str):
    try:
        pb = process.get_pb(mapb)
        if pb:
            return pb
        raise HTTPException(status_code=404, detail="PB not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{mapb}", response_model=PB)
async def update_pb(mapb: str, pb: PB):
    try:
        update_pb = process.update_pb(mapb, pb)
        if update_pb:
            return update_pb
        raise HTTPException(status_code=404, detail="PB not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{mapb}")
async def delete_pb(mapb: str):
    try:
        delete_pb = process.delete_pb(mapb)
        if delete_pb:
            return delete_pb
        raise HTTPException(status_code=404, detail="PB not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")