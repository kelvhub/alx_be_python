def perform_operation(num1: float, num2: float, operation: str):
    """
    Performs basic arithmetic operations: add, subtract, multiply, divide.
    Returns result or an error message for invalid operations or division by zero.
    """
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else:
        return "Error: Invalid operation"
