from app.shared.dto import Dto


class Handler:
    def __init__(self):
        ...

    def execute(self, dto: Dto) -> None: 
        raise NotImplementedError