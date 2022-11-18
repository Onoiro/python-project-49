from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def build_task():
    number = randint(-100, 100)
    if is_even(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, number
