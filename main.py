# Author: Joshua Parker
from tkinter import *

root = Tk()

label = Label(root, "Welcome to your password handbook")
root.mainloop()
appname = []
username = []
password = []
end = "no"

name = input("Please Enter your first and last name: ")
print ("\nWelcome to %s\'s Password Handbook Creator." % (name))
while (end != "no" or end != "No" or end != "NO" or end != "nO"):
    appn = input("Please enter the Website or Application name(ex. Wellsfargo.com): ")
    usern = input("Please enter your username: ")
    passw = input("Please enter your password: ")

    appname.append(appn)
    username.append(usern)
    password.append(passw)
    end = input("\nDo you want to create more entries: ")

print("\nThanks for using my program")
