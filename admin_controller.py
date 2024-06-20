from model.da.data_access import *
from model.entity.admin import Admin
from model.tools.decorators import exception_handling


class AdminController:
    admin_da = DataAccess(Admin)

    @classmethod
    @exception_handling
    def save(cls, username, password):
        admin = Admin(username, password)
        return True, cls.admin_da.save(admin)

    @classmethod
    @exception_handling
    def edit(cls, admin_id, username, password):
        admin = Admin(username, password)
        admin.admin_id = admin_id
        return True, cls.admin_da.edit(admin)

    @classmethod
    @exception_handling
    def remove(cls, admin_id):
        entity = cls.admin_da.find_by_id(admin_id)
        return True, cls.admin_da.remove(entity)

    @classmethod
    @exception_handling
    def find_all(cls):
        return True, cls.admin_da.find_all()

    @classmethod
    @exception_handling
    def find_by_id(cls, admin_id):
        return True, cls.admin_da.find_by_id(admin_id)

    @classmethod
    @exception_handling
    def find_by_username(cls, username):
        return True, cls.admin_da.find_by(Admin.username == username)

    @classmethod
    @exception_handling
    def find_by_username_and_password(cls, username, password):
        return True, cls.admin_da.find_by(and_(Admin.username == username, Admin.password == password))
