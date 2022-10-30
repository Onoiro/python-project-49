#!/usr/bin/env python3

from random import randint

def main():

    print("Welcome to the Brain Games!")
    name = input('May I have your name? ')
    print(f'Hello, {name}!')
    user_answer = ''
    right_answer = ''
    valid_answers = ('yes', 'no')
    task = "Answer 'yes' if the number is even, otherwise answer 'no'."
    count = 0

    print(task)

    while count < 3:

        number = randint(-1000000, 1000000)

        if number%2 == 0:
            right_answer = 'yes'
        else:
            right_answer = 'no'

        while True:
            user_answer = input(f'Question: {number}: ')

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


if __name__ == '__main__':
    main()
