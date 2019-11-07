import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.sql import func

Base = declarative_base()


class Category(Base):
    __tablename__ = 'category'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)


class CatalogItem(Base):
    __tablename__ = 'catalog_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    category_id = Column(Integer, ForeignKey('category.id'))
    timestamp = Column(DateTime(timezone=True), default=func.now())

    category = relationship(Category)


engine = create_engine('sqlite:///catalog.db')
Base.metadata.create_all(engine)
