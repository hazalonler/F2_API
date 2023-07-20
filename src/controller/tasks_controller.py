from datetime import datetime
from flask import abort, make_response

TASKS = [
    {
        "id": "1",
        "name": "Prepare a new board",
        "date": datetime(2023, 4, 3),
        "listId": "e1",
        "priority": 1000,
        "description": "",
        "boardId": "a1"
    },
    {
        "id": "2",
        "name": "Prepare a task list",
        "date": datetime(2023, 5, 6),
        "listId": "e2",
        "priority": 1000,
        "description": "",
        "boardId": "a1"
    },
    {
        "id": "3",
        "name": "naming",
        "date": datetime(2022, 5, 6),
        "listId": "e3",
        "priority": 1000,
        "description": "",
        "boardId": "a1"
    },
    {
        "id": "4",
        "name": "Make a to-do list for shopping",
        "date": datetime(2021, 4, 3),
        "listId": "e3",
        "priority": 2000,
        "description": "",
        "boardId": "a1"
    },
    {
        "id": "5",
        "name": "edit",
        "date": datetime(2023, 5, 8),
        "listId": "e2",
        "priority": 2000,
        "description": "",
        "boardId": "a1"
    },
    {
        "id": "6",
        "name": "Going to lake side",
        "date": datetime(2023, 7, 6),
        "listId": "e3",
        "priority": 3000,
        "description": "",
        "boardId": "a1"
    },
    {
        "id": "7",
        "name": "New board task created",
        "date": datetime(2019, 4, 3),
        "listId": "e3",
        "priority": 4000,
        "description": "",
        "boardId": "a1"
    },
]


def read_tasks(boardId):
    task_list = []
    for task in TASKS:
        if task.get("boardId") == boardId:
            task_list.append(task)

    return task_list


def create(boardId, task):
    task_id = task.get("id")
    name = task.get("name")
    description = task.get("description", "")
    priority = task.get("priority", int())
    listId = task.get("listId", "")
    date = task.get("date", "")

    if date != "":
        date_frmt = "%Y-%m-%d"
        date = datetime.strptime(date, date_frmt)
    else:
        date = datetime.now()

    for task in TASKS:
        if task_id and task.get("id") != task_id:
            continue
        else:
            if task.get("boardId") == boardId:
                abort(
                    406,
                    f"Task with the name of {name} already exists",
                )

    print(date)

    dict_instance = {
        "id": task_id,
        "name": name,
        "description": description,
        "priority": priority,
        "listId": listId,
        "date": date
    }
    TASKS.append(dict_instance)
    return 201


def read_one(id):
    for task in TASKS:
        if task.get("id") == id:
            return task

    abort(
        404, f"Task with the id({id}) not found"
    )


def delete(id):
    for idx in range(0, len(TASKS)):
        if TASKS[idx].get("id") == id:
            del TASKS[idx]
            return make_response(
                f"The task with the ID ({id}) successfully deleted", 200
            )

    abort(
        404,
        f"Task with the ID({id}) not found"
    )


def update(id, task):
    print(id)
    for idx in range(0, len(TASKS)):
        if TASKS[idx].get("id") == id:
            my_task = TASKS[idx].get("description")
            my_task = task.get("description", my_task)
            return my_task

    abort(
        404,
        f"Task with the ID ({id}) not found"
    )






