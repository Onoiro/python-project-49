from random import randint


def get_number():

    number = randint(-100, 100)
    return number


def is_even_number(num):

    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def build_task():

    task = 'Answer "yes" if the number is even, otherwise answer "no".'
    current_number = get_number()
    right_answer = is_even_number(current_number)

    return right_answer, current_number, task
