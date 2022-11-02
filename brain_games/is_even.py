from random import randint
from greeting import greeting


def get_number():

    number = randint(-100, 100)
    return number


def is_even_number(num):

    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def get_valid_answer(num):

    valid_answers = ('yes', 'no')

    while True:
        answer = input(f'Question: {num}: ')

        if answer in valid_answers:
            break
        else:
            print("Your answer isn't valid, type 'yes' or 'no'")
    return answer


def is_even_run():

    task = "Answer 'yes' if the number is even, otherwise answer 'no'."
    count = 0
    user_name = greeting()
    print(task)

    while count < 3:

        current_number = get_number()
        right_answer = is_even_number(current_number)
        user_answer = get_valid_answer(current_number)

        if user_answer == right_answer:
            print('Correct!')
            count += 1
            if count == 3:
                print(f'Congratulations, {user_name}!')
                break
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{right_answer}'.")
            print(f"Let's try again, {user_name}!")
            break


is_even_run()
