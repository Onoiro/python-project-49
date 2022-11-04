from random import randint
from greeting import greeting
from game_play import print_messages

def get_number():

    number = randint(-100, 100)
    return number


def get_valid_answer(exp):

    while True:
        answer = input(f'Question: {exp}: ')

        try:
            answer = int(answer)
        except:
            print("Your answer isn't valid, enter integer")
        else:
            break
    
    return answer


def build_task():

    task = "What is the result of the expression?"
    print(task)
    first_number = get_number()
    second_number = get_number()
    operator = randint(1, 2)
    
    if operator == 1:
        expression = f"{first_number} + {second_number}"
        right_answer = first_number + second_number
    elif operator == 2:
        expression = f"{first_number} - {second_number}"
        right_answer = first_number - second_number
    
    user_answer = get_valid_answer(expression)

    return right_answer, user_answer


def game_run():

    user_name = greeting()
    status_answers = 0
    while status_answers < 3:

        right_answer, user_answer = build_task()
        status_answers = print_messages(right_answer, user_answer, user_name, status_answers)
        if status_answers == 0:
            break


game_run()
