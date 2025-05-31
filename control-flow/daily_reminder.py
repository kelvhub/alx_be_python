Task = input("input a task description")
Priority = input("high, medium, low")
Time_bound = input("yes or no")

match Priority:
    case "high":
        message = f"Reminder: '{Task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{Task}' is a medium priority task"
    case "low":
        message = f"Reminder: '{Task}' is a low priority task"
    case "_":
        message = f"Reminder: '{Task}' is an unknown priority task"

if Time_bound == 'yes':
    message += "This task requires an immediate attention today!"


print(message)
    