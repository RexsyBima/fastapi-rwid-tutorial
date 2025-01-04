from app.models import User, Cart, Product
from fastapi import status
from typing import Annotated
from app.depends import get_current_active_user, get_session
from fastapi import Depends
from sqlmodel import Session, select


from . import router


@router.post("/add_product_to_cart/")
def add_product(current_user: Annotated[User, Depends(get_current_active_user)], session: Annotated[Session, Depends(get_session)], product_id: int) -> int:
    product = session.exec(select(Product)
                           .where(Product.id == product_id)).first()
    if product is None:
        return status.HTTP_404_NOT_FOUND
    cart = Cart(
        user_id=current_user.id,
        product_id=product.id
    )
    session.add(cart)
    session.commit()
    return status.HTTP_201_CREATED


@router.post("/calculate_total_price/")
def calculate_total_price(current_user: Annotated[User, Depends(get_current_active_user)], session: Annotated[Session, Depends(get_session)], ) -> int:
    products = session.exec(select(Cart)
                            .where(Cart.user_id == current_user.id)).all()
    if len(products) == 0:
        return status.HTTP_404_NOT_FOUND
    total_price = 0
    for product in products:
        target = session.exec(select(Product).where(
            Product.id == product.product_id)).first()
        if target is not None:
            total_price += target.price * target.quantity
    return total_price
