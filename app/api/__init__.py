from fastapi import APIRouter
from app.api.routes import recommendations

router = APIRouter()
router.include_router(recommendations.router, prefix="/api", tags=["recommendations"])
