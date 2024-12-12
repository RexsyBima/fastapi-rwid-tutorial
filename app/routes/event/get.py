from . import router
from app.models import Event, Item
from fastapi import status


@router.get('/', status_code=status.HTTP_200_OK)
def get_event():
    return {"event": Event(name="latest event"),
            "item": Item(name="latest item")}
