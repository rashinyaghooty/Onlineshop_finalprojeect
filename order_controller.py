from controller.customer_controller import CustomerController
from controller.product_controller import ProductController
from model.da.data_access import *
from model.entity.order import Order
from model.entity.customer import Customer
from model.entity.product import Product
from model.tools.decorators import exception_handling

class OrderController:
    order_da = DataAccess(Order)
    customer_da = DataAccess(Customer)
    product_da = DataAccess(Product)

    @classmethod
    @exception_handling
    def save(cls, quantity, unit_price, order_date, total_price, product_id, customer_id):
        if product_id and customer_id:
            _, customer = CustomerController.find_by_customer_id(customer_id)
            _, product = ProductController.find_by_product_id(product_id)
            order = Order(int(quantity), int(unit_price), order_date, int(total_price), int(product.product_id), int(customer.customer_id))
            cls.customer_da.save(order)
            return True, "Order saved"
        else:
            return False, "Cannot save order"

    @classmethod
    @exception_handling
    def edit(cls, order_id, quantity, unit_price, order_date, total_price, customer_id, product_id):
        _, customer = CustomerController.find_by_customer_id(customer_id)
        _, product = ProductController.find_by_product_id(product_id)
        order = Order(int(quantity), int(unit_price), order_date, int(total_price), int(product.product_id), int(customer.customer_id))
        order.order_id = order_id
        cls.order_da.edit(order)
        return True, "Order edited successfully"

    @classmethod
    @exception_handling
    def remove(cls, order_id):
        entity = cls.order_da.find_by_id(order_id)
        return True, cls.order_da.remove(entity)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.order_da.find_all()

    @classmethod
    @exception_handling
    def find_by_order_id(cls, order_id):
        return True, cls.order_da.find_by_id(order_id)

    @classmethod
    @exception_handling
    def find_by_customer_id(cls, id):
        return True, cls.order_da.find_by(Order.customer_id == id)

    @classmethod
    @exception_handling
    def find_by_product_id(cls, id):
        return True, cls.order_da.find_by(Order.product_id == id)

    @classmethod
    @exception_handling
    def find_by_order_date(cls, order_date):
        return True, cls.order_da.find_by(Order.order_date == order_date)

    @classmethod
    @exception_handling
    def calculate_total_price(cls,quantity, unit_price):
        total_price = unit_price * quantity
        print(total_price)
        return True, int(total_price)

    @classmethod
    @exception_handling
    def total_amount(cls,customer_id):
        total_amount = 0
        order_list= cls.order_da.find_by(Order.customer_id == customer_id)
        for order in order_list:
            total_amount = total_amount + int(order.total_price)
            print(total_amount)
        return True, int(total_amount)







