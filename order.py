from model.entity import *


class Order(Base):
    __tablename__ = "order_tbl"
    __table_args__ = {"extend_existing": True}
    order_id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(Integer, nullable=False)
    order_date = Column(Date, nullable=False)
    total_price = Column(Integer, nullable=False)

    #relations
    product_id = Column(Integer, ForeignKey("product_tbl.product_id"), nullable=False)
    customer_id = Column(Integer, ForeignKey("customer_tbl.customer_id"), nullable=False)
    product = relationship("Product", back_populates="order")
    customer = relationship("Customer", back_populates="order")

    def to_dict(self):
        return {'order_id' : self.order_id,
                'quantity' : self.quantity,
                'unit_price' : self.unit_price,
                'order_date' : self.order_date,
                'total_price': self.total_price,
                'product_id': self.product_id,
                'customer_id':self.customer_id}



    def __init__(self, quantity , unit_price, order_date, total_price, product_id, customer_id):
        self.quantity = quantity
        self.unit_price = unit_price
        self.order_date = order_date
        self.total_price = total_price
        self.product_id = product_id
        self.customer_id = customer_id

    @validates("quantity")
    def validate_quantity(self, key, quantity):
        return Validator.amount_validator(quantity, "Quantity must be more than zero")

    @validates("unit_price")
    def validate_unit_price(self, key, unit_price):
        return Validator.price_validator(unit_price, "Invalid price must be more than zero")

    @validates("order_date")
    def validate_order_date(self, key, order_date):
        return Validator.date_validator(order_date, "Invalid date!")

    @validates("total_price")
    def validate_total_price(self, key, total_price):
        return Validator.price_validator(total_price,"Invalid price must be more than zero")





