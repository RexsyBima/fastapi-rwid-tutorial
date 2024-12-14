from typing import Annotated
from app.models import Product
from sqlmodel import Session, select
from app.depends import get_session
from fastapi import Depends, HTTPException
from fastapi import status, Body
from . import router


@router.post("/calculate_total_price/", status_code=status.HTTP_201_CREATED)
def calculate_total_price(products: Annotated[list[Product], Body()]):
    total_price = 0
    for p in products:
        total_price += p.price * p.quantity
    discounted_price = total_price * 0.5
    total_price = total_price - discounted_price
    return total_price


@router.post("/add_product/", status_code=status.HTTP_201_CREATED)
def add_product(product: Product, session: Annotated[Session, Depends(get_session)]):
    if product.price < 0 or product.quantity < 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)
    session.add(product)
    session.commit()
    session.refresh(product)
    return product
