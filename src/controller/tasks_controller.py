from datetime import datetime
from flask import abort, make_response
from dataclasses import dataclass


@dataclass
class Tasks:
    id: str
    name: str
    date: str
    list_id: str
    priority: int = 1000
    board_id: str = "a1"
    description: str = ""


TASKS = list()
example_1 = Tasks("1", "Prepare a new board", datetime(2023, 4, 3).strftime("%Y-%m-%d"), "e1")
example_2 = Tasks("2", "Prepare a task list", datetime(2023, 5, 6).strftime("%Y-%m-%d"), "e2")
example_3 = Tasks("3", "naming", datetime(2022, 5, 6).strftime("%Y-%m-%d"), "e3")
example_4 = Tasks("4", "Make a to-do list for shopping", datetime(2021, 4, 3).strftime("%Y-%m-%d"), "e3", 2000)
example_5 = Tasks("5", "edit", datetime(2023, 5, 8).strftime("%Y-%m-%d"), "e2", 2000)
example_6 = Tasks("6", "Going to lake side", datetime(2023, 7, 6).strftime("%Y-%m-%d"), "e3", 3000)
example_7 = Tasks("7", "New board task created", datetime(2019, 4, 3).strftime("%Y-%m-%d"), "e3", 4000)

TASKS.append(example_1)
TASKS.append(example_2)
TASKS.append(example_3)
TASKS.append(example_4)
TASKS.append(example_5)
TASKS.append(example_6)
TASKS.append(example_7)


def read_tasks(boardId):
    task_list = []
    for task in TASKS:
        if task.board_id == boardId:
            task_list.append(task)

    return task_list


def create(boardId, task):
    task_id = task.get("id")
    name = task.get("name")
    description = task.get("description", "")
    priority = task.get("priority", int())
    listId = task.get("listId", "")
    date = task.get("date", "")

    if date == "":
        date = datetime.now()

    for task in TASKS:
        if task_id and task.id != task_id:
            continue
        else:
            if task.board_id == boardId:
                abort(
                    406,
                    f"Task with the name of {name} already exists",
                )

    task_instance = Tasks(task_id, name, description, priority, listId, date)
    TASKS.append(task_instance)
    return 201


def read_one(id):
    for task in TASKS:
        if task.id == id:
            return task

    abort(
        404, f"Task with the id({id}) not found"
    )


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
        if TASKS[idx].id == id:
            my_task = TASKS[idx].description
            my_task = task.get("description", my_task)
            return my_task

    abort(
        404,
        f"Task with the ID ({id}) not found"
    )






