from tkinter import Label, Entry, Button, Tk
from login_signup import *

class UI:
    def __init__(self):
        box = Tk()
        box.title("E-crypt login form")
        box.minsize(400, 400)

        Label(box, text="Email :").pack(pady=(20, 5))
        email_line = Entry(box, width=25)
        email_line.pack_configure(pady="5",ipady="1")

        Label(box, text="Password :").pack()
        password_line = Entry(box, show="*", width=25)
        password_line.pack_configure(pady="5",ipady="1")

        l_s = login_signup()

        def login_clicked():
            email = email_line.get()
            password = password_line.get()
            box.destroy()
            l_s.login(email,password)

        def signup_clicked():
            email = email_line.get()
            password = password_line.get()
            box.destroy()
            l_s.signup(email,password)

        log_in = Button(box, text="Login", command=login_clicked, width=8).pack(pady=(20, 5))
        sign_up = Button(box, text="Sign Up", command=signup_clicked, width=8).pack()

        Label(box, text="project@6th_sem").pack(side="bottom")

        box.mainloop()


if __name__ == '__main__':
    UI()
