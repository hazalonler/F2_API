from dataclasses import dataclass
from src.model.style import Style


@dataclass
class ListConfig:
    id: str
    name: str
    style: Style

