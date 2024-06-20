from tkinter import *
import tkinter.messagebox as msg

from controller.customer_controller import CustomerController
from view.component.label_text import TextWithLabel
from view.customer_main_view import CustomerMainView


class CustomerLoginView:
    def login_click(self):
        ret, customer = CustomerController.find_by_username_and_password(self.username.variable.get(),
                                                                         self.password.variable.get())
        if ret:
            self.win.destroy()
            main_view = CustomerMainView(customer)
        else:
            msg.showerror("Login Error", "Access Denied!")

    def sign_up_click(self):
        self.win.destroy()
        from view.customer_signup_view import SignUpView
        sign_up_view = SignUpView()

    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="Ghost White")
        self.win.geometry("250x250")
        self.win.title("Login")

        self.username = TextWithLabel(self.win, "Username", 25, 40, distance=70, bg="Ghost White")
        self.password = TextWithLabel(self.win, "Password", 25, 90, distance=70, bg="Ghost White")

        Button(self.win, text="Login", width=10, font=("Arial", 11), bg="sea green", command=self.login_click).place(x=75, y=145,
                                                                                                     width=100,
                                                                                                     height=30)
        Button(self.win, text="Signup", width=10, font=("Arial", 11), bg="sea green", command=self.sign_up_click).place(x=75, y=185,
                                                                                                      width=100,
                                                                                                      height=30)

        self.win.mainloop()


#login = CustomerLoginView()
