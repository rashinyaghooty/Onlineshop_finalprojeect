import datetime
from controller.order_controller import OrderController

#remove--passed
#stat,msg = OrderController.remove(1)

#find_by_id--passed
#stat,msg = OrderController.find_all()

#find_by_customer_id--passed
#stat,msg = OrderController.find_by_customer_id(1)

#find_by_product_id--passed
#stat,msg = OrderController.find_by_product_id(1)

#save--passed
#stat,msg = OrderController.save(10,10,(2024,6,2),100,2,3)

#calculate_total_price--passed
#stat,msg = OrderController.calculate_total_price(3,10)

#edit--passed
#stat,msg = OrderController.edit(1,10,900,(2024,6,19),1800,30,4)

#find_by_order_date--passed
#stat,msg = OrderController.find_by_order_date(datetime.date(2024,6,2))

#stat,msg = OrderController.find_all()

#total_amount--passed
stat,msg = OrderController.total_amount(7)

print(msg)




