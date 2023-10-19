from sqlalchemy import (
    Column,
    INT,
    VARCHAR,
    CheckConstraint,
    ForeignKey,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Base(DeclarativeBase):
    id = Column(INT, autoincrement=True, primary_key=True)


class Status(Base):
    __tablename__ = "statuses"

    name = Column(VARCHAR(10), nullable=False, unique=True)

    orders = relationship(argument="Order", back_populates="status")


class User(Base):
    __tablename__ = "users"
    __table_args = (CheckConstraint("char_length(name) >= 4, email LIKE '%@%'"),)

    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)

    orders = relationship(argument="Order", back_populates="user")


class Category(Base):
    __tablename__ = "categories"
    __table_args = (CheckConstraint("char_length(name) >= 2"),)

    name = Column(VARCHAR(24), nullable=False, unique=True)

    products = relationship(argument="Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"
    __table_args = (CheckConstraint("char_length(title) >= 2"),)

    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140))
    category_id = Column(
        INT,
        ForeignKey(column="categories.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    category = relationship(argument=Category, back_populates="products")
    order_items = relationship(argument="OrderItem", back_populates="product")


class Order(Base):
    __tablename__ = "orders"

    user_id = Column(
        INT,
        ForeignKey(column="users.id", ondelete="RESTRICT"),
        nullable=False,
    )
    status_id = Column(
        INT,
        ForeignKey(column="statuses.id", ondelete="RESTRICT"),
        nullable=False,
        index=True,
    )

    user = relationship(argument=User, back_populates="orders")
    status = relationship(argument=Status, back_populates="orders")
    order_items = relationship(argument="OrderItem", back_populates="order")


class OrderItem(Base):
    __tablename__ = "order_items"

    order_id = Column(
        INT,
        ForeignKey(column="orders.id", ondelete="RESTRICT"),
        nullable=False,
    )
    product_id = Column(
        INT,
        ForeignKey(column="products.id", ondelete="RESTRICT"),
        nullable=False,
    )

    order = relationship(argument=Order, back_populates="order_items")
    product = relationship(argument=Product, back_populates="order_items")


engine = create_engine("sqlite:///db2.sqlite3")
session = sessionmaker(bind=engine)
