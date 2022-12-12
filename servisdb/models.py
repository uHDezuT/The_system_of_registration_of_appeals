from sqlalchemy import Column, Integer, String

from database import Base


class appeals(Base):
    __tablename__ = "appeals"

    id = Column(Integer, primary_key=True, index=True)

    last_name = Column(String)
    first_name = Column(String)
    second_name = Column(String)
    telephone = Column(String)
    body = Column(String)
