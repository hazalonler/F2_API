from datetime import datetime
from flask import abort, make_response
from dataclasses import dataclass


@dataclass
class Task:
    id: str
    name: str
    date: str
    list_id: str
    board_id: str
    priority: int = 1000
    description: str = ""



TASKS = list()
TASKS.append(Task("1", "Prepare a new board", datetime(2023, 4, 3).strftime("%Y-%m-%d"), "e1", "a1"))
TASKS.append(Task("2", "Prepare a task list", datetime(2023, 5, 6).strftime("%Y-%m-%d"), "e2", "a1"))
TASKS.append(Task("3", "naming", datetime(2022, 5, 6).strftime("%Y-%m-%d"), "e3", "a1"))
TASKS.append(Task("4", "Make a to-do list for shopping", datetime(2021, 4, 3).strftime("%Y-%m-%d"), "e3", "a1", 2000))
TASKS.append(Task("5", "edit", datetime(2023, 5, 8).strftime("%Y-%m-%d"), "e2", "a1", 2000))
TASKS.append(Task("6", "Going to lake side", datetime(2023, 7, 6).strftime("%Y-%m-%d"), "e3", "a1", 3000))
TASKS.append(Task("7", "New board task created", datetime(2019, 4, 3).strftime("%Y-%m-%d"), "e3", "a1", 4000))


def read_tasks(board_id, list_id):
    task_list = []
    for task in TASKS:
        if task.board_id == board_id and task.list_id == list_id:
            task_list.append(task)

    idx = 0
    while idx < (len(task_list)-1):
        if task_list[idx].priority > task_list[idx+1].priority:
            task_list[idx], task_list[idx+1] = task_list[idx+1], task_list[idx]
        idx += 1

    print(task_list)
    return task_list


def create(board_id, list_id, task):
    date = task.get("date", "")
    description = task.get("description", "")
    task_id = task.get("id")
    name = task.get("name")
    priority = task.get("priority", int())

    if date == "":
        date = datetime.now()

    for task_in_list in TASKS:
        if task_in_list.board_id == board_id:
            if task_id and task_in_list.id != task_id:
                continue
            else:
                abort(
                    406,
                    f"Task with the name of {name} already exists",
                )

    task_instance = Task(task_id, name, date, list_id, board_id, priority, description)
    TASKS.append(task_instance)
    return 201


def delete(id):
    for idx in range(0, len(TASKS)):
        if TASKS[idx].id == id:
            del TASKS[idx]
            return make_response(
                f"The task with the ID ({id}) successfully deleted", 200
            )

    abort(
        404,
        f"Task with the ID({id}) not found"
    )


def update(id, task):

    for idx in range(0, len(TASKS)):
        if TASKS[idx].id == task.get("id"):
            TASKS[idx].list_id = task.get("list_id", TASKS[idx].list_id)
            TASKS[idx].priority = task.get("priority", TASKS[idx].priority)
            TASKS[idx].description = task.get("description", TASKS[idx].description)
            print(TASKS[idx])
            return 200

    abort(
        404,
        f"Task with the ID ({id}) not found"
    )
