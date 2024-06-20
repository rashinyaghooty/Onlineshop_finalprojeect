from tkinter import *
from model.entity import Admin
from view.admin_profile_view import *


class AdminMainView:
    def click_profile(self):
        self.win.destroy()
        from view.admin_profile_view import AdminProfileView
        admin_profile_view = AdminProfileView(self.admin)

    def click_product_list(self):
        self.win.destroy()
        from view.admin_product_list_view import AdminProductListView
        admin_product_list_view = AdminProductListView(self.admin)

    def __init__(self, admin):
        self.admin = admin
        self.win = Tk()
        self.win.configure(bg="Ghost white")
        self.win.geometry("250x250")
        self.win.title("Admin Panel")

        #Label(text=admin[0].username, font=("Arial", 16)).place(x=90, y=15)

        Button(self.win, text="Profile", width=15, bg="Pale Green", height=2, font=("Arial", 13),
               command=self.click_profile).place(x=50, y=70)
        Button(self.win, text="Product List", width=15, bg="forest green", height=2, font=("Arial", 13),
               command=self.click_product_list).place(x=50, y=140)

        self.win.mainloop()

#admin = Admin("rashin","rashin12")
#admin_view = AdminMainView(admin)
