from fastapi import APIRouter, HTTPException
import uuid
import process
from models import NVL

router = APIRouter()


@router.post("/", response_model=NVL)
async def create_nvl(nvl: NVL):
    try:
        nvl.MANVL = str(uuid.uuid4())  # Generate a unique ID
        create_nvl = process.create_nvl(nvl)
        if create_nvl:
            return create_nvl
        raise HTTPException(status_code=500, detail="Error creating NVL")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{manvl}", response_model=NVL)
async def read_nvl(manvl: str):
    try:
        nvl = process.get_nvl(manvl)
        if nvl:
            return nvl
        raise HTTPException(status_code=404, detail="NVL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{manvl}", response_model=NVL)
async def update_nvl(manvl: str, nvl: NVL):
    try:
        update_nvl = process.update_nvl(manvl, nvl)
        if update_nvl:
            return update_nvl
        raise HTTPException(status_code=404, detail="NVL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{manvl}", response_model=NVL)
async def delete_nvl(manvl: str):
    try:
        delete_nvl = process.delete_nvl(manvl)
        if delete_nvl:
            return delete_nvl
        raise HTTPException(status_code=404, detail="NVL not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")