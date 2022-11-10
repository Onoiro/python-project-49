from random import randint


def get_number():

    number = randint(1, 100)
    return number


def get_gcd(num1, num2):

    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1

    return num1


def build_task():

    task = "Find the greatest common divisor of given numbers."
    print(task)
    current_number_1 = get_number()
    current_number_2 = get_number()
    right_answer = get_gcd(current_number_1, current_number_2)
    current_numbers = f'{current_number_1} {current_number_2}'
    user_answer = get_valid_answer(current_numbers)

    return right_answer, user_answer


def get_valid_answer(exp):

    while True:
        answer = input(f'Question: {exp}: ')

        try:
            answer = int(answer)
        except ValueError:
            print("Your answer isn't valid, enter integer")
        else:
            break

    return answer
