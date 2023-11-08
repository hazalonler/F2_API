from dataclasses import dataclass
from src.model.board_style import Style


@dataclass
class ListConfig:
    id: str
    name: str
    style: Style

