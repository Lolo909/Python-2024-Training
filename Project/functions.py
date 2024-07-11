def Insert_number_of_your_chosen_task(tasks_details):
    print("-------------------------------")         
    isInputCorectForTask = False

    chosen_task = dict()

    while not isInputCorectForTask:
        choice_user = input("Insert number of your chosen task:")

        if not choice_user.isnumeric():
            print("Wrong input! Insert number!")
            continue
        else:
            for task in tasks_details:
                if task["id"] == int(choice_user):
                    chosen_task = task
                    isInputCorectForTask = True
                    break
                                    
            if isInputCorectForTask == False:
                print("Wrong input! There is not task with such a number!")
    
    print("-------------------------------")
    return chosen_task

def Are_you_ready():
    isInputCorectForTask = False

    print("-------------------------------")
    while not isInputCorectForTask:
        choice_user = input("Are you ready with reading? (yes/no):").lower()
        print("-------------------------------")
        match choice_user:
            case "yes":
                isInputCorectForTask = True
                return True
            case "no":
                isInputCorectForTask = True
                return False
            case _:
                print("Wrong input! You can only answer with \"yes\" or \"no.\"")

def Print_all_tasks(tasks_details):
    last_id = 1
    for task in tasks_details:
                    date_to_be_compleated = task["date_to_be_completed"].split()
                    print("№",task["id"],"| Task:",task["task"], "| Priority:",task["priority"],"| Date to be completed:",date_to_be_compleated[0]+" "+date_to_be_compleated[1])
                    last_id = task["id"]
    return last_id

    