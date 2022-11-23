from tkinter import *
from tkinter import messagebox
login_screen=Tk()
login_screen.title('Authentification')
login_screen.geometry("300x250")
Label(login_screen, text="Please enter login details").pack()
Label(login_screen, text="").pack()
Label(login_screen, text="Username").pack()
username_login_entry = Entry(login_screen, textvariable="username")
username_login_entry.pack()
Label(login_screen, text="").pack()
Label(login_screen, text="Password").pack()
password__login_entry = Entry(login_screen, textvariable="password", show='*')
password__login_entry.pack()
def verify():
    all_users={"user_1":"pass_1","user_2":"pass_2", "user_3":"pass_3", "user_4":"pass_4"}
    username=username_login_entry.get()
    password=password__login_entry.get()
    if (username, password) in all_users.items():
        #Label(login_screen, text="correct login").pack()
        messagebox.showinfo(title="Login in details",message="Correct")

        login_screen.withdraw()
        import errorhandling
        errorhandling.new_window()
    else:
        messagebox.showinfo("Error", "Incorrect login please try again")
        password__login_entry.delete(0, END)
        username_login_entry.delete(0, END)

Button(login_screen, text="Login", width=10, height=1, bg="magenta", command=verify).pack()





login_screen.mainloop()