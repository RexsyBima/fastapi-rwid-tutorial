from typing import Annotated
from . import router, products
from fastapi import APIRouter, Path, status, Response, HTTPException


@router.delete("/todo/{item_id}", status_code=status.HTTP_202_ACCEPTED)
def remove_products(item_id: Annotated[int, Path(ge=1, le=len(products))], response: Response) -> int:
    # 0 1 2 3 4 5
    if item_id > len(products):
        response.status_code = status.HTTP_400_BAD_REQUEST
        raise HTTPException(status_code=response.status_code,
                            detail="Invalid Product ID index")
    products.pop(item_id - 1)
    return status.HTTP_202_ACCEPTED
