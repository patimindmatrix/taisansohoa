from fastapi import APIRouter, HTTPException
import uuid
import process
from models import CTDH

router = APIRouter()


@router.post("/", response_model=CTDH)
async def create_ctdh(ctdh: CTDH):
    ctdh.MACTDH = str(uuid.uuid4())  # Generate a unique ID
    create_ctdh = process.create_ctdh(ctdh)
    if create_ctdh:
        return create_ctdh
    raise HTTPException(status_code=500, detail="Error creating CTDH")


@router.get("/{mactdh}", response_model=CTDH)
async def read_ctdh(mactdh: str):
    ctdh = process.get_ctdh(mactdh)
    if ctdh:
        return ctdh
    raise HTTPException(status_code=404, detail="CTDH not found")


@router.put("/{mactdh}", response_model=CTDH)
async def update_ctdh(mactdh: str, ctdh: CTDH):
    update_ctdh = process.update_ctdh(mactdh, ctdh)
    if update_ctdh:
        return update_ctdh
    raise HTTPException(status_code=404, detail="CTDH not found")


@router.delete("/{mactdh}", response_model=CTDH)
async def delete_ctdh(mactdh: str):
    delete_ctdh = process.delete_ctdh(mactdh)
    if delete_ctdh:
        return delete_ctdh
    raise HTTPException(status_code=404, detail="CTDH not found")
