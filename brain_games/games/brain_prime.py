from random import randint


def get_number():

    number = randint(1, 100)

    return number


def is_prime_number(num):

    divider = 2
    while divider < num:
        if num % divider == 0:
            answer = 'no'
            break
        divider += 1
        answer = 'yes'

    return answer


def build_task():

    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    current_number = get_number()
    right_answer = is_prime_number(current_number)

    return right_answer, current_number, task
