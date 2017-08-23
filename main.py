import sys

def main():
    print("Please enter a number to start:")
    print("1) Make new file")
    print("2) Begin at the end of another file")
    print("3) Update a file entry")
    print("4) Exit")

    choice = input("Choice: ")
    if (choice == "1"):
        new_file()
        quit_program()

    elif (choice == "2"):
        resume_input()
        quit_program()

    elif (choice == "3"):
        update_entry()
        quit_program()

    elif(choice == "4"):
        quit_program()

    else:
        print("Choose a valid option.")
        main()

def new_file():
    global name
    file = open("%s.txt" % (name), "w")
    file.write("\n%s\'s Password Handbook" % (name) + "\n")
    file.write("***********************************\n")
    output(file)
    file.close()

def output(file):
    """This writes the 4 variables to a file."""
    end = "no"
    while (end.lower() == "no"):
        print("\n")
        print("\nIf you don't have an answer to the prompt, hit the enter button.")
        appname = input("Please enter the Website or Application name(ex. Wellsfargo.com): ")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        comment = input("Please enter your comment: ")

        file.write("appname: %s " % (appname) + "\n")
        file.write("username: %s " % (username) + "\n")
        file.write("password: %s " % (password) + "\n")

        if (comment == ""):
            comment = "N/A"
            file.write("Comments: %s " % (comment) + "\n")
        else:
            file.write("Comments: %s " % (comment) + "\n")

        file.write("***********************************\n")
        end = input("Are you done typing in entries (yes or no)? ")

def output(file, line_number, data_):
    """This writes the 4 variables to a file."""
    end = "no"
    new_data = []
    while (end.lower() == "no"):
        print("\n")
        print("\nIf you don't have an answer to the prompt, hit the enter button.")
        appname = input("Please enter the Website or Application name(ex. Wellsfargo.com): ")
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        comment = input("Please enter your comment: ")

        new_data.append("appname: %s " % (appname) + "\n")
        new_data.append("username: %s " % (username) + "\n")
        new_data.append("password: %s " % (password) + "\n")
        # file.write("appname: %s " % (appname) + "\n")
        # file.write("username: %s " % (username) + "\n")
        # file.write("password: %s " % (password) + "\n")

        if (comment == ""):
            comment = "N/A"
            # file.write("Comments: %s " % (comment) + "\n")
            new_data.append("Comments: %s " % (comment) + "\n")
        else:
            # file.write("Comments: %s " % (comment) + "\n")
            new_data.append("Comments: %sJoshua Parker " % (comment) + "\n")

        new_data.append("***********************************\n")
        end = input("Are you done typing in entries (yes or no)? ")
    index = 0
    for line in new_data:
        data_.insert(line_number + index, line)
        index+=1
    for line in data_:
        file.write(line)

def resume_input():
    # need try catch fo file not found error
    filename = input("Please enter the exact file name: ")
    testVar = "%s.txt" % (filename.strip())
    with open(testVar, "r") as file:
        data = file.readlines()
        index_ = 0
        for line in data:
            index_+=1
            if(line.__contains__("Note Section:")):
                index_-=2
                line = data[index_]
                file.close()
                with open(testVar, "w") as file:
                    output(file, index_, data)
                    break
        # if (data == "Note Section:"):
        #     for line in data:
        #         if line == "Note Section:":
        #             new_data = output(file) + line
        #             file.write(new_data)
        else:
            output(filename)
            add_note(filename)

def update_entry():
    pass

def add_note(file):
    # ask user at end of entering entries if they want to add a note section
    # add a new line after ** line to allow space for a note section
    # if note section exists resume input if it exists
    add_note = input("Do you want to add a note section? ")
    while True:
        if (add_note.lower() == "no"):
            break
        elif (add_note == "yes"):
            end = "no"
            while (end == "no"):
                note = input("Please enter only one sentence: ")
                file.write(note + "\n")
                end = input("Do you want to add another note? ")
        else:
            print("Input yes or no only!")
            add_note = input("Do you want to add a note section? ")

def quit_program():
    print("\nThank you for using the password manager!")
    sys.exit(0)

""" Program Starts Here """

name = input("Please enter your first and last name: ")
print("\nWelcome to %s\'s Password Handbook Creator." % (name))

main()
