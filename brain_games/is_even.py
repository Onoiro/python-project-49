from random import randint


def get_number():

    number = randint(-1000000, 1000000)
    return number


def is_even_number(num):

    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return answer


def run_game():

    name = input('May I have your name? ')
    print(f'Hello, {name}!')

    valid_answers = ('yes', 'no')
    task = "Answer 'yes' if the number is even, otherwise answer 'no'."
    count = 0

    print(task)

    while count < 3:

        current_number = get_number()
        right_answer = is_even_number(current_number)

        while True:
            user_answer = input(f'Question: {current_number}: ')

            if user_answer in valid_answers:
                break
            else:
                print("Your answer isn't valid, type 'yes' or 'no'")

        if user_answer == right_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.")
            print(f"Let's try again, {name}!")
            break

    if count == 3:
        print(f'Congratulations, {name}!')


run_game()
