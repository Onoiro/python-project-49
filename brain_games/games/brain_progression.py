from random import randint

TASK = "What number is missing in the progression?"


def get_progression(first_number, prog_step):
    progression = []
    for i in range(1, 10):
        prog_number = first_number + prog_step
        first_number = first_number + prog_step
        progression.append(str(prog_number))
    return progression


def build_task():
    number1 = randint(1, 10)
    number3 = randint(2, 10)
    missing_number_index = randint(1, 8)
    current_progression = get_progression(number1, number3)
    right_answer = current_progression[missing_number_index]
    current_progression[missing_number_index] = '..'
    task_string = " ".join(current_progression)
    return right_answer, task_string
