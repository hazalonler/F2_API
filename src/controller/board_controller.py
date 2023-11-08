from src.dao.board_dao import board_dao_instance as board_dao

Board = board_dao.find()


def find_board():
    return Board


