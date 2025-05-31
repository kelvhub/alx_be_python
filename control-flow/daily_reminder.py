task = input("Enter your task description:")
time_bound = input("is the task time-bound (yes or no):")
priority = input("Enter the task priority (high, medium, low):")


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


print(message)
    