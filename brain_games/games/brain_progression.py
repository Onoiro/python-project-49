from random import randint

TASK = "What number is missing in the progression?"


def get_progression(first_number, prog_step):
    progression = []
    for i in range(10):
        prog_number = first_number + prog_step
        first_number = first_number + prog_step
        progression.append(str(prog_number))
    return progression


def build_task():
    start_prog_number = randint(1, 10)
    step_prog_number = randint(1, 10)
    progression = get_progression(start_prog_number, step_prog_number)
    missing_number_index = randint(1, len(progression))
    right_answer = progression[missing_number_index]
    progression[missing_number_index] = '..'
    task_string = " ".join(progression)
    return right_answer, task_string
