from fastapi import APIRouter, HTTPException
import uuid
import process
from models import CCDC

router = APIRouter()


@router.post("/", response_model=CCDC)
async def create_ccdc(ccdc: CCDC):
    ccdc.MACCDC = str(uuid.uuid4())  # Generate a unique ID
    create_ccdc = process.create_ccdc(ccdc)
    if create_ccdc:
        return create_ccdc
    raise HTTPException(status_code=500, detail="Error creating CCDC")


@router.get("/{maccdc}", response_model=CCDC)
async def read_tscd(maccdc: str):
    ccdc = process.get_ccdc(maccdc)
    if ccdc:
        return ccdc
    raise HTTPException(status_code=404, detail="CCDC not found")


@router.put("/{maccdc}", response_model=CCDC)
async def update_ccdc(maccdc: str, ccdc: CCDC):
    update_ccdc = process.update_ccdc(maccdc, ccdc)
    if update_ccdc:
        return update_ccdc
    raise HTTPException(status_code=404, detail="CCDC not found")


@router.delete("/{maccdc}", response_model=CCDC)
async def delete_ccdc(maccdc: str):
    delete_ccdc = process.delete_ccdc(maccdc)
    if delete_ccdc:
        return delete_ccdc
    raise HTTPException(status_code=404, detail="CCDC not found")
