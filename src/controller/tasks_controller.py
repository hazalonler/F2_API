from datetime import datetime
from flask import abort, make_response
from src.dao.task_dao import Task_Dao
from src.dao.task_dao import task_dao_instance as task_dao


def find_tasks(boardId, listId):
    return task_dao.find_tasks(boardId, listId)


def create(boardId, listId, task):
    try:
        date = int(datetime.utcnow().timestamp()) * 1000
        description = task.get("description", "")
        name = task.get("name")
        priority = task.get("priority", int())

        task_document = {"name": name, "creationTs": date, "updatedTs": date, "listId": listId,
                         "boardId": boardId, "priority": priority, "description": description}

        generated_id = Task_Dao().create(task_document)
        return {'id': str(generated_id)}, 201

    except BaseException:
        return 404
    except:
        return {}, 500


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
