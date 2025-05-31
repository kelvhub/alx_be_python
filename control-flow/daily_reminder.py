task = input("input a task description")
priority = input("high, medium, low")
time_bound = input("yes or no")

match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{task}' is a low priority task"
    case "_":
        message = f"Reminder: '{task}' is an unknown priority task"

if time_bound == 'yes':
    message += "This task requires an immediate attention today!"


print(message)
    