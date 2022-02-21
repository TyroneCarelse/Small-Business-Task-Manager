from datetime import date

f = open("user.txt", "r")

users = []                                                                            # creating an empty list

while True:
    inp = f.readline()                                                                # to read a line from the text file
    if inp == "":                                                                     # if the end of the list reached, break
        break
    else:
        splitted = inp.split(", ")                                                    # split the characters in the list using a parameter
        length = len(splitted[1])                                                     # split the username and password according to position within the list
        splitted[1] = splitted[1].strip()         
        users.append(splitted[0])                                                     # appending to the new list with position 0 for username
        users.append(splitted[1])                                                     # appending to the new list with position 1 for passwordf.close()

print(users)

# User input required to verify username and password

while True:
    username = input("username: ")                                                   
    password = input("password: ")

    if username not in users:
        print("Entered username does not exist. \n")
        
# User input verified and navigates user to menu         
    elif username in users:
        ind = users.index(username)
        if password == users[ind+1]:
            print('\nPlease select one of the following options:\n'
                   'r - register user\n'
                   'a - add task\n'
                   'va - view all tasks\n'
                   'vm - view my tasks\n'
                   'e - exit')
            break
        
        else:
            print("Wrong password")
            
# User input required to choose an option to display
input_char = input("Please choose an option: ")

print("====================================================================================================================================================================================")

# This is the beginning of evaluating all the different options in the menu above. Every option is individually selected and either read and / or append to the relevant text files.
# Create a while loop to verify if user input match and append to file if new. Here the user selects the option to register a new user.
while True:
    if input_char == "r":
        username = input("Please enter a username: ")
        password = input("Please enter a password: ")
        password_confirm = input("Please confirm password: ")

        if password == password_confirm:                                                

            f = open("user.txt", "a")                                                   # using the append function to add new info to text file                                             
            f.write("\n"+ username + ", " + password_confirm)
            f.close()                                                                   # closing the file 
            print("User added successfully!")
            print("====================================================================================================================================================================================")

            break

        else:
            print("Password mismatch, please try again!")
            
# Here the user selects adding a task. We have to append the new information to the task text file.         
    elif input_char == "a":
        username = input("Please enter the username for this task: ")
        task_title = input("Please enter the title for this task: ")
        description = input("Please enter the description for this task: ")
        start_date = input("Please enter the start date of this task: ")
        due_date = input("Please enter the due date for this task: ")
        task_status = input("Has the task been completed? ")

        today = date.today()
        assigned_date = today.strftime('%d %b %Y')                                     # using the date function to store values in specific format

        f = open("tasks.txt", "a")
        f.write("\n"+ username + ", " + task_title + ", " + description + ", " + start_date + ", " + due_date + ", " + task_status)
        f.close()
        print("Task added successfully!")
        print("======================================================================================================================================================================================")
        break
    
# Here the user selects the option to view all tasks. Only the read function is required to perform this function. The information is organised so that the user can identify and read it easily.
    elif input_char == "va":

        f = open("tasks.txt", "r")
        tasks = []
        for i in f:
            j = i.split(", ")
            tasks.append(j)
            print("Task assigned to:" + j[0])
            print("Task title: " + j[1])
            print("Task Description: " + j[2])
            print("Task assigned date: " + j[3])
            print("Task due date: " + j[4])
            print("Task completed: " + j[5])
            print("============================================================================================================================================================================")

        break
        f.close()
        
# Here the user selects the option to view only the tasks of the user that is currently logged in. The information is organised so that the user can identify and read it easily. 
    elif input_char == "vm":
        f = open("tasks.txt", "r")
        for i in f:
            j = i.split(", ")
            if username == j[0]:
                print("User with username" + " " + j[0] + " " + "currently logged in")
                print(j[1] + " " + "is assigned to" + " " + j[0])
                print("Task Description: " + j[2])
                print("This task was assigned to you on: " + j[3])
                print("This task is due on: " + j[4])
                print("Is the task complete: " + j[5])
                print("=====================================================================================================================================================================================")
        break
        
# Modify program so that only username admin is allowed to register new users

# User input required to verify if user has rights to add new user/s
master_user = input("Please enter username to register new users: ")
master_password = input("Please enter password: ")
password_match = input("Please confirm password: ")

# Creating a loop with  conditions to check validity of input 
while True:

    if master_user == "admin" and master_password != password_match:
        print("Password mismatch, please start again!")
        break
        

    elif master_user != "admin":
            print("Username" + " " + master_user + " " + "does not have the rights to use this function!")
            print("=====================================================================================================================================================================================")
            break

    elif master_user == "admin" and master_password == password_match:
        newUserName = input("Please enter username to for new user: ")
        newPassWord = input("Please enter password for new user: ")
        password_match = input("Please confirm password: ")
        

        if newPassWord == password_match:
            f = open("user.txt", "a")
            f.write("\n"+ newUserName + ", " + password_match)
            f.close()
            print("User added successfully!")
            print("=====================================================================================================================================================================================")
            break

# Displaying statistics to admin user only        

# Input required from user to verify
user_name = input("Enter username to check statistics: ")
user_stats = input("Enter 'u' to view user statistics: ")
task_stats = input("Enter 't' to view task statistics: ")

while user_name != 'admin':
    print("U don't have permission to access this information!")
    break

fname = "user.txt"
count = 0

# if statement to loop over file and verify by opening text file in read mode
if user_name == 'admin' and user_stats == 'u':
    with open('user.txt', 'r') as f:
        for line in f:
            count += 1
print("Total number of users currently:", count)

fname = "tasks.txt"
count = 0   

# if statement to loop over file and verify by opening text file in read mode     
if user_name == 'admin' and task_stats == 't':
    with open('tasks.txt', 'r') as p:
        for line in p:
                count +=1
print("Total number of tasks currently:", count)
    


# This is the end of this code. 
    
    



    


    





                       
 
        

    
         
    

    
              
        
            

        
    

    

  
