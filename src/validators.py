from datetime import datetime


def validate_priority(priority):
    valid_priorities = ["high", "medium", "low"]

    if priority.lower() in valid_priorities:
        return True
    else:
        return False


def validate_deadline(deadline):
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validate_not_empty(value):
    if value.strip() == "":
        return False
    else:
        return True

def validate_task_id(task_id, tasks):
    if task_id < 1:
        return False

    for task in tasks:
        if task.task_id == task_id:
            return True

    return False

def validate_integer(value):
    try:
        int(value)
        return True
    except ValueError:
        return False