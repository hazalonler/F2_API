from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    name: str
    creationTs: int
    updatedTs: int
    listId: str
    boardId: str
    _id: object = None
    priority: int = 1000
    description: str = ""

    @staticmethod
    def fromJSON(listId, boardId, task):
        date = int(datetime.utcnow().timestamp()) * 1000
        description = task.get("description", "")
        name = task.get("name")
        priority = task.get("priority", 1000)
        return Task(name, date, date, listId, boardId, None, priority, description)

    @staticmethod
    def toJSON(task):
        task_id = task.get("_id")
        name = task.get("name")
        creationTs = task.get("creationTs")
        updatedTs = task.get("updatedTs")
        listId = task.get("listId")
        boardId = task.get('boardId')
        priority = task.get("priority")
        description = task.get("description")

        return Task(name, creationTs, updatedTs, listId, boardId, task_id, priority, description)


    # @dataclass
    # class B:
    #     id: ObjectId = field(init=False)
#
    #     def __post_init__(self):
    #         self.id = ObjectId()