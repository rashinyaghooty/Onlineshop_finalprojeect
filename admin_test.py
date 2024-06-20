from controller.admin_controller import AdminController
from model.entity.admin import Admin

#save--passed
#status,message = AdminController.save("rashin","rashin123")

#edit--passed
#status,message = AdminController.edit(1,"eli","elnaz123")

#remove--passed
#status,message = AdminController.remove('1')

#find_by_id--passed
status,message = AdminController.find_by_id(2)

#find_all--passed
#status,message = AdminController.find_all()

#find_by_username--passed
#status,message = AdminController.find_by_username("eli")

#find_by_username_and_password--passed
#status,message = AdminController.find_by_username_and_password("eli","elnaz123")
#print(message)


print(message)