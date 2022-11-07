
from brain_games import is_even
from brain_games import calc_it


def greeting():

    print("Welcome to the Brain Games!")
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def choose_game():
    game_task = input('choose game:\n\
is even number (1): \n\
calculate this (2): \n: ')
    return game_task

def game_run():

    user_name = greeting()
    game_number = choose_game()
    
    answers_count = 0
    while answers_count < 3:
        if game_number == '1':
            right_answer, user_answer = is_even.build_task()
        elif game_number == '2':
            right_answer, user_answer = calc_it.build_task()
        answers_count = print_messages\
(right_answer, user_answer, user_name, answers_count)
        if answers_count == 0:
            break

    return right_answer, user_answer, user_name, answers_count


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

#game_run()
