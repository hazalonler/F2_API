BOARD_CONFIG = {
    "boardName": "Hazal's Project",
    "listConfig": [
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
    ]
}


def read_board():
    return BOARD_CONFIG


