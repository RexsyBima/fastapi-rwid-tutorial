from app.models import User, Cart, Product
from fastapi import status
from typing import Annotated
from app.depends import get_current_active_user, get_session
from fastapi import Depends
from sqlmodel import Session, select


from . import router


@router.delete("/delete_product_from_cart/")
def add_product(current_user: Annotated[User, Depends(get_current_active_user)], session: Annotated[Session, Depends(get_session)], product_id: int) -> int:
    cart = session.exec(select(Cart)
                        .where(Cart.product_id == product_id and Cart.user_id == current_user.id)).first()
    if cart is None:
        return status.HTTP_404_NOT_FOUND
    session.delete(cart)
    session.commit()
    return status.HTTP_200_OK
