import pymongo
from bson import ObjectId
from src.model.task import Task


class Task_Dao:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.database = self.client["F2"]
        self.task_collection = self.database["task"]

    def __custom_json_encoder(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def find(self, board_id, list_id):
        result = []
        query_find = {"listId": list_id, "boardId": board_id}
        cursor = self.task_collection.find(query_find).sort("priority")
        for task_dict in cursor:
            task_dict["id"] = str(task_dict.get("_id"))
            result.append(Task.fromBSON(task_dict))

        return result

    def create(self, listId, boardId, task):
        return self.task_collection.insert_one(
            Task.asDict(
                Task.fromJSON(listId, boardId, task)
            )
        ).inserted_id

    def delete(self, task_id):
        if self.task_collection.delete_one(
                {"_id": ObjectId(task_id)}
        ).deleted_count:
            return True

        return False

    def update(self, task_id, task):
        update_condition = {"_id": ObjectId(task_id)}
        new_values = {
            "$set": {
                "priority": task.get("priority"),
                "listId": task.get("listId"),
                "description": task.get("description")
            }
        }

        if self.task_collection.update_one(update_condition, new_values).modified_count:
            return True

        return False


task_dao_instance = Task_Dao()