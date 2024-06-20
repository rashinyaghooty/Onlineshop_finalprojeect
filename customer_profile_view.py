from tkinter import *
from controller.customer_controller import CustomerController
import tkinter.messagebox as msg
from view.component.label_text import TextWithLabel
from view.customer_main_view import CustomerMainView


class CustomerProfileView:
    def reset_form(self):
        self.customer_id.variable.set("")
        self.name.variable.set("")
        self.last_name.variable.set("")
        self.username.variable.set("")
        self.password.variable.set("")
        self.phone_number.variable.set("")
        self.address.variable.set("")

    def edit_click(self):
        status, message = CustomerController.edit(self.customer_id.variable.get(),
                                                  self.name.variable.get(),
                                                  self.last_name.variable.get(),
                                                  self.username.variable.get(),
                                                  self.password.variable.get(),
                                                  self.phone_number.variable.get(),
                                                  self.address.variable.get())
        if status:
            msg.showinfo("Edit", "Edited successfully")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)

    def close_win(self):
        self.win.destroy()
        main_view = CustomerMainView(self.customer)


    def __init__(self, customer):
        self.customer = customer
        self.win = Tk()
        self.win.configure(bg="Ghost White")
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)
        self.win.geometry("250x400")
        self.win.title("Profile")

        self.customer_id = TextWithLabel(self.win, "ID", 25, 20, disabled=False, distance=65)
        #self.admin_id.variable.set(f"{self.admin.admin_id}")
        self.name = TextWithLabel(self.win, "Firstname", 25, 60, width=20, distance=65)
        self.last_name = TextWithLabel(self.win, "Lastname", 25, 110, width=20, distance=65)
        self.username = TextWithLabel(self.win, "Username", 25, 160, width=20, distance=65)
        self.password = TextWithLabel(self.win, "Password", 25, 210, width=20, distance=65)
        self.phone_number = TextWithLabel(self.win, "Phonenum", 25, 260, width=20, distance=65)
        self.address = TextWithLabel(self.win, "Address", 25, 310,width=20, distance=65)

        Button(self.win, text="Edit", width=10, font=("Arial", 11), bg="Pale Green",  command=self.edit_click).place(x=75, y=350)

        self.win.mainloop()
#profile_view = CustomerProfileView(CustomerController)

