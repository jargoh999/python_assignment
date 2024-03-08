
class PlayerLimitReachedException(Exception):
    def __init__(self, message: str):
        super().__init__(message)


class TileIsOccupiedException(Exception):
    def __init__(self, message: str):
        super().__init__(message)
