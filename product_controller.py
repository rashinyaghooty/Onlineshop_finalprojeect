from model.da.data_access import *
from model.entity import Product
from model.tools.decorators import exception_handling


class ProductController:
    product_da = DataAccess(Product)

    @classmethod
    @exception_handling
    def save(cls, product_name, price):
        product = Product(product_name, int(price))
        return True, cls.product_da.save(product)

    @classmethod
    @exception_handling
    def edit(cls, product_id, product_name, price):
        product = Product(product_name, int(price))
        product.product_id= product_id
        return True, cls.product_da.edit(product)

    @classmethod
    @exception_handling
    def remove(cls, product_id):
        entity = cls.product_da.find_by_id(product_id)
        return True, cls.product_da.remove(entity)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.product_da.find_all()

    @classmethod
    @exception_handling
    def find_by_product_id(cls, product_id):
        return True, cls.product_da.find_by_id(product_id)

    @classmethod
    @exception_handling
    def find_by_product_name(cls, product_name):
        return True, cls.product_da.find_by(Product.product_name == product_name)
