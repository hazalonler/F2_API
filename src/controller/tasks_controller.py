from datetime import datetime
from flask import abort, make_response
from dataclasses import dataclass
from src.dao.task_dao import Task_Dao


@dataclass
class Task:
    _id: str
    name: str
    creationTs: int
    updatedTs: int
    listId: str
    boardId: str
    priority: int = 1000
    description: str = ""


def read_tasks(boardId, listId):
    task = Task_Dao()
    task_list = []
    result = task.read_task(boardId, listId)
    for task in result:
        task_list.append(Task(**task))
    return task_list


def create(boardId, listId, task):
    date = int(datetime.utcnow().timestamp()) * 1000
    description = task.get("description", "")
    name = task.get("name")
    priority = task.get("priority", int())

    task_document = {"name": name, "creationTs": date, "updatedTs": date, "listId": listId,
                     "boardId": boardId, "priority": priority, "description": description}

    created_task = Task_Dao()

    return created_task.create(task_document)


def delete(_id):
    deleted_task = Task_Dao().delete(_id)
    if deleted_task == 200:
        make_response(
            f"The task with the ID ({_id}) successfully deleted", 200
        )
    if deleted_task == 404:
        abort(
            404,
            f"Task with the ID({_id}) not found"
        )


def update(_id, task):
    updated_task = Task_Dao().updates(_id, task)

    if updated_task == 200:
        return make_response(
            f"The task with the ID {_id} successfully updated", 200
        )
    if updated_task == 404:
        return abort(
            404,
            f"Task with the ID {_id} not found"
        )
