from dataclasses import asdict
from flask import make_response
from src.dao.task_dao import Task_Dao
from src.dao.task_dao import task_dao_instance as task_dao
from src.model.task_config import Task
import logging


def find_tasks(boardId, listId):
    return task_dao.find_tasks(boardId, listId), 200


def create(boardId, listId, task):
    try:
        generated_task = asdict(Task.fromJSON(listId, boardId, task))
        generated_id = Task_Dao().create(generated_task)
        return {'id': str(generated_id)}, 201

    except BaseException as e:
        print(f"Failed to create task on board({boardId}) in list({listId})! Task: {task}, Exception: {e}")
        return 404
    except:
        return {}, 500


def delete(_id):
    try:
        deleted_task = Task_Dao().delete(_id)
        if deleted_task:
            make_response(
                f"The task with the ID ({_id}) successfully deleted", 200
            )
    except BaseException as e:
        logging.exception(f"Task with the ID {_id} not found, Exception {e}")
        return 404


def update(_id, task):
    try:
        updated_task = Task_Dao().updates(_id, task)

        if updated_task is True:
            return make_response(
                f"The task with the ID {_id} successfully updated", 200
            )
    except BaseException as e:
        logging.exception(f"Failed to update task({_id})! Data: {task}, Exception: {e}")
        return {}, 500
    except NameError as err:
        logging.exception(f"Task with the ID {_id} not found, Exception {err}")
        return 404
