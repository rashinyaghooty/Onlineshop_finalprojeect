from tkinter import *
from controller.admin_controller import AdminController
import tkinter.messagebox as msg

from view.component.label_text import TextWithLabel


class AdminProfileView:
    def reset_form(self):
        self.admin_id.variable.set("")
        self.username.variable.set("")
        self.password.variable.set("")

    def edit_click(self):
        status, message = AdminController.edit(self.admin_id.variable.get(),
                                               self.username.variable.get(),
                                               self.password.variable.get())
        if status:
            msg.showinfo("Edit", "Edited successfully")
            self.reset_form()
        else:
            msg.showerror("Edit Error", message)



    def __init__(self, admin):
        self.admin = admin
        self.win = Tk()
        self.win.configure(bg="Ghost white")


        self.win.geometry("250x250")
        self.win.title("Edit Profile")

        self.admin_id = TextWithLabel(self.win, "AdminID", 30, 30, disabled=False)
        #self.admin_id.variable.set(f"{self.admin.admin_id}")
        self.username = TextWithLabel(self.win, "Username", 30, 80, width=20)
        self.password = TextWithLabel(self.win, "Password", 30, 130, width=20)

        Button(self.win, text="Edit", width=10, font=("Arial", 11),bg="Pale Green", command=self.edit_click).place(x=75, y=185)

        self.win.mainloop()


#profile_view = AdminProfileView(AdminController)
