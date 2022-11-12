from random import randint


def get_progression(first_number, prog_step):

    progression = []
    for i in range(1, 10):
        prog_number = first_number + prog_step
        first_number = first_number + prog_step
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
    number1 = randint(1, 10)
    number3 = randint(2, 10)
    missing_number_index = randint(1, 8)
    current_progression = get_progression(number1, number3)
    right_answer = get_missing_number(current_progression, missing_number_index)
    task_string = get_task_string(current_progression, missing_number_index)

    return right_answer, task_string, task
