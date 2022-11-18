from random import randint

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    divider = 2
    while divider < num:
        if num % divider == 0:
            answer = 'no'
            return answer
        divider += 1
        answer = 'yes'
    return answer


def build_task():
    number = randint(3, 100)
    right_answer = is_prime(number)
    return right_answer, number
