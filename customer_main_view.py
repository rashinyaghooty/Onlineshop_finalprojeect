from tkinter import *


class CustomerMainView:
    def profile_click(self):
        self.win.destroy()
        from view.customer_profile_view import CustomerProfileView
        customer_profile_view = CustomerProfileView(self.customer)

    def products_list(self):
        self.win.destroy()
        from view.customer_product_list_view import CustomerProductListView
        customer_product_list_view = CustomerProductListView('product', self.customer)

    def cart_click(self):
        self.win.destroy()
        from view.customer_cart_view import CustomerCartView
        customer_cart_view = CustomerCartView(self.customer)

    def __init__(self, customer):
        self.customer = customer
        self.win = Tk()
        self.win.configure(bg="Ghost White")
        self.win.geometry("250x300")
        self.win.title("Customer Panel")

        print(customer)
        Label(text=f"Welcome to your panel {customer[0].username}!", font=("Arial", 11), bg="Ghost White").place(x=25, y=20)

        Button(self.win, text="Profile", width=15, bg="forest green", height=2, font=("Arial", 13),
               command=self.profile_click).place(x=50, y=70)
        Button(self.win, text="Products", width=15, bg="Pale Green", height=2, font=("Arial", 13),
               command=self.products_list).place(x=50, y=140)
        Button(self.win, text="Cart", width=15, bg="sea green", height=2, font=("Arial", 13), command=self.cart_click).place(x=50, y=210)

        self.win.mainloop()

#customer = Customer("rashin","rashin12")
#customer_view = CustomerMainView('customer')
