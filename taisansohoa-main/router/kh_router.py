from fastapi import APIRouter, HTTPException
import uuid
import process
from models import KH

router = APIRouter()


@router.post("/", response_model=KH)
async def create_kh(kh: KH):
    try:
        kh.MAKH = str(uuid.uuid4())  # Generate a unique ID
        created_kh = process.create_kh(kh)
        if created_kh:
            return created_kh
        raise HTTPException(status_code=500, detail="Error creating KH")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{makh}", response_model=KH)
async def read_kh(makh: str):
    try:
        kh = process.get_kh(makh)
        if kh:
            return kh
        raise HTTPException(status_code=404, detail="KH not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{makh}", response_model=KH)
async def update_kh(makh: str, kh: KH):
    try:
        update_kh = process.update_kh(makh, kh)
        if update_kh:
            return update_kh
        raise HTTPException(status_code=404, detail="KH not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{makh}", response_model=KH)
async def delete_kh(makh: str):
    try:
        delete_kh = process.delete_kh(makh)
        if delete_kh:
            return delete_kh
        raise HTTPException(status_code=404, detail="KH not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")