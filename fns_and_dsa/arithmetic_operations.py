def perform_operation(num1, num2, operation):
    """
    Perform a basic arithmetic operation on two numbers.

    Parameters:
        num1 (float): First number.
        num2 (float): Second number.
        operation (str): One of 'add', 'subtract', 'multiply', 'divide'.

    Returns:
        float or str: Result of the operation, or error message for invalid input or divide by zero.
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Invalid operation."
# This function performs basic arithmetic operations based on user input.
# It takes two numbers and an operation, then returns the result.