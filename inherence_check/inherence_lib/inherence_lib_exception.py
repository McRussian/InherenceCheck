

class InherenceLibException(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self) -> str:
        return self.__msg


class VariableException(InherenceLibException):
    pass


class AxiomException(InherenceLibException):
    pass


class SequencyException(InherenceLibException):
    pass
