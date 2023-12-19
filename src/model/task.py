from dataclasses import dataclass
from datetime import datetime
from dataclasses import asdict

@dataclass
class Task:
    name: str
    creationTs: int
    updatedTs: int
    listId: str
    boardId: str
    priority: str
    id: object = None
    description: str = ""

    @staticmethod
    def fromJSON(listId, boardId, task):
        date = int(datetime.utcnow().timestamp()) * 1000
        description = task.get("description", "")
        name = task.get("name")
        priority = task.get("priority")
        return Task(name, date, date, listId, boardId, priority, description)

    @staticmethod
    def fromBSON(task):
        task_id = task.get("id")
        name = task.get("name")
        creationTs = task.get("creationTs")
        updatedTs = task.get("updatedTs")
        listId = task.get("listId")
        boardId = task.get('boardId')
        priority = task.get("priority")
        description = task.get("description")

        return Task(name, creationTs, updatedTs, listId, boardId, priority, task_id, description)

    @staticmethod
    def asDict(task):
        dict = asdict(task)
        dict.pop("id")
        return dict

    # @dataclass
    # class B:
    #     id: ObjectId = field(init=False)
#
    #     def __post_init__(self):
    #         self.id = ObjectId()