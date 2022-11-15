import random


def build_task():

    task = "What is the result of the expression?"
    first_number = random.randint(-100, 100)
    second_number = random.randint(-100, 100)
    operator = random.choice(['+', '-', '*'])

    expression = f"{first_number} {operator} {second_number}"
    right_answer = str(get_result(first_number, second_number, operator))

    return right_answer, expression, task


def get_result(number1, number2, operation):
    if operation == '+':
        result = number1 + number2
    elif operation == '-':
        result = number1 - number2
    elif operation == '*':
        result = number1 * number2

    return result
