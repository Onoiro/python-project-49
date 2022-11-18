from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even_number(num):
    return num % 2 == 0


def build_task():
    current_number = randint(-100, 100)
    if is_even_number(current_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, current_number
