import pymongo
from bson import ObjectId
from src.model.task_config import Task


class Task_Dao:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.database = self.client["F2"]
        self.task_collection = self.database["task"]

    def __custom_json_encoder(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def find_tasks(self, board_id, list_id):
        result = []
        query_find = {"listId": list_id, "boardId": board_id}
        cursor = self.task_collection.find(query_find).sort("priority")
        for task_dict in cursor:
            task_dict["_id"] = str(task_dict.get("_id"))
            result.append(Task.toJSON(task_dict))

        return result

    def create(self, task):
        if self.task_collection is not None:
            return self.task_collection.insert_one(task).inserted_id

        raise BaseException("'task_collection' is not initialized!")

    # It does not create a new task because of task_config and _id issues

    def delete(self, task_id):
        if self.task_collection.delete_one({"_id": ObjectId(task_id)}).deleted_count:
            return True
        raise BaseException(f"task with {task_id} is not found")

    def updates(self, task_id, task):

        query_update = {"_id": ObjectId(task_id)}
        new_values = {"$set": {"priority": task.get("priority"), "listId": task.get("listId"), "description": task.get(
            "description")}}

        x = self.task_collection.update_one(query_update, new_values)
        if x.modified_count:
            return True

        if ObjectId(task_id) is None:
            raise NameError(f"Task with {task_id} is not found!")

        raise BaseException("task is not updated!")


task_dao_instance = Task_Dao()