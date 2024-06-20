from tkinter import *
import tkinter.messagebox as msg

from controller.admin_controller import AdminController
from view.component.label_text import TextWithLabel
from view.admin_main_view import AdminMainView


class AdminLoginView:
    def admin_login_click(self):
        ret, admin = AdminController.find_by_username_and_password(self.username.variable.get(),
                                                                  self.password.variable.get())
        if ret:
            self.win.destroy()
            #admin = AdminController(self.)
            main_view = AdminMainView(admin)
        else:
            msg.showerror("Login Error", "Access Denied!")

    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="Ghost white")
        self.win.geometry("250x250")
        self.win.title("Login")

        self.username = TextWithLabel(self.win, "Username", 25, 40, distance=70)
        self.password = TextWithLabel(self.win, "Password", 25, 90, distance=70)

        Button(self.win, text="Login", width=10, font=("Arial", 11), bg="Pale Green", command=self.admin_login_click).place(x=75, y=170,
                                                                                                     width=100,
                                                                                                     height=30)

        self.win.mainloop()


#login = AdminLoginView()
