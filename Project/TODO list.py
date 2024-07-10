# Task: To make todo list. Information will be saved and read by JSON file.
# The function wich the program will provide are:create, read, update, delete

import json
import urllib.parse
from datetime import datetime



isProgramStillRunning = True

last_id = 1

while isProgramStillRunning:
    
    print("TODO LIST:")
    print("----------")
    #print all tasks here:

    try:
        with open("Project\\data.json", "r") as file:
            
            tasks_details = json.load(file)
            
            if len(tasks_details) == 0:
                print("There is not any tasks today! :)")
            else:           
                for task in tasks_details:
                    date_to_be_compleated = task["date_to_be_completed"].split()
                    print("№",task["id"],"| Task:",task["task"], "| Priority:",task["priority"],"| Date to be completed:",date_to_be_compleated[0]+"."+date_to_be_compleated[1]+"."+date_to_be_compleated[2]+" "+date_to_be_compleated[3]+":"+date_to_be_compleated[4])
                    last_id = task["id"]

            print("-------------------------------")
            print("What are you going to do today?:")
            print("1. Add new task")
            print("2. Read task")
            print("3. Update task")
            print("4. Delete task")
            print("5. EXIT")
            print("-------------------------------")
            isInputCorect = False

            while not isInputCorect:
                choice_user = input("Insert number of your choice:")

                match choice_user:
                    case "1":
                        isInputCorect = True

                        #Add new task
                        task_name = input("What is the task?:")
                        # task_priority
                        task_description = input("Describe the task more in more details:")

                        while True:
                            task_date_to_be_completed = input("What date should the task be completed? (date must be in the future) - format:(day month year hour minute):")                           
                            try:
                                task_date_to_be_completed_into_list = task_date_to_be_completed.split()
                                date_string = f"{task_date_to_be_completed_into_list[0]}-{task_date_to_be_completed_into_list[1]}-{task_date_to_be_completed_into_list[2]} {task_date_to_be_completed_into_list[3]}:{task_date_to_be_completed_into_list[4]}"
                                parsed_datetime = datetime.strptime(date_string, "%d-%m-%Y %H:%M")

                                current_datetime = datetime.now()
                                formatted_current_datetime = current_datetime.strftime("%d-%m-%Y %H:%M")

                                if current_datetime > parsed_datetime:
                                    print("Date must be in the future!")
                                    continue
                                
                                data = {
	                                "id": last_id+1,
	                                "task": task_name,
	                                "date_created": formatted_current_datetime,
	                                "date_to_be_completed": str(parsed_datetime),
                                    "description": task_description,
                                    "priority": "low"
                                }

                                tasks_details.append(data)

                                with open('Project\\data.json', 'w') as file:
                                    json.dump(tasks_details, file, indent=2, separators=(',',': '))


                            except BaseException as e:
                                print("Wrong input!", e )
                                continue
                            else:
                                break


                        print("Added new task succesfully!")
                    case "2":

                        print("-------------------------------")           
                        isInputCorectForTask = False

                        chosen_task = dict()

                        while not isInputCorectForTask:
                            choice_user = input("Insert number of your chosen task:")

                            if not choice_user.isnumeric():
                                print("Wrong input! Insert number!")
                                continue
                
                            for task in tasks_details:
                                if task["id"] == int(choice_user):
                                    chosen_task = task
                                    isInputCorectForTask = True
                                    break
                                else:
                                    print("Wrong input! There is not task with such a number!")

                        print("-------------------------------")



                        isInputCorect = True
                        print()                    
                    case "3":
                        isInputCorect = True
                        print()
                    case "4":
                        isInputCorect = True
                        print()
                    case "5":
                         print("Have a nice day! :)")
                         isInputCorect = True
                         isProgramStillRunning = False
                         break

                    
                print("Wrong input! Insert correct number!")
                    


    except FileNotFoundError:
        print("File not found.")
        isProgramStillRunning = False
        break
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     isProgramStillRunning=False
    #     break
