from tkinter import *
import csv

root = Tk()

#*****************variables**********************


name_var = StringVar()
price_var = StringVar()


#*************************GUI functions**********************


def submit():
    name = name_entry.get()
    price_stock = price_var.get()

    with open('stock_prices.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, price_stock])

    #resets the entry fields
    name_var.set("")
    price_var.set("")


#************************ GUI compentents********************


#creating a label for company and iserting it on page
name_label = Label(root, text="company")
name_label.grid(row=0, column=0)

#company name entry and insert
name_entry = Entry(root, textvariable = name_var)
name_entry.grid(row=0, column=1)

#stock price of company label
price_label = Label(root, text="stock price")
price_label.grid(row=1, column=0)

#stock price of company entry
price_entry = Entry(root, textvariable=price_var)
price_entry.grid(row=1, column=1)

#submit button
submit_button = Button(root, text="submit", command=submit)
submit_button.grid(row=2, column=1)


#****************** END **********************


root.mainloop()
