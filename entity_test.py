from model.da.data_access import DataAccess
from model.entity import Customer, Product, Order
from model.entity.admin import User


#User:
#save--passed
#edit--passed
#find_all--passed
#find_by_id--passed
#remove--passed
user_da = DataAccess(User)
#user1 = User("maryam","maryam123",role="customer")
#user2 = User("ali","ali123",role="customer")
#user_da.save(user2)
#print(user_da.find_all())
#print(user_da.find_by_id(2))
#user_da.remove(user2)


#Customer:
#save--passed
#edit--passed
#find_all--passed
#find_by_id--passed
customer_da = DataAccess(Customer)
#custumer1 = Customer("maryam","hosseini","09016497577","gvghvjhgvhgfgfpgvh",3)
#customer_da.edit(custumer1)
#customer_da.save(custumer1)
#custumer1.last_name ="hasaneini"
#customer_da.edit(custumer1)
#print(customer_da.find_all())
#print(customer_da.find_by_id(1))
customer3 = Customer("elnaz","tabatabaei","09355983286","hgfgdhgsgsfhhgfghghgjhnn",6)
customer_da.save(customer3)
customer_da.remove(customer3)


#Product:
#save--passed
#edit--passed
#find_all--passed
#find_by_id--passed
product_da = DataAccess(Product)
#product1 = Product("mobile",15000000)
#product_da.save(product1)
#product1.product_name = "laptop"
#product_da.edit(product1)
#print(product_da.find_all())
#print(product_da.find_by_id(4))


#Order:
#save--passed
#edit--passed
#find_all--passed
#find_by_id--passed
order_da = DataAccess(Order)
order1 = Order(1,15000000,(2024,6,15),15000000,4,1)
#order_da.save(order1)
#order1.quantity =2
#order_da.edit(order1)
#print(order_da.find_all())
#print(order_da.find_by_id(6))
order_da.remove(order1)


