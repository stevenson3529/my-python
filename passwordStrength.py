'''
A program that tests how strong a password is.
'''

from tkinter import Tk, simpledialog, messagebox
root = Tk()
root.withdraw()

weakPasswords = {'password','PASSWORD','PassWord','Password','password123','qwerty','qwertyuiop','qwerty123','pass word'}


while True:
    password = simpledialog.askstring("Enter password","What is your password?")
    if password in weakPasswords:
        messagebox.showwarning("Weak password","Your password is easy to guess. Create one that is not commonly used.")
    elif password == None:
        messagebox.showinfo("Goodbye","Thank you for using this Password Strength Checker. Press OK to exit.")
        break
    elif password.isalpha() == True:
        messagebox.showwarning("Weak password","Your password is quite weak. Try adding numbers or special characters.")
    elif len(password) < 8:
        messagebox.showwarning("Weak password","Your password is quite weak. Try making it longer.")
    else:
        messagebox.showinfo("Good password","Your password is strong.")

