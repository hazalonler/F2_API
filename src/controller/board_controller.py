from src.dao.board_dao import board_dao_instance as board_dao


def find_board():
    return board_dao.find()


