from dataclasses import dataclass


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
