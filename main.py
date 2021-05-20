# OOP Task 1 - Easy Tickets
# Designing a program that allows you to purchase tickets
# using your cellphone number
from tkinter import *
import tkinter.ttk as ttk


# Creating a window and adding a title and background colour
window = Tk()
window.title("Ticket Sales")
window.geometry("500x300")
window.config(bg="yellow")
window.resizable(0, 0)


# Adding a class called TicketSales
class TicketSales:
    output = StringVar()

    def __init__(self, root): # Initializing my window
        # Creating a label and entry to input cell number
        self.lbl_cell = Label(root, text="Enter your cell number: ", bg="yellow")
        self.lbl_cell.grid(row=0, column=0, padx=10, pady=10)
        self.cell_ent = Entry(root)
        self.cell_ent.grid(row=0, column=1, padx=15, pady=15)
        # Creating a label and combobox to select the category
        self.lbl_category = Label(root, text=" Please select a category:", bg="yellow")
        self.lbl_category.grid(row=1, column=0)
        self.category_box = ttk.Combobox(root, textvariable="Category")
        self.category_box["values"] = "Select-- Soccer Movies Theatre"
        self.category_box.current(0)
        self.category_box.grid(row=1, column=1)
        # Creating a label and entry box to enter amount of tickets
        self.lbl_tickets = Label(root, text="Please select number of tickets: ", bg="yellow")
        self.lbl_tickets.grid(row=2, column=0, padx= 10, pady=15)
        self.ticket_entry = Entry(root, textvariable="Tickets")
        self.ticket_entry.grid(row=2, column=1)

        # Creating Calculate and Clear Button
        self.calc_btn = Button(root, text="Calculate Ticket", bg="red", borderwidth=10,  command=self.price_ticket)
        self.calc_btn.grid(row=3, column=0)
        self.lbl_result = Label(root, textvariable= self.output, bg="yellow")
        self.lbl_result.grid(row=5, column=0, padx=10, pady=10)
        self.clear_btn = Button(root, text="Clear Entries", bg="red", borderwidth=10, command=self.clear_entries)
        self.clear_btn.grid(row=3, column=1)

# defining function to calculate ticket price

    def ticket_amount(self):
        ticket_amount = 0
        if self.category_box.get() == "Soccer":
            ticket_amount = 45
        elif self.category_box.get() == "Movies":
            ticket_amount = 75
        elif self.category_box.get() == "Theatre":
            ticket_amount = 100
        else:
            pass
        return ticket_amount


# To assign ticket price
    def price_ticket(self):
        amount_payable = int(self.ticket_entry.get()) * self.ticket_amount()
        vat = amount_payable*15/100
        ticket_cost = vat + amount_payable
        self.output.set("Amount owed " + str(ticket_cost) + "\n" +
                        "Reservation for " + self.category_box.get() + " for " + self.ticket_entry.get() + " tickets " + " \n " +
                         " was done by " + self.cell_ent.get())

# A function to clear all entries
    def clear_entries(self):
        self.cell_ent.delete(0, END)
        self.category_box.delete(0, END)
        self.ticket_entry.delete(0, END)


# To run the code and window
obj_ts = TicketSales(window)
window.mainloop()
