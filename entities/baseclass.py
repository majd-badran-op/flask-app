from dataclasses import dataclass


@dataclass
class BaseEntity:
    id: int

    def __init__(self, id: int):
        self.id = id
