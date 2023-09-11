import pymongo
import json
from bson import ObjectId
from flask import abort

client = pymongo.MongoClient('mongodb://localhost:27017/')
database = client["F2"]
task_collection = database["tasks"]


def custom_json_encoder(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


class Task_Dao:
    def read_task(self, board_id, list_id):
        returned_task = []
        query_for_read = {"listId": list_id, "boardId": board_id}
        cursor = task_collection.find(query_for_read).sort("priority")
        for each_task in cursor:
            json_task = json.dumps(each_task, default=custom_json_encoder)
            parsed_task_data = json.loads(json_task)
            returned_task.append(parsed_task_data)

        return returned_task

    def create(self, task):
        task_collection.insert_one(task)
        return 201

    def delete(self, task_id):
        Tasks = []
        for each_task in task_collection.find():
            Tasks.append(each_task)

        json_tasks = json.dumps(Tasks, default=custom_json_encoder)
        parsed_tasks_data = json.loads(json_tasks)

        for task in parsed_tasks_data:
            if task["_id"] == task_id:
                task_collection.delete_one(task)
                return 200
            return 404

    def updates(self, task_id, task):
        query_id = str()

        for each_task in task_collection.find():
            json_tasks = json.dumps(each_task, default=custom_json_encoder)
            parsed_tasks_data = json.loads(json_tasks)

            if parsed_tasks_data["_id"] == task_id:
                query_id = each_task["_id"]

        query_update = {"_id": query_id}
        my_result = task_collection.find(query_update)
        for x in my_result:
            print(x)
        new_values = {"$set": {"priority": task.get("priority")}}

        x = task_collection.update_one(query_update, new_values)
        if x.modified_count != 0:
            return 200
        else:
            return 404
