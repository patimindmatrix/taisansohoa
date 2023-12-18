from fastapi import APIRouter, HTTPException
import uuid
import process
from models import NCC
from process import ncc as ncc_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[NCC])
async def get_all_ncc():
    try:
        all_ncc = ncc_model.get_all_ncc()  # Replace this with your actual function to fetch all NV
        return all_ncc
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/", response_model=NCC)
async def create_ncc(ncc: NCC):
    try:
        ncc.MANCC = str(uuid.uuid4())  # Generate a unique ID
        created_ncc = ncc_model.create_ncc(ncc)
        if created_ncc:
            return created_ncc
        raise HTTPException(status_code=500, detail="Error creating NCC")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{mancc}", response_model=NCC)
async def read_ncc(mancc: str, ncc: NCC):
    try:
        ncc = ncc_model.get_ncc(mancc)
        if ncc:
            return ncc
        raise HTTPException(status_code=404, detail="NCC not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{mancc}", response_model=NCC)
async def update_ncc(mancc: str, ncc: NCC):
    try:
        updated_ncc = ncc_model.update_ncc(mancc, ncc)
        if updated_ncc:
            return updated_ncc
        raise HTTPException(status_code=404, detail="NCC not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
@router.delete("/{mancc}", response_model=NCC)
async def delete_ncc(mancc: str, ncc: NCC):
    try:
        deleted_ncc = ncc_model.delete_ncc(mancc)
        if deleted_ncc:
            return deleted_ncc
        raise HTTPException(status_code=404, detail="NCC not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")