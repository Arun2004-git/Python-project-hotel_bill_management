import json
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Treeview
from print import save_frame_as_image

def print1():
    save_frame_as_image(f2, filename="E://image/bill1.png")

def load_menu():
    try:
        with open("menu.json", "r") as file:
            menu = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        menu = {}
    return menu

def display_menu():
    for widget in f.winfo_children():
        widget.destroy()
    Label(f, text="Menu", font=("Gabriola", 25, "bold"), fg="black", bg="lightgreen").pack()
    Button(root, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Edit", command=edit).place(x=100,y=600)
    for item, price in menu.items():
        Label(f, text=f"{item} . . . Rs.{price}/plate", font=("Lucida Calligraphy", 15, 'bold'), bg="lightgreen", fg="black").pack(anchor="w")

a = []
b1 = []

def cal_menu():
    for widget in f1.winfo_children():
        widget.destroy()
    a.clear()
    Button(root, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Reset", command=reset).place(x=450,y=600)
    Button(root, bd=5, fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, text="Total", command=total).place(x=650,y=600)
    
    for index, item in enumerate(menu.keys()):
        Label(f1, text=f"{item}", font=("aria", 20, "bold"), width=12, fg="blue4").grid(row=index, column=0, sticky="w")
        entry_var = StringVar()
        a.append(entry_var)
        Entry(f1, font=("aria", 20, "bold"), bd=6, textvariable=entry_var, width=8, bg="lightpink").grid(row=index, column=1)

def total():
    cost = 0
    b1.clear()  
    for i in a:
        try:
            quantity = int(i.get())
        except ValueError:
            quantity = 0
        b1.append(quantity)

    col=('Menu','Price','Quantity','Total')
    table=Treeview(f2,columns=col,show="headings")
    table.heading("Menu",text="Menu")
    table.heading("Price",text="Price")
    table.heading("Quantity",text="Quantity")
    table.heading("Total",text="Total")

    table.column("Menu",anchor="center",width=100)
    table.column("Price",anchor="center",width=60)
    table.column("Quantity",anchor="center",width=60)
    table.column("Total",anchor="center",width=80)
    table.grid(row=1,column=0)
    s=ttk.Style()
    s.configure("Treeview",font=("Arial",10,'bold'))
    c=2    
    for q,item, price in zip(b1,menu.keys(),menu.values()):
        if q>0:
            table.insert("","end",values=(item,price,q,price*q))
            #Label(f2, text=f"{item}       Rs.{price}     x    {q}    =     {price*q}", font=("Arial", 15, 'bold'), bg="lightgreen", fg="black").grid(row=c,column=0)
            c=c+1
   
    for i, j in zip(b1, menu.values()):
        cost += i * j
    Label(f2, text='Total', font=("aria", 25, 'bold'), fg="lightyellow", bg='black').grid(row=25,column=0)
    Entry(f2, font=("aria", 20, "bold"), textvariable=b, bd=6, width=12, bg="lightpink").grid(row=26,column=0)

    b.set(f"Rs. {cost:.2f}")
    pb = Button(root, text="Print Frame", fg="black", bg="lightblue", font=("ariel", 16, "bold"), width=10, command=print1)
    pb.place(x=850,y=600)

    
def reset():
    for e in a:
        e.set("")

def edit():
    def save_menu(menu):
        with open("menu.json", "w") as file:
             json.dump(menu, file, indent=4)

    def add_item():
        name = entry_name.get().strip()
        price = entry_price.get().strip()
        if name and price.isdigit():
            menu[name] = int(price)
            save_menu(menu)
            display_menu()
            cal_menu()
            entry_name.delete(0, END)
            entry_price.delete(0, END)
            messagebox.showinfo("Success", f"'{name}' added successfully.")
        else:
            messagebox.showwarning("Invalid Input", "Please enter a valid item name and price.")

    def update_item():
        name = entry_name.get().strip()
        price = entry_price.get().strip()
        if name in menu and price.isdigit():
            menu[name] = int(price)
            save_menu(menu)
            display_menu()
            cal_menu()
            entry_name.delete(0, END)
            entry_price.delete(0, END)
            messagebox.showinfo("Success", f"'{name}' updated successfully.")
        else:
            messagebox.showwarning("Invalid Input", "Item not found or invalid price.")

    def remove_item():
        name = entry_name.get().strip()
        if name in menu:
            del menu[name]
            save_menu(menu)
            display_menu()
            cal_menu()
            entry_name.delete(0, END)
            entry_price.delete(0, END)
            messagebox.showinfo("Success", f"'{name}' removed successfully.")
        else:
            messagebox.showwarning("Invalid Input", "Item not found in menu.")

    def close():
        edit_frame.destroy()
    
    edit_frame = Frame(root, width=200, height=200,bg="beige")
    edit_frame.place(x=320, y=10)

    bt=Button(edit_frame,font=("ariel",10,'bold'),bg="khaki",width=10,text="Close",command=close)
    bt.grid(row=4, column=0, columnspan=2, pady=10)
    
    Label(edit_frame, text="Item Name:", font=("Arial", 12,'bold'),bg="beige").grid(row=0, column=0, pady=10, padx=5)
    entry_name = Entry(edit_frame, font=("Arial", 12,"bold"),bg="lightyellow")
    entry_name.grid(row=0, column=1, pady=10, padx=5)

    Label(edit_frame, text="Price:", font=("Arial", 12,'bold'),bg="beige").grid(row=1, column=0, pady=10, padx=5)
    entry_price = Entry(edit_frame, font=("Arial", 12,"bold"),bg="lightyellow")
    entry_price.grid(row=1, column=1, pady=10, padx=5)

    Button(edit_frame, text="Add Item", font=("Arial", 10,'bold'),bg="khaki", command=add_item, width=10).grid(row=2, column=0, pady=10, padx=5)
    Button(edit_frame, text="Update Item", font=("Arial", 10,'bold'),bg="khaki", command=update_item, width=10).grid(row=2, column=1, pady=10, padx=5)
    Button(edit_frame, text="Remove Item", font=("Arial", 10,'bold'),bg="khaki", command=remove_item, width=10).grid(row=3, column=0, columnspan=2, pady=10)



root = Tk()
root.attributes("-topmost", True)
root.geometry("1250x750")
root.title("Bill Management")

menu = load_menu()

Label(text="Hotel Bill Management System", bg="black", fg="white", font=("calibri", 33), width="300", height="2").pack()

f_canvas = Canvas(root, bg="lightgreen", highlightbackground="black", highlightthickness=1, width=350, height=450)
f_scrollbar = Scrollbar(root, orient="vertical", command=f_canvas.yview)
f = Frame(f_canvas, bg="lightgreen")
f.bind("<Configure>", lambda e: f_canvas.configure(scrollregion=f_canvas.bbox("all")))
f_canvas.create_window((0, 0), window=f, anchor="nw")
f_canvas.configure(yscrollcommand=f_scrollbar.set)
f_canvas.place(x=10, y=118)
f_scrollbar.place(x=410, y=118, height=450)

display_menu()

# Frame `f1` with Scrollbar
f1_canvas = Canvas(root, bd=5, highlightbackground="black", highlightthickness=1, width=400, height=450, relief=RAISED)
f1_scrollbar = Scrollbar(root, orient="vertical", command=f1_canvas.yview)
f1 = Frame(f1_canvas)
f1.bind("<Configure>", lambda e: f1_canvas.configure(scrollregion=f1_canvas.bbox("all")))
f1_canvas.create_window((0, 0), window=f1, anchor="nw")
f1_canvas.configure(yscrollcommand=f1_scrollbar.set)
f1_canvas.place(x=427, y=118)
f1_scrollbar.place(x=827, y=118, height=450)

cal_menu()

b = StringVar()

f2_canvas = Canvas(root, bg="lightyellow", highlightbackground="black", highlightthickness=1, width=420, height=450)
f2_scrollbar = Scrollbar(root, orient="vertical", command=f2_canvas.yview)
f2 = Frame(f2_canvas, bg="lightyellow")
f2.bind("<Configure>", lambda e: f2_canvas.configure(scrollregion=f2_canvas.bbox("all")))
f2_canvas.create_window((0, 0), window=f2, anchor="nw")
f2_canvas.configure(yscrollcommand=f2_scrollbar.set)
f2_canvas.place(x=840, y=118)
f2_scrollbar.place(x=1240, y=118, height=450)

Label(f2, text='Bill', font=("calibri", 25), fg='black', bg="lightyellow").grid(row=0,column=0)

root.mainloop()                
