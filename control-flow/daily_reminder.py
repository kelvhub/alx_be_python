#Prompt for task details
task = input("Enter your task: ")
priority = input("priority (high, medium, low): ").lower()
time_bound = input("is it time-bound? (yes or no): ").lower()


#process the task
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case _:
        message = f"Reminder: '{task}' is an unknown priority task"

if time_bound == 'yes':
    message += "This task requires an immediate attention today!"
else:
    message += "Consider completing the code"


print(f"Reminder:{message}")
    