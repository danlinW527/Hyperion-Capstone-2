#====Login Section====

#create empty lists to store user and password#
user_list = []
password_list = []
user_file = open('user.txt', 'r')
for line in user_file:
#after split data in each line, define the first one as user
#and the second one as password. Add each data to the relevant lists
    user, password = line.split(', ')
    user_list.append(user)
    password_list.append(password.strip("\n"))

username = input('Enter the username: ')
#if the username entered is not in the list, ask the user to re-enter the username#
while not username in user_list:
        print('Invalid username. ')
        username = input('Enter the username: ')
#define the position of the user in the list to help locate the same position in the password list#
position = user_list.index(username)
password = input('Enter the password: ')
#if the entered password isn't equal to the one in the list
#ask the user to re-enter the password. Alternatively login successfully
while password != password_list[position]:
    print('Invalid password.')
    password = input('Enter the password: ')
print(f'Welcome, {username}')
user_file.close()

#====Menu Section====
while True:
    if username == 'admin':

    #presenting the menu to the user and
    # making sure that the user input is coneverted to lower case.
        menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
s - view the total number of tasks and users
e - Exit
: ''').lower()

        if menu == 'r':
            nusername = input('Enter a new username: ')
            npassword1 = input('Set up your password: ')
            npassword2 = input('Please confirm your password: ')
            while True:
            #if the 2nd password isn't equal to the first one,
            #ask the user to re-enter the 2nd password
                if npassword1 != npassword2:
                    print('Incorrect password.')
                    npassword2 = input('Please confirm your password: ')
                    continue
                else:
            #if the 2 passwords are the same, open the user text file in a+ mode
            #add the new user name and new password to the file
                    new_user = open('user.txt', 'a+')
                    new_user.write(f"\n{nusername}, {npassword1}")
                    print(f'{nusername} has been added successfully.')
                    new_user.close()
                    break

        elif menu == 'a':

            #if user select 'a' for adding task, ask user to input below information.

            assigned = input('Enter the username of the person whom the task is assigned to: ')
            title = input('Title of the task: ')
            description = input('Please describe the task: ')
            due = input('Enter the due date of the task, please use the format xx(date) Month xxxx(year): ')
            # open the tasks text file in a+ mode so that
            # the information user entered can be added to the tasks file
            task_file = open('tasks.txt', 'a+')
            task_file.write(f'\n{assigned}, {title}, {description}, 04 Jan 2023, {due}, No')
            task_file.close()
            continue

        elif menu == 'va':
            tasks_read = open('tasks.txt', 'r')
            data = tasks_read.readlines()
            for line in data:
                #split the data in each line
                split_data = line.split(', ')
                #create variable 'output' which store all the info and print them in one go#
                output = f'─────────────────────────────\n'
                output += '\n'
                #locate the data in the split_data list and assign it to it's category
                output += f'Task:\t\t\t\t{split_data[1]}\n'
                output += f'Assigned to: \t\t{split_data[0]}\n'
                output += f'Date assigned: \t\t{split_data[3]}\n'
                output += f'Due date:\t\t\t{split_data[4]}\n'
                output += f'Task complete?:\t\t{split_data[5]}'
                output += f'Task description:\t{split_data[2]}\n'
                output += '\n'
                output += f'─────────────────────────────\n'
                print(output)
            tasks_read.close()

        elif menu == 'vm':
            tasks_read = open('tasks.txt', 'r')
            data = tasks_read.readlines()
            for line in data:
                split_data = line.split(', ')
                #match the entered username with the 0 position in the splited data in the tasks file
                if username == split_data[0]:
                    output = f'─────────────────────────────\n'
                    output += '\n'
                    output += f'Task:\t\t\t\t{split_data[1]}\n'
                    output += f'Assigned to:\t\t{split_data[0]}\n'
                    output += f'Date assigned:\t\t{split_data[3]}\n'
                    output += f'Due date:\t\t\t{split_data[4]}\n'
                    output += f'Task complete?:\t\t{split_data[5]}'
                    output += f'Task description:\t{split_data[2]}\n'
                    output += '\n'
                    output += f'─────────────────────────────\n'
                    print(output)
            tasks_read.close()

        elif menu == 's':
        #open the user file in read mode and read each line
            user_read = open('user.txt', 'r')
            user_data = user_read.readlines()
        #as each user is stored in one line. The number of lines is equal to the number of users
            user_number = len(user_data)
        #open the task file in read mode and read each line
            tasks_read = open('tasks.txt', 'r')
            data = tasks_read.readlines()
        #same as above, the number of tasks is equal to the number of lines in tasks file
            task_number = len(data)
            print(f'The total number of the tasks is {task_number} and the total number of users is {user_number}')
            user_read.close()
            tasks_read.close()
        elif menu == 'e':
            print('Thank you for using the service, goodbye!!!')
            exit()

        else:
            print("You entered an incorrect choice, please try again")
            continue
    else:
        menu = input('''Select one of the following Options below:
        a - Adding a task
        va - View all tasks
        vm - view my task
        e - Exit
        : ''').lower()

        if menu == 'a':
            # if user select 'a' for adding task, ask user to input below information.

            assigned = input('Enter the username of the person whom the task is assigned to: ')
            title = input('Title of the task: ')
            description = input('Please describe the task: ')
            due = input('Enter the due date of the task, please use the format xx(date) Month xxxx(year): ')
            # open the tasks text file in a+ mode so that
            # the information user entered can be added to the tasks file
            task_file = open('tasks.txt', 'a+')
            task_file.write(f'\n{assigned}, {title}, {description}, 04 Jan 2023, {due}, No')
            task_file.close()
            continue

        elif menu == 'va':
            tasks_read = open('tasks.txt', 'r')
            data = tasks_read.readlines()
            for line in data:
                # split the data in each line
                split_data = line.split(', ')
                # create variable 'output' which store all the info and print them in one go#
                output = f'─────────────────────────────\n'
                output += '\n'
                # locate the data in the split_data list and assign it to it's category
                output += f'Task:\t\t\t\t{split_data[1]}\n'
                output += f'Assigned to: \t\t{split_data[0]}\n'
                output += f'Date assigned: \t\t{split_data[3]}\n'
                output += f'Due date:\t\t\t{split_data[4]}\n'
                output += f'Task complete?:\t\t{split_data[5]}'
                output += f'Task description:\t{split_data[2]}\n'
                output += '\n'
                output += f'─────────────────────────────\n'
                print(output)
            tasks_read.close()

        elif menu == 'vm':
            tasks_read = open('tasks.txt', 'r')
            data = tasks_read.readlines()
            for line in data:
                split_data = line.split(', ')
                # match the entered username with the 0 position in the splited data in the tasks file
                if username == split_data[0]:
                    output = f'─────────────────────────────\n'
                    output += '\n'
                    output += f'Task:\t\t\t\t{split_data[1]}\n'
                    output += f'Assigned to:\t\t{split_data[0]}\n'
                    output += f'Date assigned:\t\t{split_data[3]}\n'
                    output += f'Due date:\t\t\t{split_data[4]}\n'
                    output += f'Task complete?:\t\t{split_data[5]}'
                    output += f'Task description:\t{split_data[2]}\n'
                    output += '\n'
                    output += f'─────────────────────────────\n'
                    print(output)
            tasks_read.close()


        elif menu == 'e':
            print('Thank you for using the service, goodbye!!!')
            exit()

        else:
            print("You entered an incorrect choice, please try again")
            continue