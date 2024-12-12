from typing import Annotated
from app.models import Product
from fastapi import status,  Body
from . import router


@router.post("/calculate_total_price/", status_code=status.HTTP_201_CREATED)
def calculate_total_price(products: Annotated[list[Product], Body()]):
    total_price = 0
    for p in products:
        total_price += p.price * p.quantity
    discounted_price = total_price * 0.5
    total_price = total_price - discounted_price
    return total_price
