#this program helps a business manage tasks assigned to each member of the team

#=====importing libraries===========
#learnt how to import time on phoenixapp.com
from datetime import date

#created open variables for the users and tasks
total_users = []
total_tasks = []

#====Login Section====
#the user will be prompted to enter their username and password
#the program reads usernames and passwords from the user.txt file
#used a while loop to validate the username and password
#if the details are correct, they will be able to access the menu
with open("user.txt", 'r+') as f:
    for line in f:
        total_users.append(line.split())

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        for i in range(len(total_users)):
            if username and password in total_users[i]:
                details = True

        if details == True:
            break
        else:
            print("Enter a valid username/ password.")

while True:
    #displays menu and converting the user's input to lower case
    #the admin gets displayed a different menu that allows them to view statistics
    if username == "admin":
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - display statistics
e - Exit
: ''').lower()

    #every other user gets displayed this menu
    else:
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    #only the admin can register users
    #if you aren't the admin, a message letting you know will be displayed
    #a new username and password are entered. the password is confirmed
    #if both passwords match, the registering was successful
    #if they don't, they get a message letting them know
    if menu == 'r':
        with open('user.txt', 'a+') as g:
            if username == "admin":
                new_username = input("Enter a new username: ")
                new_password = input("Enter new user's password: ")
                password_confirmation = input("Confirm new user's password: ")
                if new_password == password_confirmation:
                    print("User registered successfully")
                    g.write(f'\n{new_username}, {new_password}')
                elif new_password != password_confirmation:
                    print("Passwords do not match")

            else:
                print("Only admin can register new users.")

            g.close()

    #if they choose to add a new task
    #the details of the task are entered by the user
    #it is then written to the tasks.txt file
    elif menu == 'a':
        with open('tasks.txt', 'a+') as g:
            username = input("Assigned to? ")
            title = input("What is the title?: ")
            description = input("Enter task description: ")
            due_date = input("When is it due?: ")
            current_date = date.today()
            date_format = current_date.strftime("%d %b %Y")
            completion = "No"
            g.write(f'\n{username}, {title}, {description}, {due_date}, {date_format}, {completion}')

        g.close()

    #if they choose to view all tasks
    #all the tasks in tasks.txt file are displayed in a easy to read format using the index
    elif menu == 'va':
        with open("tasks.txt", 'r') as g:
            for viewing in g:
                contents = viewing.split(",")
                view_names = (f'''Tasks:\t\t\t\t {contents[1]}
Assigned to:\t\t {contents[0]}
Date assigned:\t\t {contents[3]}
Due date:\t\t\t {contents[4]}
Task Complete?\t\t {contents[5]}
Task description:\t {contents[2]}\n''')

                print(view_names)
            g.close()

    #if the user chooses to view their tasks
    #only their tasks are retreived using the index and username
    #the tasks are displayed in a easy to read format using the index
    elif menu == 'vm':
        with open("tasks.txt", 'r') as g:
            for viewing in g:
                contents = viewing.split(",")
                view_names = (f'''Tasks:\t\t\t\t {contents[1]}
Assigned to:\t\t {contents[0]}
Date assigned:\t\t {contents[3]}
Due date:\t\t\t {contents[4]}
Task Complete?\t\t {contents[5]}
Task description:\t {contents[2]}\n''')

                if contents[0] == username:
                    print(view_names)
            g.close()

    #if the admin chooses to view the statistics
    #the number of lines in both text files are retreived and displayed
    #only the admin has access to this operation
    elif menu == 's' and username == "admin":
        with open('user.txt', 'r') as g:
            users = len(g.readlines())

        with open('tasks.txt', 'r') as f:
            tasks = len(f.readlines())

        print(f'There are {tasks} tasks and {users} users')

    #if the user chooses to exit the program
    #the loop is exited
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    #if the user enters something that isn't on the menu
    #the message gets displayed
    else:
        print("You have made a wrong choice, Please Try again")