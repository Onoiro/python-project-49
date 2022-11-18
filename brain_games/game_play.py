import prompt


def run_game(game):
    user_name = greet_user()
    print(game.TASK)
    answers_count = 0
    while answers_count < 3:
        right_answer, task_value = game.build_task()
        user_answer = prompt.string(f'Question: {task_value}\nYour answer: ')
        answers_count = print_messages(right_answer, user_answer,
                                       user_name, answers_count)
        if answers_count == 0:
            break


def greet_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
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
