from random import randint


def is_even_number(num):

    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def build_task():

    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    current_number = randint(-100, 100)
    right_answer = is_even_number(current_number)

    return right_answer, current_number, task
