from random import randint


def get_gcd(num1, num2):

    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1

    return num1


def build_task():

    task = "Find the greatest common divisor of given numbers."
    current_number_1 = randint(1, 100)
    current_number_2 = randint(1, 100)
    right_answer = str(get_gcd(current_number_1, current_number_2))
    current_numbers = f'{current_number_1} {current_number_2}'

    return right_answer, current_numbers, task
