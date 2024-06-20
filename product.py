from model.entity import *


class Product(Base):
    __tablename__ = "product_tbl"
    __table_args__ = {"extend_existing": True}
    product_id = Column(Integer, primary_key=True, autoincrement=True)
    product_name = Column(String(20), unique=True, nullable=False)
    price = Column(Integer, nullable=False)

    #relation

    order = relationship("Order", back_populates="product")

    def to_dict(self):
        return {'id': self.product_id,
                'product name': self.product_name,
                'product price': self.price}

    def __init__(self, product_name , price):
        self.product_name = product_name
        self.price = price
        self.product_id = None

    @validates("product_name")
    def validate_product_name(self, key, product_name):
        return Validator.name_validator(product_name, "Invalid Username.")

    @validates("price")
    def validate_price(self, key, price):
        return Validator.price_validator(price, "Invalid price.")

