from tkinter import *
from view.component.table import Table
from view.component.label_text import TextWithLabel
from controller.product_controller import ProductController
from view.admin_main_view import AdminMainView
import tkinter.messagebox as msg


class AdminProductListView:
    def select_row(self, product):
        self.product_id.variable.set(product[0])
        self.product_name.variable.set(product[1])
        self.product_price.variable.set(product[2])

    def reset_form(self):
        self.product_id.variable.set("")
        self.product_name.variable.set("")
        self.product_price.variable.set("")
        status, product_list = ProductController.find_all()
        if status:
            self.table.refresh_table(product_list)

    def to_dict(self):
        return {'id': self.product_id,
                'product name': self.product_name,
                'product price': self.product_price}

    def add_click(self):
        status, message = ProductController.save(self.product_name.variable.get(),
                                                 self.product_price.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Save", "Saved successfully!")
        else:
            msg.showerror("Error", message)

    def edit_click(self):
        status, message = ProductController.edit(self.product_id.variable.get(),
                                                 self.product_name.variable.get(),
                                                 self.product_price.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Edit", "Edited successfully!")
        else:
            msg.showerror("Error", message)

    def delete_click(self):
        status, message = ProductController.remove(self.product_id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Remove", "Deleted successfully!")
        else:
            msg.showerror("Error", message)

    def reset_click(self):
        self.product_id.variable.set("")
        self.product_name.variable.set("")
        self.product_price.variable.set("")

    def search_by_product_name(self, event):
        if self.search_product.variable.get():
            status, product_list = ProductController.find_by_product_name(self.search_product.variable.get())
            if status:
                self.table.refresh_table(product_list)
        else:
            status, product_list = ProductController.find_all()
            if status:
                self.table.refresh_table(product_list)

    def close_win(self):
        self.win.destroy()
        main_view = AdminMainView(self.admin)

    def __init__(self,admin):
        self.admin = admin
        self.win = Tk()
        self.win.configure(bg="Ghost white")
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)
        self.win.title("Product List")
        self.win.geometry("600x300")

        self.product_id = TextWithLabel(self.win, 'Product ID', 30, 30, 70, disabled=True)
        self.product_name = TextWithLabel(self.win, 'Product', 30, 70, 70)
        self.product_price = TextWithLabel(self.win, 'Unit Price', 30, 110, 70)

        self.table = Table(self.win,
                           ['ID', 'Product', 'Unit Price'],
                           [60, 120, 120],
                           260,
                           30,
                           self.select_row,
                           height=10)

        Button(self.win, text='Add', width=11,bg="Pale Green", command=self.add_click).place(x=30, y=195)
        Button(self.win, text='Edit', width=11,bg="Pale Green",  command=self.edit_click).place(x=140, y=195)
        Button(self.win, text='Delete', width=11,bg="Pale Green",  command=self.delete_click).place(x=30, y=230)
        Button(self.win, text='Reset', width=11,bg="Pale Green",  command=self.reset_form).place(x=140, y=230)

        self.search_product = TextWithLabel(self.win, 'Find Product', 30, 150, 75, width=19)
        self.search_product.text_box.bind("<KeyRelease>", self.search_by_product_name)
        self.search_product.text_box.bind("<ButtonRelease>", self.search_by_product_name)

        self.reset_form()

        self.win.mainloop()


#admin = AdminProductListView('admin')
