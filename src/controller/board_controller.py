from dataclasses import dataclass
import pymongo
import json
from bson import ObjectId

my_client = pymongo.MongoClient('mongodb://localhost:27017/')
my_database = my_client["F2"]
my_board_collection = my_database["boardConfig"]

Board = my_board_collection.find_one()


def custom_json_encoder(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")


json_board = json.dumps(Board, default=custom_json_encoder)
parsed_board_data = json.loads(json_board)


@dataclass
class Style:
    background_color: str
    border_radius: str
    width: str


@dataclass
class ListConfig:
    id: str
    name: str
    style: Style


@dataclass
class BoardConfig:
    board_name: str
    board_id: str
    list_config: list[ListConfig]


BOARD = {
    "boards": [
        BoardConfig(parsed_board_data["boardName"], parsed_board_data["_id"], parsed_board_data["listConfig"])
    ]
}


def read_board():
    boards = BOARD.get("boards")
    return boards
