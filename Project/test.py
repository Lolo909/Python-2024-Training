from datetime import datetime

date_format = '%d-%m-%Y %H:%M'

task_date_to_be_completed = input("What date should the task be completed? (date must be in the future) - format:(day month year hour minute):")                           

task_date_to_be_completed_into_list = task_date_to_be_completed.split()
# task_date_to_be_completed_into_list=["11", "7", "2024", "17", "30"]
date_string = f"{task_date_to_be_completed_into_list[0]}-{task_date_to_be_completed_into_list[1]}-{task_date_to_be_completed_into_list[2]} {task_date_to_be_completed_into_list[3]}:{task_date_to_be_completed_into_list[4]}"
print(date_string)
parsed_datetime = datetime.strptime(date_string, date_format)
print(parsed_datetime)
temp = parsed_datetime.strftime(date_format)
print(temp)


current_datetime = datetime.now()
print(current_datetime.strftime(date_format))