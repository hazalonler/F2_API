from dataclasses import dataclass


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


style_config = Style("rgb(255, 204, 204)", "12px", "230px")


listConfig_1 = ListConfig("e1", "Backlog", style_config)
listConfig_2 = ListConfig("e2", "To-Do", style_config)
listConfig_3 = ListConfig("e3", "In-Progress", style_config)
listConfig_4 = ListConfig("e4", "Done", style_config)


BOARD_CONFIG = BoardConfig("Hazal's Project", "a1", [listConfig_1, listConfig_2, listConfig_3, listConfig_4])


def read_board(boardId):
    if BOARD_CONFIG.board_id == boardId:
        return BOARD_CONFIG


