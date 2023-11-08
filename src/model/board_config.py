from dataclasses import dataclass
from src.model.list_config import ListConfig


@dataclass
class BoardConfig:
    board_name: str
    board_id: str
    list_config: list[ListConfig]


    @staticmethod
    def toJSON(board):
        id = board.get("_id")
        name = board.get("boardName")
        listConfig = board.get("listConfig")

        return BoardConfig(name, id, listConfig)


