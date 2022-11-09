from random import randint


def get_progression(first_number, operator, prog_step):

    progression = []
    for i in range(1, 8):
        if operator == 1:
            prog_number = first_number + prog_step
            first_number = first_number + prog_step
            progression.append(prog_number)
        elif operator == 2:
            prog_number = first_number * prog_step
            first_number = first_number * prog_step
            progression.append(prog_number)
            
    return progression


def get_missing_number(numbers, index):

    missing_number = numbers[index]

    return missing_number


def get_task_string(numbers_list, index):

    new_string = ''
    for i in range(len(numbers_list)):
        if i == index:
            new_string += '.. '
        else:
            new_string += str(f'{numbers_list[i]} ')
        
    
    return new_string


def build_task():
    
    task = "What number is missing in the progression?"
    print(task)
    number1 = randint(1, 10)
    number2 = randint(1, 2)
    number3 = randint(2, 10)
    missing_number_index = randint(1, 7)
    current_progression = get_progression(number1, number2, number3)
    right_answer = get_missing_number(current_progression, missing_number_index)
    task_string = get_task_string(current_progression, missing_number_index)
    user_answer = get_valid_answer(task_string)
    
    return right_answer, user_answer


def get_valid_answer(exp):

    while True:
        answer = input(f'Question: {exp}: ')

        try:
            answer = int(answer)
        except:
            print("Your answer isn't valid, enter integer")
        else:
            break
    
    return answer