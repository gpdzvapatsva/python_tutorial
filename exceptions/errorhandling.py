from tkinter import *
from tkinter import messagebox
def error_check(x):
    try:

        if x<3000:
            raise  ValueError("Please deposit more money to qualify")
        else:
           messagebox.showinfo (title="STATUS FEEDBACK", message="Congratulations. You qualify to go to Malaysia")
    except ValueError as e:
        messagebox.showinfo(title="STATUS FEEDBACK",message=e)
def new_window():
    root = Tk()
    root.title("Exception handling: ")
    root.geometry("200x200")
    my_amount=Label(root, text="Please enter amount in your account")
    my_amount.place(x=20, y=10)
    my_amount_entry=Entry(root)
    my_amount_entry.place(x=20, y=35)
    error_check(5000)
    check_button = Button(root, text="Check qualification", bg='magenta', command=error_check)
    check_button.place(x=20, y=65)
    root.mainloop()