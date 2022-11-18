import prompt


def run_game(game):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(game.TASK)
    answers_count = 0
    while answers_count < 3:
        right_answer, task_value = game.build_task()
        user_answer = prompt.string(f'Question: {task_value}\nYour answer: ')
        if user_answer == right_answer:
            message = 'Correct!'
            answers_count += 1
            if answers_count == 3:
                message = f'Correct!\nCongratulations, {user_name}!'
        else:
            message = f"'{user_answer}' is wrong answer ;(. \
    Correct answer was '{right_answer}'.\nLet's try again, {user_name}!"
            answers_count = 0
        print(message)
        if answers_count == 0:
            break
