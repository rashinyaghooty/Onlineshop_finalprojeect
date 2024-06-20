from model.da.data_access import *
from model.entity import customer
from model.entity.customer import Customer
from model.tools.decorators import exception_handling


class CustomerController:
    customer_da = DataAccess(Customer)

    @classmethod
    @exception_handling
    def save(cls, name, last_name,  username, password, phone_number, address):
        customer = Customer(name, last_name, username, password, phone_number, address)
        return True, cls.customer_da.save(customer)

    @classmethod
    @exception_handling
    def edit(cls, customer_id, name, last_name, username, password, phone_number, address):
        customer = Customer(name, last_name, username, password, phone_number, address)
        customer.customer_id = customer_id
        return True, cls.customer_da.edit(customer)

    @classmethod
    @exception_handling
    def remove(cls, customer_id):
        entity = cls.customer_da.find_by_id(customer_id)
        return True, cls.customer_da.remove(entity)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.customer_da.find_all()

    @classmethod
    @exception_handling
    def find_by_customer_id(cls, customer_id):
        return True, cls.customer_da.find_by_id(customer_id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return True, cls.customer_da.find_by(Customer.username == username)

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        return True, cls.customer_da.find_by(and_(Customer.username == username, Customer.password == password))

    #print(customer.customer_id)