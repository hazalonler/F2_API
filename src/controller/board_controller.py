from dataclasses import dataclass


@dataclass
class BoardConfig:
    board_name: str
    board_id: str
    list_config: list


BOARD_CONFIG = BoardConfig("Hazal's Project", "a1", [
            {
                "id": 'e1',
                "name": "Backlog",
                "style": {
                    "backgroundColor": "rgb(255, 204, 204)",
                    "borderRadius": "12px",
                    "width": "230px"
                }
            },
            {
                "id": 'e2',
                "name": "To-Do",
                "style": {
                    "backgroundColor": "rgb(255, 204, 204)",
                    "borderRadius": "12px",
                    "width": "230px"
                }
            },
            {
                "id": 'e3',
                "name": "In-Progress",
                "style": {
                    "backgroundColor": "rgb(255, 204, 204)",
                    "borderRadius": "12px",
                    "width": "230px"
                }
            },
            {
                "id": 'e4',
                "name": "Done",
                "style": {
                    "backgroundColor": "rgb(255, 204, 204)",
                    "borderRadius": "12px",
                    "width": "230px"}
            },
        ])


def read_board(boardId):
    if BOARD_CONFIG.board_id == boardId:
        return BOARD_CONFIG


