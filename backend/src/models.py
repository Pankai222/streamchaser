from sqlalchemy import String
from sqlalchemy.dialects import postgresql
from sqlalchemy.sql.schema import Column

from database import Base


class Media(Base):
    __tablename__ = 'media'

    id = Column(String, primary_key=True)
    title = Column(String, nullable=True)
    original_title = Column(String, nullable=True)
    overview = Column(String, nullable=True)
    release_date = Column(String, nullable=True)
    genres = Column(postgresql.ARRAY(String), nullable=True)
    poster_path = Column(String, nullable=True)
