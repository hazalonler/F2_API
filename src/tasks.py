import datetime
from flask import abort, make_response

TASKS = [
    {
        "id": "1",
        "name": "Prepare a new board",
        "date": datetime.date(2023, 4, 3),
        "listId": "e1",
        "priorty": 1000,
        "description": "",
    },
    {
        "id": "2",
        "name": "Prepare a task list",
        "date": datetime.date(2023, 5, 6),
        "listId": "e2",
        "priorty": 1000,
        "description": "",
    },
    {
        "id": "3",
        "name": "naming",
        "date": datetime.date(2022, 5, 6),
        "listId": "e3",
        "priorty": 1000,
        "description": "",
    },
    {
        "id": "4",
        "name": "Make a to-do list for shopping",
        "date": datetime.date(2021, 4, 3),
        "listId": "e3",
        "priorty": 2000,
        "description": "",
    },
    {
        "id": "5",
        "name": "edit",
        "date": datetime.date(2023, 5, 8),
        "listId": "e2",
        "priorty": 2000,
        "description": "",
    },
    {
        "id": "6",
        "name": "Going to lake side",
        "date": datetime.date(2023, 7, 6),
        "listId": "e3",
        "priorty": 3000,
        "description": "",
    },
    {
        "id": "7",
        "name": "New board task created",
        "date": datetime.date(2019, 4, 3),
        "listId": "e3",
        "priorty": 4000,
        "description": "",
    },
]


def read_tasks():
    return TASKS


def create(task):
    task_id = task.get("id")
    name = task.get("name")
    description = task.get("description", "")
    priorty = task.get("priorty", int())
    listId = task.get("listId", "")

    for task_in_list in TASKS:
        for value in task_in_list.values():
            if task_id and value != task_id:
                continue
            else:
                abort(
                    406,
                    f"Task with the name of {name} already exists",
                )

    dict_instance = {
        "id": task_id,
        "name": name,
        "description": description,
        "priorty": priorty,
        "listId": listId,
    }
    TASKS.append(dict_instance)
    return 201


def read_one(id):
    for task in TASKS:
        if task.get("id") == id:
            return task

    abort(
        404, f"Task with the ID({id}) not found"
    )


def delete(id):
    for idx in range(0, len(TASKS)):
        if TASKS[idx].get("id") == id:
            del TASKS[idx]
            return make_response(
                f"The ID({id}) successfully deleted", 200
            )

    abort(
        404,
        f"Task with the ID({id}) not found"
    )




