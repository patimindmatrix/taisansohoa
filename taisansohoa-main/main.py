# main.py
from fastapi import FastAPI
from router.user_router import router as user_router
from router.ncc_router import router as ncc_router
from router.pb_router import router as pb_router
from router.kh_router import router as kh_router
from router.nv_router import router as nv_router
from router.tscd_router import router as tscd_router
from router.ccdc_router import router as ccdc_router
from router.tl_router import router as tl_router
from router.hd_router import router as hd_router
from router.sp_router import router as sp_router
from router.nvl_router import router as nvl_router
from router.dh_router import router as dh_router
from router.ctdh_router import router as ctdh_router
from router.bb_router import router as bb_router
from router.vbpq_router import router as vbpq_router
app = FastAPI()

@app.get("/")
async def create_item():
    return {"message": "Item created successfully"}

app.include_router(user_router, prefix="/user", tags=["user"])
app.include_router(ncc_router, prefix="/ncc", tags=["ncc"])
app.include_router(pb_router, prefix="/pb", tags=["pb"])
app.include_router(kh_router, prefix="/kh", tags=["kh"])
app.include_router(nv_router, prefix="/nv", tags=["nv"])
app.include_router(tscd_router, prefix="/tscd", tags=["tscd"])
app.include_router(ccdc_router, prefix="/ccdc", tags=["ccdc"])
app.include_router(tl_router, prefix="/tl", tags=["tl"])
app.include_router(hd_router, prefix="/hd", tags=["hd"])
app.include_router(sp_router, prefix="/sp", tags=["sp"])
app.include_router(nvl_router, prefix="/nvl", tags=["nvl"])
app.include_router(dh_router, prefix="/dh", tags=["dh"])
app.include_router(ctdh_router, prefix="/ctdh", tags=["ctdh"])
app.include_router(bb_router, prefix="/bb", tags=["bb"])
app.include_router(vbpq_router, prefix="/vbpq", tags=["vbpq"])