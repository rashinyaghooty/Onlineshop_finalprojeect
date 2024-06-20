
from tkinter import *

from model.entity import product, order


class WelcomeView:
    def admin_click(self):
        self.win.destroy()
        from view.admin_login_view import AdminLoginView
        login_view = AdminLoginView()

    def customer_click(self):
        self.win.destroy()
        from view.customer_login_view import CustomerLoginView
        customer_login_view = CustomerLoginView()

    def __init__(self):
        self.win = Tk()
        self.win.geometry("300x260")
        self.win.config(bg="Ghost white")
        self.win.title("Welcome")

        Label(self.win, text="Welcome to our shop!", bg="Ghost white", fg="forest green", font=("Arial", 18)).place(x=30, y=30)
        Label(self.win, text="Please choose your role:", bg="Ghost white", fg="black", font=("Arial", 12)).place(x=60, y=80)

        Button(self.win, text="Admin", width=10, font=('Arial',11), bg="Pale Green", command=self.admin_click).place(x=90, y=130, width=120,
                                                                                           height=35)
        Button(self.win, text="Customer", width=10, font=('Arial',11), bg="Pale Green", command=self.customer_click).place(x=90, y=180, width=120,
                                                                                                 height=35)

        self.win.mainloop()
#welcome_view = WelcomeView()
