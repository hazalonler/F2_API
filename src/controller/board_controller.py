import logging

from src.dao.board_dao import board_dao_instance as board_dao


def find_board():
    try:
        return board_dao.find()
    except Exception as e:
        logging.exception(f"Board is not found, Exception: {e}",)
        return {f"Board is not found"}, 500


