from fastapi import APIRouter, HTTPException
import uuid
import process
from models import SP

router = APIRouter()


@router.post("/", response_model=SP)
async def create_sp(sp: SP):
    try:
        sp.MASP = str(uuid.uuid4())  # Generate a unique ID
        create_sp = process.create_sp(sp)
        if create_sp:
            return create_sp
        raise HTTPException(status_code=500, detail="Error creating SP")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{masp}", response_model=SP)
async def read_sp(masp: str):
    try:
        sp = process.get_sp(masp)
        if sp:
            return sp
        raise HTTPException(status_code=404, detail="SP not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{masp}", response_model=SP)
async def update_sp(masp: str, sp: SP):
    try:
        update_sp = process.update_sp(masp, sp)
        if update_sp:
            return update_sp
        raise HTTPException(status_code=404, detail="SP not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{masp}", response_model=SP)
async def delete_sp(masp: str):
    try:
        delete_sp = process.delete_sp(masp)
        if delete_sp:
            return delete_sp
        raise HTTPException(status_code=404, detail="SP not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")