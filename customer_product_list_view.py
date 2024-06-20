from tkinter import *
from view.component.table import Table
from view.component.label_text import TextWithLabel
from controller.product_controller import ProductController
from controller.order_controller import OrderController
import tkinter.messagebox as msg
from view.component.persian_calendar import PersianCalendar
from view.customer_main_view import CustomerMainView

class CustomerProductListView:
    def select_row(self, product):
        self.product_id.variable.set(product[0])
        self.product_name.variable.set(product[1])
        self.unit_price.variable.set(product[2])

    def reset_form(self):
        self.product_id.variable.set("")
        self.product_name.variable.set("")
        self.unit_price.variable.set("")
        self.quantity.variable.set("")
        #self.total_price.variable.set("")
        status, product_list = ProductController.find_all()
        if status:
            self.table.refresh_table(product_list)

    def to_dict(self):
        return {#'order_id': self.order_id,
                'quantity': self.quantity,
                'unit_price': self.unit_price,
                #'order_date': self.order_date,
                #'total_price': self.total_price,
                'customer_id': self.customer_id,
                'product_id': self.product_id}

    def add_click(self):
        status, message = OrderController.save(self.quantity.variable.get(),
                                               self.unit_price.variable.get(),
                                               self.calendar.gregorian_date,
                                               str(self.calculate_total_price()),
                                               self.product_id.variable.get(),
                                               self.customer_id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Save", "Saved successfully!")
        else:
            msg.showerror("Error", message)

    def reset_click(self):
        self.product_id.variable.set("")
        self.product_name.variable.set("")
        self.unit_price.variable.set("")
        self.quantity.variable.set("")

    def continue_click(self):
        self.win.destroy()
        from view.customer_cart_view import CustomerCartView
        customer_cart = CustomerCartView(self.customer)

    def back_click(self):
        self.win.destroy()
        from view.customer_main_view import CustomerMainView
        customer_main_view = CustomerMainView(self.customer)

    def search_by_product_name(self, event):
        if self.search_product.variable.get():
            status, product_list = ProductController.find_by_product_name(self.search_product.variable.get())
            if status:
                self.table.refresh_table(product_list)
        else:
            status, product_list = ProductController.find_all()
            if status:
                self.table.refresh_table(product_list)

    def calculate_total_price(self):
        if (self.quantity.variable.get() and self.unit_price.variable.get()):
            status, total_price = OrderController.calculate_total_price(int(self.quantity.variable.get()),
                                                                        int(self.unit_price.variable.get()))
            if status:
                return total_price

    def close_win(self):
        self.win.destroy()
        main_view = CustomerMainView(self.customer)

    def __init__(self, product, customer):
        self.product = product
        self.customer = customer
        self.win = Tk()
        self.win.configure(bg="Ghost White")
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)
        self.win.title("Product List")
        self.win.geometry("600x350")

        print(customer[0].customer_id)
        print(type(customer))

        self.customer_id = TextWithLabel(self.win, 'Customer ID', 30, 30, 70, disabled=True)
        self.customer_id.variable.set(f"{self.customer[0].customer_id}")
        self.product_id = TextWithLabel(self.win, 'Product ID', 30, 70, 70, disabled=True)
        self.product_name = TextWithLabel(self.win, 'Product', 30, 110, 70, disabled=True)
        self.unit_price = TextWithLabel(self.win, 'Unit Price', 30, 150, 70, disabled=True)
        Label(self.win, text="OrderDate", bg="Ghost White").place(x=30, y=230)
        self.calendar = PersianCalendar(self.win, 100, 230)
        self.quantity = TextWithLabel(self.win, 'Quantity', 30, 190, 70, disabled=False)

        self.table = Table(self.win,
                           ['ID', 'Product', 'Unit Price'],
                           [60, 120, 120],
                           260,
                           30,
                           self.select_row,
                           10)

        Button(self.win, text='Add to cart', width=11, bg="Pale Green",  command=self.add_click).place(x=30, y=270)
        Button(self.win, text='Reset', width=11, bg="Pale Green",  command=self.reset_click).place(x=140, y=270)
        Button(self.win, text='Go to cart', width=11, bg="Pale Green",  command=self.continue_click).place(x=30, y=305)
        Button(self.win, text='Previous page', width=11, bg="Pale Green",  command=self.back_click).place(x=140, y=305)

        self.search_product = TextWithLabel(self.win, 'Find Product', 260, 275, 75, width=19)
        self.search_product.text_box.bind("<KeyRelease>", self.search_by_product_name)
        self.search_product.text_box.bind("<ButtonRelease>", self.search_by_product_name)

        self.reset_form()

        self.win.mainloop()

#customer = CustomerProductListView('product','customer')
#customer = Customer("ali","alipoor","aliii","ali123","09134567891","jhgfhfjfhjewgvk")
#customer_view = CustomerProductListView('product',customer)
