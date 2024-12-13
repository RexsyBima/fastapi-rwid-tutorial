from fastapi import Path, Response, status, Form, Query, Depends, HTTPException
from typing import Annotated
from app.models import Product
from ...depends import QueryParameter, query_parameter_function
from . import router, products


@router.get("/get_detail/{item_id}", status_code=status.HTTP_202_ACCEPTED)
def get_product_detail(response: Response, item_id: Annotated[int, Path(ge=1)]) -> Product:
    return products[item_id - 1]


@router.get("/products/", status_code=status.HTTP_202_ACCEPTED)
def get_products(params: Annotated[dict, Depends(query_parameter_function)], response: Response) -> list[Product]:
    if params['end'] > len(products) or params['start'] > len(products) or params['start'] < 0:
        response.status_code = status.HTTP_400_BAD_REQUEST
        raise HTTPException(status_code=response.status_code,
                            detail="Invalid value")
    return products[params['start']:params['end']]
