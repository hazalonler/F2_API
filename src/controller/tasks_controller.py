from flask import make_response
from src.dao.task_dao import task_dao_instance as task_dao
import logging


def find(boardId, listId):
    try:
        return task_dao.find(boardId, listId), 200
    except Exception as e:
        # exceptionlari(e) return etme
        logging.exception(f"Failed to find task collection with listId{listId} in board{boardId}, Exception: {e}")
        return {f"Failed to find task collection with listId{listId} in board{boardId}"}, 500


def create(boardId, listId, task):
    try:
        generated_id = task_dao.create(listId, boardId, task)
        return {'id': str(generated_id)}, 201
    except Exception as e:
        logging.exception(f"Failed to create new task in list{listId} of board{boardId}, Exception: {e}")
        return {f"Failed to create new task in list{listId} of board{boardId}"}, 500


def delete(_id):
    try:
        is_deleted = task_dao.delete(_id)
        return {"deleted": is_deleted}, 200
    except Exception as e:
        logging.exception(f"Failed to delete task{_id}, Exception: {e}")
        return {f"Failed to delete task{_id}"}, 500


def update(_id, task):
    try:
        is_updated = task_dao.update(_id, task)

        if is_updated is True:
            return make_response(
                f"The task with the ID {_id} successfully updated", 200
            )
    except Exception as e:
        logging.exception(f"Failed to update task({_id})! Data: {task}, Exception: {e}")
        return {"result": f"Failed to update task({_id})"}, 500
