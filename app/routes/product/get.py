from fastapi import Path, Response, status, Form, Query, Depends, HTTPException
from typing import Annotated
from app.models import Product
from ...depends import QueryParameter, query_parameter_function
from . import router
