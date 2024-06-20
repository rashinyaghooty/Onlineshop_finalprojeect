from datetime import datetime
from tkinter import *
from view.component.table import Table
from view.component.label_text import TextWithLabel
from controller.order_controller import OrderController
import tkinter.messagebox as msg
from view.component.persian_calendar import PersianCalendar
from view.customer_main_view import CustomerMainView
from view.customer_product_list_view import CustomerProductListView
from tkinter import ttk


class CustomerCartView:
    def select_row(self, order):
        self.order_id.variable.set(order[0])
        self.quantity.variable.set(order[1])
        self.unit_price.variable.set(order[2])
        date_time = datetime.strptime(order[3], "%Y-%m-%d")
        self.calendar.set_date(date_time)
        self.total_price.variable.set(order[4])
        self.product_id.variable.set(order[5])

    def reset_form(self):
        self.order_id.variable.set("")
        self.quantity.variable.set("")
        self.unit_price.variable.set("")
        self.total_price.variable.set("")
        self.product_id.variable.set("")
        status, order_list = OrderController.find_by_customer_id(self.customer[0].customer_id)
        if status:
            self.table.refresh_table(order_list)
            self.calc_total_amount()
        else:
            Label(self.win, text='0',font=("Arial",12)).place(x=430, y=385)

    def to_dict(self):
        return {'order_id': self.order_id,
                'quantity': self.quantity,
                'unit_price': self.unit_price,
                'order_date': self.calendar,
                'total_price': self.total_price,
                'product_id': self.product_id,
                'customer_id': self.customer_id}

    def edit_click(self):
        status, message = OrderController.edit(self.order_id.variable.get(),
                                               self.quantity.variable.get(),
                                               self.unit_price.variable.get(),
                                               self.calendar.gregorian_date,
                                               self.total_price.variable.get(),
                                               int(self.product_id.variable.get()),
                                               int(self.customer_id.variable.get()))
        self.reset_form()
        if status:
            msg.showinfo("Edit", "Edited successfully!")
        else:
            msg.showerror("Error", message)

    def reset_click(self):
        self.order_id.variable.set("")
        self.quantity.variable.set("")
        self.unit_price.variable.set("")
        self.total_price.variable.set("")
        self.product_id.variable.set("")

    def remove_click(self):
        status, message = OrderController.remove(self.order_id.variable.get())
        self.reset_form()
        if status:
            msg.showinfo("Remove", "record deleted successfully!")
        else:
            msg.showerror("Error", message)

    def previous_page(self):
        self.win.destroy()
        from view.customer_main_view import CustomerMainView
        customer_main_view = CustomerMainView(self.customer)

    def confirm_order_click(self):
        msg.showinfo("Confirm","Order saved successfully!")

    def calc_total_amount(self):
        status, total_amount = OrderController.total_amount(self.customer_id.variable.get())
        if status:
            return Label(self.win, text=total_amount, font=("Arial",12)).place(x=400, y=385)


    def close_win(self):
        self.win.destroy()
        main_view = CustomerMainView(self.customer)

    def __init__(self, customer):
        self.customer = customer
        self.win = Tk()
        self.win.configure(bg="Ghost White")
        self.win.protocol("WM_DELETE_WINDOW", self.close_win)

        self.win.title("Cart")
        self.win.geometry("880x450")

        Label(self.win, text="Please check your cart", font=("Arial", 15),fg="forest green", bg="Ghost White").place(x=30, y=25)
        self.customer_id = TextWithLabel(self.win, 'CustomerID', 30, 70, 70, disabled=True)
        self.customer_id.variable.set(f"{self.customer[0].customer_id}")
        self.order_id = TextWithLabel(self.win, 'OrderID', 30, 110, 70, disabled=True)
        self.product_id = TextWithLabel(self.win, 'Product ID', 30, 150, 70, disabled=True)
        self.unit_price = TextWithLabel(self.win, 'Unit Price', 30, 190, 70, disabled=True)
        self.quantity = TextWithLabel(self.win, 'Quantity', 30, 230, 70, disabled=False)
        self.total_price = TextWithLabel(self.win, 'Total Price', 30, 270, 70, disabled=True)
        Label(self.win, text="OrderDate",bg="Ghost White").place(x=30, y=315)
        self.calendar = PersianCalendar(self.win, 100, 315)

        self.table = Table(self.win,
                           ['Order ID', 'Quantity', 'Unit Price', 'OrderDate', 'TotalPrice', 'Product Id'],
                           [80, 60, 120, 120, 120, 80],
                           260,
                           30,
                           self.select_row,
                           15)

        Button(self.win, text='Edit', width=11, bg="Pale Green", command=self.edit_click).place(x=30, y=360)
        Button(self.win, text='Remove', width=11, bg="Pale Green", command=self.remove_click, height=1).place(x=140, y=360)
        Button(self.win, text='Reset', width=11, bg="Pale Green", command=self.reset_click).place(x=30, y=390)
        Button(self.win, text='Previous page', width=11, bg="Pale Green", command=self.previous_page).place(x=140, y=390)
        Button(self.win, text='Confirm order', width=14, height=2, bg="forest green", font=("Arial", 12),
               command=self.confirm_order_click).place(x=700, y=370)

        Label(self.win, text="Total Amount:", font=("Arial", 14), fg="black",bg="Ghost White").place(x=280, y=380)

        self.reset_form()

        self.win.mainloop()
