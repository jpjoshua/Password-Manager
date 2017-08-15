

def output(appname, username, password, comment):
    """This writes the 3 variables to a file."""
    file.write("appname: %s " %(appname) + "\n")
    file.write("username: %s " %(username) + "\n")
    file.write("password: %s " %(password) + "\n")
    if (comment == ""):
        comment = "N/A"
        file.write("Comments: %s " %(comment) + "\n")
    else:
        file.write("Comments: %s " %(comment) + "\n")
    file.write("***********************************\n")

def resume_input():
    global file
    with open("%s.txt" % (name), "a") as file:
        output(appname, username, password, comment)

def update_entry():

    """ Main Program """
end = "no"
name = input("Please Enter your first and last name: ")
file = open("%s.txt" % (name), "w+")
print("\nWelcome to %s\'s Password Handbook Creator." % (name))
file.write("%s\'s Password Handbook" % (name) + "\n")
file.write("***********************************\n")
ans1 = input("Do already have a password file (yes or no)? ")
ans2 = input("DO you want to add to an existing file (yes or no)? ")
ans3 = input("Do you want to update one of your entries (yes or no)? ")
print("\nIf you dont have an answer to the prompt, hit the enter button.")


while (end.lower() == "no" or end.lower() == "n"):
    appname = input("Please enter the Website or Application name(ex. Wellsfargo.com): ")
    username = input("Please enter your username: ")
    password = input("Please enter your password: ")
    comment = input("Please enter your comment: ")
    output(appname, username, password, comment)
    end = input("Are you done typing in entries (yes or no)? ")

file.close()
