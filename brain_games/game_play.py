import prompt
from brain_games import is_even
from brain_games import calc_it
from brain_games import find_gcd
from brain_games import find_number
from brain_games import is_prime


def greeting():

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def choose_game():

    while True:
        game_task = prompt.string('choose game (type number of game):\n\
    define if number is even     (1): \n\
    find result of expression    (2): \n\
    find greatest common divisor (3): \n\
    find missing number          (4): \n\
    define if number is prime    (5): \n\
    : ')

        if game_task in ('1', '2', '3', '4', '5'):
            break
        else:
            print("Your answer isn't valid, type 1, 2, 3, 4 or 5")

    return game_task


def game_run(game_number):

    user_name = greeting()
    if game_number == 0:
        game_number = choose_game()

    answers_count = 0
    while answers_count < 3:
        if game_number == '1':
            right_answer, user_answer = is_even.build_task()
        elif game_number == '2':
            right_answer, user_answer = calc_it.build_task()
        elif game_number == '3':
            right_answer, user_answer = find_gcd.build_task()
        elif game_number == '4':
            right_answer, user_answer = find_number.build_task()
        elif game_number == '5':
            right_answer, user_answer = is_prime.build_task()

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
