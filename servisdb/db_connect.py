from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False}
    # допускаем одно подключение из нескольких потоков
)

Session = sessionmaker(engine,
                       autocommit=False,
                       autoflush=False)


def get_session() -> Session:  # механизм внедрения зависимостей для
    # автоматического открытия и закрытия сессии
    session = Session()
    try:
        yield session
    finally:
        session.close()
