import pymongo
import json
from bson import ObjectId

from src.model.task_config import Task


class Task_Dao:
    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.database = self.client["F2"]
        self.task_collection = self.database["tasks"]

    def __custom_json_encoder(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    def find_tasks(self, board_id, list_id):
        result = []
        query_for_read = {"listId": list_id, "boardId": board_id}
        cursor = self.task_collection.find(query_for_read).sort("priority")
        for task_dict in cursor:
            task_dict["_id"] = str(task_dict.get("_id"))
            Task(**task_dict)
            result.append(task_dict)

        return result

    def create(self, task):
        if self.task_collection is not None:
            return self.task_collection.insert_one(task).inserted_id

        raise BaseException("'task_collection' is not initialized!")

    def delete(self, task_id):
        Tasks = []
        for each_task in self.task_collection.find():
            Tasks.append(each_task)

        json_tasks = json.dumps(Tasks, default=self.__custom_json_encoder)
        parsed_tasks_data = json.loads(json_tasks)
        print(parsed_tasks_data)
        print(task_id)

        for task in parsed_tasks_data:
            if task["_id"] == task_id:
                self.task_collection.delete_one(task)
                return 200
            return 404

    def updates(self, task_id, task):
        query_id = str()
# asdsad
        for each_task in self.task_collection.find():
            json_tasks = json.dumps(each_task, default=self.__custom_json_encoder)
            parsed_tasks_data = json.loads(json_tasks)

            if parsed_tasks_data["_id"] == task_id:
                query_id = each_task["_id"]

        query_update = {"_id": query_id}
        new_values = {"$set": {"priority": task.get("priority"), "listId": task.get("listId"), "description": task.get(
            "description")}}

        x = self.task_collection.update_one(query_update, new_values)
        if x.modified_count:
            return 200
        else:
            return 404


task_dao_instance = Task_Dao()