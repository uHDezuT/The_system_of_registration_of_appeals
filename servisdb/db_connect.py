from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .settings import settings

engine = create_engine(
    settings.database_url,
    connect_args={'check_same_thread': False}
    # допускаем одно подключение из нескольких потоков
)

SessionLocal = sessionmaker(engine,
                            autocommit=False,
                            autoflush=False)


