from random import randint


def is_even_number(num):

    if num % 2 == 0:

        return True


def build_task():

    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    current_number = randint(-100, 100)
    if is_even_number(current_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, current_number, task
