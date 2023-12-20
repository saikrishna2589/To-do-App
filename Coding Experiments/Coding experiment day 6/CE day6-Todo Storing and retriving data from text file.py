# Task 1- What if user does not enter 'add' , 'show' or 'exit' and enters something different. how to show
# message back to user perhaps saying 'input not valid.Please re-enter'


# we want to add a new feature for editing the to-do list. how do we go about adding the feature ?


# Day5- When user wants to modify a task in the list, he/she currently has to count the number in the list that they
# want to modify manually. we want to make user experience better by adding number in front of the printed modify
# output. how to achieve this? Answer-Enumerate() function

user_prompt = " Type add (or) show (or) exit (or) modify (or) complete : "

while True:
    user_display = input(user_prompt)
    user_display = user_display.strip()
    user_display = user_display.lower()

    match user_display:
        case "add":
            user_input_to_do_list = input("what item do you want to add to the to-do list? ") + "\n"
            file = open('C:/Users/saikr/Documents/pycharm projects/Day Classes/To-Do App/To_do_list.txt', 'r')  # read the existing To_do_list items
            To_do_list = file.readlines()  # read the existing To_do_list items
            file.close()

            To_do_list.append(user_input_to_do_list)
            print(To_do_list)

            # how to store the to-do list in a file. In below, we use open() ,which is a file object and write
            # into the To_do_list.txt text file created in the same directory('w--> write.'r'-->read)
            with open('C:/Users/saikr/Documents/pycharm projects/Day Classes/To-Do App/To_do_list.txt', 'w') as file2:
                file2.writelines(To_do_list)
                file2.close()
            # writelines is a method available for file objects.this writelines method
            # gets 'list' as an argument.Here we are giving our To_Do_List as an argument to the writelines method
            # file2.write() is used for text and same for file2.read()

        # we use enumerate function so we can index number along with the to-do list.
        # there is a space between the index number and the to-do list obejcts in the o/p. To reduce that, we
        # will need to use f-strings

        case "show" | "display":  # using Bitwise 'OR' operator
            read_todo_list = open('C:/Users/saikr/Documents/pycharm projects/Day Classes/To-Do App/To_do_list.txt', 'r')
            To_do_list = read_todo_list.readlines()
            read_todo_list.close()

            for index, i in enumerate(To_do_list):
                i = i.title()  # adding title case for each of the To-do items using the for loop before printing the
                # output.
                output1 = f"{index + 1}.{i}"
                print(output1)
            print(f"Length of the list is: {index + 1}")  # last value of the index is stored in the index value
            # outside the for loop
            # but actual proper way to get length of a list is to use length function
            print(f"Length of the list is :{len(To_do_list)}")

        case "modify":
            for index, i in enumerate(To_do_list):
                i = i.title()
                output = f"{index + 1}.{i}"
                print(output)
                # the print function prints the o/p but there are spaces between index and item object in the print.
                # what if you dont want spaces in the o/p between index and item object. Enter 'Fstring'
            user_modify = int(input("what numbered task do you want to modify from the above?"))
            user_modify = user_modify - 1
            # above code, we are converting user input to int format as list index below accepts only numbers as input
            # to retrieve list indices
            to_do_list_task_to_amend = To_do_list[user_modify]
            print("the task you want to amend is :" + str(to_do_list_task_to_amend).title())
            new_user_to_do_entry = input("Enter the replacement for " + str(to_do_list_task_to_amend).title() + " :")
            To_do_list[user_modify] = new_user_to_do_entry
            print(To_do_list)

        # we will use 'list indexing' method to extract that numbered task from the array to-do list

        # Adding another case statement to help user mark the to-do as complete. adn if complete, item will be
        # removed from to-do list This will be manipulation as in we are manipulating the list. If complete,
        # we want it removed from the list. so in such cases for manipulation of the list or any of the objects,
        # we need to think about 'METHODS'

        case "complete":
            for index, i in enumerate(To_do_list):
                todo_tasks = f"{index + 1}.{i}"
                print(todo_tasks)
            task_completed = int(input("what numbered task is complete: "))
            task_completed = task_completed - 1
            To_do_list.pop(task_completed)
            print("remaining items on to do list: ")
            for index, i in enumerate(To_do_list):
                remaining_todo_tasks = f"{index + 1}.{i}"
                print(remaining_todo_tasks)

        case "exit":

            break

        case random_entry:
            print("input not valid.Please re-enter from options provided")

# the variable random_entry in this case does not need to be defined in the code.
# it is defined on the fly with the entry of the user if it doesn't belong to 'add','show' or 'exit'

print("Goodbye for now!See you soon. Remember to SMILE AND Be Happy keep Happy")
