from random import randint


def is_prime_number(num):

    divider = 2
    while divider < num:
        if num % divider == 0:
            return False
        divider += 1

    return True


def build_task():

    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    current_number = randint(3, 100)
    if is_prime_number(current_number) is True:
        right_answer = 'yes'
    else:
        right_answer = 'no'

    return right_answer, current_number, task
