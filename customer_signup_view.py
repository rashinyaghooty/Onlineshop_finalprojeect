from tkinter import *
import tkinter.messagebox as msg

from view.component.label_text import TextWithLabel
from controller.customer_controller import CustomerController


class SignUpView:
    def sign_in_click(self):
        status, message = CustomerController.save(self.name.variable.get(),
                                                  self.last_name.variable.get(),
                                                  self.username.variable.get(),
                                                  self.password.variable.get(),
                                                  self.phone_number.variable.get(),
                                                  self.address.variable.get())

        if status:
            msg.showinfo("Save", "record saved successfully!")
        else:
            msg.showerror("Error", message)

    def back_to_login(self):
        self.win.destroy()
        from view.customer_login_view import CustomerLoginView
        customer_login_view = CustomerLoginView()

    def __init__(self):
        self.win = Tk()
        self.win.configure(bg="Ghost White")
        self.win.geometry("300x400")
        self.win.title("Sign up")

        self.name = TextWithLabel(self.win, "Firstname", 35, 30, distance=75, width=25)
        self.last_name = TextWithLabel(self.win, "Lastname", 35, 70, distance=75, width=25)
        self.username = TextWithLabel(self.win, "Username", 35, 110, distance=75, width=25)
        self.password = TextWithLabel(self.win, "Password", 35, 150, distance=75, width=25)
        self.phone_number = TextWithLabel(self.win, "Phone num", 35, 190, distance=75, width=25)
        self.address = TextWithLabel(self.win, "Address", 35, 230, distance=75, width=25)

        Button(self.win, text="Sign in", width=10, font=("Arial", 11), bg="Pale Green", command=self.sign_in_click).place(x=85, y=285,
                                                                                                         width=130,
                                                                                                         height=35)
        Button(self.win, text="Back ", width=10, font=("Arial", 11), bg="Pale Green", command=self.back_to_login).place(x=85, y=335,
                                                                                                       width=130,
                                                                                                       height=35)

        self.win.mainloop()


#signup_view = SignUpView()
