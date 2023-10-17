import pymongo
import json
from bson import ObjectId
from src.model.board_config import BoardConfig

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


BOARD = {
    "boards": [
        BoardConfig(parsed_board_data["boardName"], parsed_board_data["_id"], parsed_board_data["listConfig"])
    ]
}


def find_board():
    boards = BOARD.get("boards")
    return boards
