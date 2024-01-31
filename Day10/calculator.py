from art import logo

def get_result(number1:float, number2:float, operation:str) -> float:
    """
    Takes 2 numbers and performs the operation given to the function (+, -, *, /).
    """
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    elif operation == '*':
        return number1 * number2
    elif operation == '/':
        return number1 / number2
    else:
        return "Invalid operation. Please choose a valid operation."

print(logo)
resume = 'y'
first_number = float(input("What's the first number?: "))
print('+\n', '-\n', '*\n', '/\n')
while resume == 'y':
    operation = input("Pick an operation: ")
    second_number = float(input("What's the next number?: "))
    result = get_result(first_number, second_number, operation) 
    print(f"{str(first_number)} {operation} {str(second_number)} = {result}")
    resume = input(f"Type 'y' to continue with {result}, or type 'n' to start a new calculator: ").lower()
    if resume == 'y':
        first_number = result