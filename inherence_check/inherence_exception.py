class InherenceException(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self) -> str:
        return self.__msg
