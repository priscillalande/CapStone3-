#login code

from datetime import date, datetime

use_dictionary = {}
with open("user.txt", mode ="r") as user_file:
    for line in user_file:
        User_name, password = line.strip('\n').split(", ")
        use_dictionary[User_name.lower()] = password

username = input("please enter your user name: ").lower()
while not username in use_dictionary:
    print('Invalid user name') 
    username = input("please enter your user name: ").lower()

password= input("please enter your user password: ")
while password != use_dictionary[username]:
    print('Invalid user password') 
    password= input("please enter your user password: ")

while True:
    #menue
    if username == 'admin':
            menue = input('''Select one of the following options:
    r - register user
    a - add task
    va - view all tasks
    vm - view my tasks
    d - display statistics = Total number of tasks & users
    e - exit
    : ''')
    else:
        menue = input('''Select one of the following options:
    a - add task
    va - view all tasks
    vm - view my tasks
    e - exit
    : ''')

    #user choice of menue
    if menue.lower() == 'r' and username == 'admin':

        new_user = str(input('New User Name required :'))
        new_password = (input ('New password required :'))
        confirmation = (input('please confirm newly entered passoword :'))
        
        if new_password == confirmation :

            print('You have made invalid selection. Try again') 
            f = open ("user.txt", mode="a" )
            f.write ('\n'+ new_user + ", " + new_password)
            f.close()

    elif menue.lower() == 'a':

            User_task = str(input('Enter name of person task is assigned to ? :'))
            task_assignment = input ('Enter tittle of the task ' )
            Description_assignment = input('Input the description of the task at hand ' )
            due_date = input ('Due date ')
            assignment_date = date.today()
            task_completed = ("No")


            f = open ("tasks.txt", mode= "a" )
            f.write ('\n'+ User_task + ", " + task_assignment + ", " + Description_assignment  + ", " + str(assignment_date) + ", " + due_date +  ", " + task_completed)
            f.close()
        

    elif menue.lower() == 'va':

        with open("tasks.txt", mode ="r") as user_file:
            for line in user_file:
                User_name, task_title, task_descrip, date_assingned, due_date, task_completion = line.strip('\n').split(", ")
                print("Task:\t\t"+task_title)
                print('Assigned to:\t'+User_name)
                print ('Date Assigned :\t'+ date_assingned)
                print ('Due date :\t'+ due_date)
                print ('Task Complete :\t' + task_completion)
                print ('Task description : \t' + task_descrip)
    

    elif menue.lower() == 'vm':
        with open('tasks.txt', 'r') as user_file:
            for line in user_file:
                User_name, task_title, task_descrip, date_assingned, due_date, task_completion = line.strip('\n').split(", ")
                if username == User_name:
                    print("Task:\t\t"+task_title)
                    print('Assigned to:\t'+User_name)
                    print ('Date Assigned :\t'+ date_assingned)
                    print ('Due date :\t'+ due_date)
                    print ('Task Complete :\t' + task_completion)
                    print ('Task description : \t' )   

    elif menue.lower() == 'e':      
        print("Thank you, Enjoy your day.")
        break
    
    elif menue.lower() == 'd' and username == 'admin':

        admin_menu = (input("""
                Please select one of the following options:
                r - register a new user
                d - display statistics = Total number of tasks & users
                e - exit
                """))

        tasks_num = 0
        users_num = 0

        with open("tasks.txt", "r") as task_file:
            for line in task_file:
                    tasks_num += 1
            print (f"\nTotal number of tasks: {tasks_num}")

            with open("user.txt", "r") as username:
                for line in username:
                    users_num += 1
            print (f"Total number of users: {users_num}")
            print ("Thanks have an awesome day")

            #importing current date
            from datetime import datetime
            #opening user file
            user_file = open("user.txt", "r+")

            login = False
            #while login is false,
            #if user enters correct credentials, login
            #changes to True. Giving exccess
        while login == True:

            username = input("Enter your username: ")
            password = input("Enter your password: ")

        for lines in user_file:
            valid_user, valid_password = lines.split(", ")

            if valid_user == username and valid_password == password:
                login = True
                print("Logging in...")
            if valid_user != username and valid_password != password:
                print("Invalid login details")
                user_file.seek(0)
                user_file.close()
        #choices for the user to choose from
        choices = input('''Select option one below:
            r - register username
            a - add task
            va - view all tasks
            vm - view my tasks
            e - exit
            s - stats
            ''')

        #if user selects admin selects "r" he can
        #register a user to user_file
        def reg_user():
            if username == "admin":
                new_userLogin = False
                new_usersName = input("Enter username: ")
                regstr = open("user.txt", "r+")
                v_user, v_password = lines.split(", ")


            while new_userLogin == False:
                if new_usersName != v_user:
                    new_userPass = input("Enter password: ")
                    validate = input("Confirm password: ")
                elif new_usersName == v_user:
                    print("That username is unavailable. Pick another one")
                    new_usersName = input("Enter username: ")
                    new_userPass = input("Enter password: ")
                    validate = input("Confirm password: ")
                if new_userPass == validate:
                    new_userLogin = True
                if new_userPass != validate:
                    print("password did not match. Try again")
                if new_userPass == validate:
                    print("password matches. New user created")
                append_me = open("user.txt", "a")
                append_me.write("\n" + str(new_usersName) + ", " + str(validate))
                append_me.close()
                if username != "admin":
                    print("Only admin can add a new user.")
                if choices == "r":
                    register = reg_user()
                    print(register)

        def add_task():

            tasks = open("tasks.txt", "a")
            assignee = input("Enter the usersname of assignee: ")
            title = input("Enter the title of the task: ")
            description = input("Enter task description: ")
            due_date = input("Enter task due date: ")
            date = datetime.now()
            completed = "no"

            tasks.write(str(assignee) + ", " + str(title) + ", " + str(description) + ", " + str(due_date)+ ", " + str(date) + ", " + str(completed) + "\n")
            tasks.close
            if choices == "a":
                adding_task = add_task()
                print(adding_task)
        #if user selects "va" he will be given info
        #of every file in an easy to read format
        def view_all():
            tasks_file = open("tasks.txt", "r+")
        #loop to print out details in proper manner
            for line in tasks_file:
                assignee, title, description, due_date, date, completed = line.split(", ")
                print(f'''
            Name: {assignee}
            Title: {title}
            Description: {description}
            Due Date: {due_date}
            Date Assigned: {date}
            Task Complete: {completed}
            ''')
            tasks_file.close()
            if choices == "va":
                all_view = view_all()
                print(all_view)
    #if user selects "vm" program
    #will desplay specific user task
    def view_mine():
        view = open("tasks.txt", "r")
        task_num = 0

        username = input("Please enter the username which you want to view the tasks for?\n")

        for row in view:
                all_items = row.strip().split(",")
        task_num += 1
        if username == all_items[0]:
            print(f'''
            task number:{task_num} 
            ''')

        if choices == "vm":
            my_view = view_mine()
            print(my_view)

    #if the user selects "e" program
    #breaks
        if choices == "e":
            print("closing program...")
            breakpoint

    #if user selects "s". number of tasks and
    #number of users are displayed
    if choices == "s":
        stats_file = open("tasks.txt", "r+")
        other_stats = open("tasks.txt", "r+")
    if username == "admin":

        num_title = 0
        num_assignee = 0
    for line in stats_file:
        assignee, title, description, due_date, date, completed = line.split(", ")
        assignee
        num_assignee += 1
        print(f'''
    Total number of users: {num_assignee}
    ''')
        stats_file.close

    for title in other_stats:
        assignee, title, description, due_date, date, completed = title.split(", ")
        title
        num_title += 1
        print(f'''
    Total number of tasks: {num_title}
    ''')
    other_stats.close()