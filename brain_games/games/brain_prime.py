from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divider = 2
    while divider < num:
        if num % divider == 0:
            return False
        divider += 1
    return True


def build_task():
    number = randint(3, 100)
    if is_prime(number):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return right_answer, str(number)
