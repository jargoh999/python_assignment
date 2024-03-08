from enum import Enum


class value_in_cell(Enum):
    EMPTY = "EMPTY"
    X = "X"
    O = "O"

    def __repr__(self):
        return f"{self.name}"
