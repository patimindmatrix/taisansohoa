from fastapi import APIRouter, HTTPException
import uuid
import process
from models import TL

router = APIRouter()


@router.post("/", response_model=TL)
async def create_tl(tl: TL):
    try:
        tl.MATL = str(uuid.uuid4())  # Generate a unique ID
        create_tl = process.create_tl(tl)
        if create_tl:
            return create_tl
        raise HTTPException(status_code=500, detail="Error creating TL")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{matl}", response_model=TL)
async def read_tl(matl: str):
    try:
        tl = process.get_tl(matl)
        if tl:
            return tl
        raise HTTPException(status_code=404, detail="TL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{matl}", response_model=TL)
async def update_tl(matl: str, tl: TL):
    try:
        update_tl = process.update_tl(matl, tl)
        if update_tl:
            return update_tl
        raise HTTPException(status_code=404, detail="TL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{matl}", response_model=TL)
async def delete_tl(matl: str):
    try:
        delete_tl = process.delete_tl(matl)
        if delete_tl:
            return delete_tl
        raise HTTPException(status_code=404, detail="TL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")