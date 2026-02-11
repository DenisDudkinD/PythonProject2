from uuid import UUID
from fastapi import Depends, FastAPI, Query
from sqlalchemy.orm import Session

from src.db.deps import get_db


app = FastAPI(title="Book API")
