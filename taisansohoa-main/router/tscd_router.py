from fastapi import APIRouter, HTTPException
import uuid
import process
from models import TSCD
from process import tscd as tscd_model
from typing import List

router = APIRouter()

@router.get("/", response_model=List[TSCD])
async def get_all_tscd():
    try:
        all_tscd = tscd_model.get_all_tscd()  # Replace this with your actual function to fetch all NV
        return all_tscd
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")


@router.post("/", response_model=TSCD)
async def create_tscd(tscd: TSCD):
    try:
        create_tscd = tscd_model.create_tscd(tscd)
        if create_tscd:
            return create_tscd
        raise HTTPException(status_code=500, detail="Error creating TSCĐ")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.get("/{matscd}", response_model=TSCD)
async def read_tscd(matscd: str):
    try:
        tscd = tscd_model.get_tscd(matscd)
        if tscd:
            return tscd
        raise HTTPException(status_code=404, detail="TSCĐ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.put("/{matscd}", response_model=TSCD)
async def update_tscd(matscd: str, tscd: TSCD):
    try:
        update_tscd = tscd_model.update_tscd(matscd, tscd)
        if update_tscd:
            return update_tscd
        raise HTTPException(status_code=404, detail="TSCĐ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@router.delete("/{matscd}", response_model=TSCD)
async def delete_tscd(matscd: str):
    try:
        delete_tscd = tscd_model.delete_tscd(matscd)
        if delete_tscd:
            return delete_tscd
        raise HTTPException(status_code=404, detail="TSCĐ not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")