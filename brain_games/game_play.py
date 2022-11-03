
def print_messages(result, answer, name, answer_status):
        
    if answer == result:
        message = 'Correct!'
        answer_status += 1
        if answer_status == 3:
            message = f'Correct!\nCongratulations, {name}!'

    else:
        message = f"'{answer}' is wrong answer ;(. Correct answer was '{result}'.\nLet's try again, {name}!"
        answer_status = 0

    print(message)

    return answer_status

