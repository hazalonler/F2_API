from dataclasses import dataclass
from src.model.list_config import ListConfig


@dataclass
class BoardConfig:
    name: str
    id: str
    list_configs: list[ListConfig]


    @staticmethod
    def fromBSON(board):
        id = board.get("_id")
        name = board.get("boardName")
        listConfigs = board.get("listConfigs")

        return BoardConfig(name, id, listConfigs)


