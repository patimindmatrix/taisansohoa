from fastapi import APIRouter, HTTPException
import uuid
import process
from models import HD

router = APIRouter()


@router.post("/", response_model=HD)
async def create_hd(hd: HD):
    hd.MAHD = str(uuid.uuid4())  # Generate a unique ID
    create_hd = process.create_hd(hd)
    if create_hd:
        return create_hd
    raise HTTPException(status_code=500, detail="Error creating HĐ")


@router.get("/{mahd}", response_model=HD)
async def read_hd(mahd: str):
    hd = process.get_hd(mahd)
    if hd:
        return hd
    raise HTTPException(status_code=404, detail="HĐ not found")


@router.put("/{mahd}", response_model=HD)
async def update_hd(mahd: str, hd: HD):
    update_hd = process.update_hd(mahd, hd)
    if update_hd:
        return update_hd
    raise HTTPException(status_code=404, detail="HĐ not found")


@router.delete("/{mahd}", response_model=HD)
async def delete_hd(mahd: str):
    delete_hd = process.delete_hd(mahd)
    if delete_hd:
        return delete_hd
    raise HTTPException(status_code=404, detail="HĐ not found")
