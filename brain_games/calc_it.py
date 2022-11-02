from random import randint
from greeting import greeting


def get_number():

    number = randint(-100, 100)
    return number


def get_valid_answer(exp):

    while True:
        answer = input(f'Question: {exp}: ')
        #break

        try:
            answer = int(answer)
        except:
            print("Your answer isn't valid, enter integer")
        else:
            break
    
    return answer


def calc_it_run():

    task = "What is the result of the expression?"
    count = 0
    user_name = greeting()
    print(task)

    while count < 3:

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


calc_it_run()
