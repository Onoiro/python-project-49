from is_even import build_task
from calc_it import build_task

def game_run():

    user_name = greeting()
    count = 0
    while count < 3:

        right_answer, user_answer = build_task()
        count = print_messages\
(right_answer, user_answer, user_name, count)
        if count == 0:
            break

    return right_answer, user_answer, user_name, count


def greeting():

    print("Welcome to the Brain Games!")
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def print_messages(result, answer, name, count):
        
    if answer == result:
        message = 'Correct!'
        count += 1
        if count == 3:
            message = f'Correct!\nCongratulations, {name}!'

    else:
        message = f"'{answer}' is wrong answer ;(. \
Correct answer was '{result}'.\nLet's try again, {name}!"
        count = 0

    print(message)

    return count

game_run()
