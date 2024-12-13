from fastapi import APIRouter
from ...models import Product

router = APIRouter(prefix="/api/product", tags=["Product Model"])
products: list[Product] = [Product(id=1, title="Product 1", price=100, quantity=10), Product(
    id=2, title="Product 2", price=200, quantity=20), Product(id=3, title="Product 3", price=300, quantity=30)]

from . import get, create, delete, update  # noqa
