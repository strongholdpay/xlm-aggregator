import datetime
import enum
from sqlalchemy import Column, DateTime, Enum, ForeignKey, Integer, Numeric, String
from database import Base


class Exchange(Base):
    __tablename__ = 'exchanges'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)

    def __init__(self, name=None):
        self.name = name

    def __repr__(self):
        return '<Exchange {}>'.format(self.name)


class OrderTypeEnum(enum.Enum):
    buy = 1
    sell = 2


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    order_type = Column(Enum(OrderTypeEnum))
    quantity = Column(Numeric(16,8))
    price = Column(Numeric(16,8))
    exchange_id = Column(Integer, ForeignKey('exchanges.id'))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, order_type=None, quantity=None, price=None, exchange_id=None):
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        self.exchange_id = exchange_id

    def __repr__(self):
        return '<Order {} {} {} {}>'.format(self.order_type, self.quantity, self.price, self.exchange)
