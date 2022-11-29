from fastapi import APIRouter, Depends  # внедрение зависимости(Depends)
from sqlalchemy.orm import Session

from servisdb.db_connect import get_session

router = APIRouter(
    prefix='/operations'
)


@router.get('/')
def get_operations(session: Session = Depends(get_session)):  # для выгрузки списка операций
    return []
