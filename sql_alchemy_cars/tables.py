from sqlalchemy import create_engine, Column, String, Integer, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

users_models_associations = Table(
    "users_models",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("model_id", Integer, ForeignKey("models.id"))
)

class Brands(Base):
    __tablename__ = "brands"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    country = Column(String, nullable=False)
    models = relationship("Models", back_populates="brands")


class Models(Base):
    __tablename__ = "models"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    year = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    brand_id = Column(Integer, ForeignKey("brands.id"))
    brands = relationship("Brands", back_populates="models")
    users = relationship("Users", secondary=users_models_associations, back_populates="models")


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    models = relationship("Models", secondary=users_models_associations, back_populates="users")
