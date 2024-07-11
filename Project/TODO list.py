# Task: To make todo list. Information will be saved and read by JSON file.
# The function wich the program will provide are:create, read, update, delete

import json
import urllib.parse
from datetime import datetime
from functions import *
import time

date_format = '%d-%m-%Y %H:%M'

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
                last_id = Print_all_tasks(tasks_details)
                # for task in tasks_details:
                #     date_to_be_compleated = task["date_to_be_completed"].split()
                #     print("№",task["id"],"| Task:",task["task"], "| Priority:",task["priority"],"| Date to be completed:",date_to_be_compleated[0]+" "+date_to_be_compleated[1])
                #     last_id = task["id"]

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
                                parsed_datetime = datetime.strptime(date_string, date_format)
                                                               
                                current_datetime = datetime.now()
                                formatted_current_datetime = current_datetime.strftime(date_format)


                                if current_datetime > parsed_datetime:
                                    print("Date must be in the future!")
                                    continue


                                parsed_datetime = parsed_datetime.strftime(date_format)
                                data = {
	                                "id": last_id+1,
	                                "task": task_name,
	                                "date_created": formatted_current_datetime,
	                                "date_to_be_completed": str(parsed_datetime),
                                    "description": task_description,
                                    "priority": "NONE"
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
                        # Read task

                        print("-------------------------------")
                        last_id = Print_all_tasks(tasks_details)
                        

                        chosen_task = Insert_number_of_your_chosen_task(tasks_details)
                        print("Task:", chosen_task["task"])
                        print("Priority:",chosen_task["priority"])
                        print("Date created:", chosen_task["date_created"])
                        print("Date to be completed:",chosen_task["date_to_be_completed"])
                        print("Description:", chosen_task["description"])
                                               
                        is_user_ready_with_reading = False
                        while not is_user_ready_with_reading:
                            time.sleep(5)
                            is_user_ready_with_reading = Are_you_ready()


                        isInputCorect = True
                        # print("Reading done")                    
                    case "3":
                        # Update task
                        print("-------------------------------")
                        last_id = Print_all_tasks(tasks_details)

                        chosen_task = Insert_number_of_your_chosen_task(tasks_details)

                        print("What would you like to change? (If you don't want to change something just press ENTER):")
                        print("-------------------------------")
                        __date_to_be_compleated = chosen_task["date_to_be_completed"].split()
                        print("Task:",chosen_task["task"], "| Priority:",chosen_task["priority"],"| Date to be completed:",__date_to_be_compleated[0]+" "+__date_to_be_compleated[1], chosen_task["description"])
                        print("-------------------------------")
                        data = dict()

                        for key, value in chosen_task.items():

                            if key == "id" or key == "date_created":
                                data[key] = value
                                continue

                            default_value = value
                            new_value = input(key + ":")

                            if not new_value:
                                new_value = default_value
                            
                            data[key] = new_value
                            
                        
                        for task in tasks_details:
                            if task == chosen_task:
                                tasks_details.remove(task)
                                break
                            
                        tasks_details.append(data)

                        with open('Project\\data.json', 'w') as file:
                            json.dump(tasks_details, file, indent=2, separators=(',',': '))

                        isInputCorect = True
                        print("Updated task succesfully!")
                    case "4":
                        # Delete task

                        print("-------------------------------")
                        last_id = Print_all_tasks(tasks_details)

                        chosen_task = Insert_number_of_your_chosen_task(tasks_details)

                        for task in tasks_details:
                            if task == chosen_task:
                                tasks_details.remove(task)
                                break
                        
                        with open('Project\\data.json', 'w') as file:
                                json.dump(tasks_details, file, indent=2, separators=(',',': '))


                        isInputCorect = True
                        print("Deleted task succesfully")
                    case "5":
                         print("Have a nice day! :)")
                         isInputCorect = True
                         isProgramStillRunning = False
                         break
                    case _:                    
                        print("Wrong input! Insert correct number!")
                    


    except FileNotFoundError:
        print("File not found.")
        isProgramStillRunning = False
        break
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #     isProgramStillRunning=False
    #     break
