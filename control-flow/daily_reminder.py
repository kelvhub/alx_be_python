
task = input("Enter your task: ")
time_bound = input("is it time-bound? (yes or no): ").lower()
priority = input("priority (high, medium, low): ").lower()


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


print("\nReminder:",message)
    