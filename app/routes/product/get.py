from fastapi import Path, Response, status
from fastapi import Form
from typing import Annotated
from ...forms import FormData
from app.models import Product
from . import router, products


@router.get("/get_detail/{item_id}", status_code=status.HTTP_201_CREATED)
def get_product_detail(response: Response, item_id: Annotated[int, Path(ge=1)]) -> Product:
    return products[item_id - 1]
