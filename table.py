from tkinter import ttk, END


class Table:
    def __init__(self, master, headers, widths, x, y, select_function, height):
        self.master = master
        self.x = x
        self.y = y
        self.headers = headers
        self.widths = widths
        self.select_function = select_function
        self.height = height
        self.columns = list(range(len(headers)))

        self.table = ttk.Treeview(self.master, columns=self.columns, show="headings", height=self.height)
        for col in self.columns:
            self.table.column(col, width=self.widths[col])
            self.table.heading(col, text=self.headers[col])

        self.table.bind("<ButtonRelease>", self.select_table)
        self.table.bind("<KeyRelease>", self.select_table)
        self.table.place(x=x, y=y)

    def refresh_table(self, data_list):
        for item in self.table.get_children():
            self.table.delete(item)

        if data_list:
            for data in data_list:
                self.table.insert("", END, values=tuple(data.to_dict().values()))

    def select_table(self, event):
        data = self.table.item(self.table.focus())["values"]
        self.select_function(data)




