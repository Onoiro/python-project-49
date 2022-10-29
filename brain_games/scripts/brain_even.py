from random import randint

print("Welcome to the Brain Games!")
name = input('May I have your name? ')
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
            print('Correct!')
            break
        else:
            print("Your answer isn't valid, type 'yes' or 'no'")
    
    if user_answer == right_answer:
        count += 1
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'.\nLet's try again, {name}!")
        break
    
if count == 3:
    print(f'Congratulations, {name}!')
