from fastapi import APIRouter, HTTPException
import uuid
import process
from models import DH

router = APIRouter()


@router.post("/", response_model=DH)
async def create_dh(dh: DH):
    dh.MADH = str(uuid.uuid4())  # Generate a unique ID
    create_dh = process.create_dh(dh)
    if create_dh:
        return create_dh
    raise HTTPException(status_code=500, detail="Error creating DH")


@router.get("/{madh}", response_model=DH)
async def read_dh(madh: str):
    dh = process.get_dh(madh)
    if dh:
        return dh
    raise HTTPException(status_code=404, detail="DH not found")


@router.put("/{madh}", response_model=DH)
async def update_dh(madh: str, dh: DH):
    update_dh = process.update_dh(madh, dh)
    if update_dh:
        return update_dh
    raise HTTPException(status_code=404, detail="DH not found")


@router.delete("/{madh}", response_model=DH)
async def delete_dh(madh: str):
    delete_dh = process.delete_dh(madh)
    if delete_dh:
        return delete_dh
    raise HTTPException(status_code=404, detail="DH not found")
