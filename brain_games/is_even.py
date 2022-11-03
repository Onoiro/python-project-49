from random import randint
from greeting import greeting
from game_play import print_messages


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
    
    task = "Answer 'yes' if the number is even, otherwise answer 'no'."
    print(task)
    current_number = get_number()
    right_answer = is_even_number(current_number)
    user_answer = get_valid_answer(current_number)
    return right_answer, user_answer


def get_valid_answer(num):

    valid_answers = ('yes', 'no')

    while True:
        answer = input(f'Question: {num}: ')

        if answer in valid_answers:
            break
        else:
            print("Your answer isn't valid, type 'yes' or 'no'")
    return answer


def game_run():

    user_name = greeting()
    status_answers = 0
    while status_answers < 3:

        right_answer, user_answer = build_task()
        status_answers = print_messages(right_answer, user_answer, user_name, status_answers)
        if status_answers == 0:
            break


game_run()
