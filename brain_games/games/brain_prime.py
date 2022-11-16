from random import randint


def is_prime_number(num):

    divider = 2
    while divider < num:
        if num % divider == 0:
            answer = 'no'
            return answer
        divider += 1
        answer = 'yes'

    return answer


def build_task():

    task = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    current_number = randint(3, 100)
    right_answer = is_prime_number(current_number)

    return right_answer, current_number, task
