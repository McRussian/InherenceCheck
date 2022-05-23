class InherenceException(Exception):
    def __init__(self, msg: str):
        self.__msg = msg

    def __str__(self) -> str:
        return self.__msg


class VariableException(InherenceException):
    pass


class AxiomException(InherenceException):
    pass


class SequencyException(InherenceException):
    pass


class RuleException(InherenceException):
    pass


class TreeException(InherenceException):
    pass


class SequencyParserException(InherenceException):
    pass


class PatternComparatorException(InherenceException):
    pass
