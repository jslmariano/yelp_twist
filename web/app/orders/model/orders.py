from app.main import db
import datetime


class Orders(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_name = db.Column(db.String(500), unique=True, nullable=False)
    customer_id = db.Column(db.String(500), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self):
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return '<id: order_name: {}'.format(self.order_name)


class OrderItems(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    price_per_unit = db.Column(db.Float, unique=True, nullable=False)
    quantity = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product = db.Column(db.String(500), unique=True, nullable=False)

    def __repr__(self):
        return '<id: product: {}'.format(self.product)


class OrderDeliveries(db.Model):
    """
    Token Model for storing JWT tokens
    """
    __tablename__ = 'order_deliveries'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_item_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    delivered_quantity = db.Column(db.Integer, primary_key=True, autoincrement=True)
