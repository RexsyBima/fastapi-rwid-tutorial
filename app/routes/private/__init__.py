from fastapi import APIRouter, Depends
from ...depends import allow_private_view

router = APIRouter(prefix="/api/private",
                   tags=["Private Access"], dependencies=[Depends(allow_private_view)])

from . import get  # noqa
