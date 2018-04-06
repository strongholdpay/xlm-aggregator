import datetime
import enum
from sqlalchemy import Column, DateTime, Enum, Integer, Numeric, String
from yourapplication.database import Base


class OrderTypeEnum(enum.Enum):
	buy = 1
	sell = 2

class Order(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    order_type = Column(Enum(OrderTypeEnum))
    quantity = Column(Numeric(8,8))
    price = Column(Numeric(8,8))
    exchange = Column(String(50))
    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, order_type=None, quantity=None, price=None, exchange=None):
        self.order_type = order_type
        self.quantity = quantity
        self.price = price
        self.exchange = exchange

    def __repr__(self):
        return '<Order {} {} {} {}>'.format(self.order_type, self.quantity, self.price, self.exchange)
