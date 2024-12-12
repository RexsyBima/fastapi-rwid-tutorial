from app.models import Product
from typing import Annotated
from app import data
from fastapi import APIRouter, Response, status, Path, Body

from . import router, products


@router.put("/add_products/", status_code=status.HTTP_202_ACCEPTED)
def add_products(product: Annotated[list[Product], Body()]) -> list[Product]:
    products.extend(product)
    return products
