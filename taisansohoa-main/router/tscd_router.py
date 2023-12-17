from fastapi import APIRouter, HTTPException
import uuid
import process
from models import TSCD

router = APIRouter()


@router.post("/", response_model=TSCD)
async def create_tscd(tscd: TSCD):
    try:
        tscd.MATSCD = str(uuid.uuid4())  # Generate a unique ID
        create_tscd = process.create_tscd(tscd)
        if create_tscd:
            return create_tscd
        raise HTTPException(status_code=500, detail="Error creating TSCĐ")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{matscd}", response_model=TSCD)
async def read_tscd(matscd: str):
    try:
        tscd = process.get_tscd(matscd)
        if tscd:
            return tscd
        raise HTTPException(status_code=404, detail="TSCĐ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{matscd}", response_model=TSCD)
async def update_tscd(matscd: str, tscd: TSCD):
    try:
        update_tscd = process.update_tscd(matscd, tscd)
        if update_tscd:
            return update_tscd
        raise HTTPException(status_code=404, detail="TSCĐ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{matscd}", response_model=TSCD)
async def delete_tscd(matscd: str):
    try:
        delete_tscd = process.delete_tscd(matscd)
        if delete_tscd:
            return delete_tscd
        raise HTTPException(status_code=404, detail="TSCĐ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")