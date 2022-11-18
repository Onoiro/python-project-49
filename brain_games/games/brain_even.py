from random import randint

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def build_task():
    number = randint(-100, 100)
    if number % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, str(number)
