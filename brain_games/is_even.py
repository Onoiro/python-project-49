from random import randint


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
