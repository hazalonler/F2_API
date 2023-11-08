import pymongo
from bson import ObjectId
from src.model.board_config import BoardConfig

class Board_Dao:

    def __init__(self):
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.database = self.client["F2"]
        self.board_collection = self.database["board"]

    def find(self):
        result = []
        cursor = self.board_collection.find()
        for board_dict in cursor:
            board_dict["_id"] = str(board_dict.get("_id"))
            result.append(BoardConfig.toJSON(board_dict))

        return result


board_dao_instance = Board_Dao()

