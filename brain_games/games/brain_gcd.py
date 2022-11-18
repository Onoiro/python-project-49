from random import randint

TASK = "Find the greatest common divisor of given numbers."


def get_gcd(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    return num1


def build_task():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    right_answer = str(get_gcd(number_1, number_2))
    numbers = f'{number_1} {number_2}'
    return right_answer, numbers
