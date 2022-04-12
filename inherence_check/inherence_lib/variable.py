from typing import List

from inherence_check.inherence_lib import ALL_LEXEMES, VariableException


class Variable:
    def __init__(self, name: str):
        if not name:
            raise VariableException("Object variable cannot have an empty name")
        if name in ALL_LEXEMES:
            raise VariableException("The variable name is the same as the service token name")
        self.__name = name

    def __str__(self) -> str:
        return self.__name

    @property
    def name(self) -> str:
        return self.__name

    def __eq__(self, other):
        if not isinstance(other, Variable):
            raise VariableException("A variable object cannot be compared with an object of another type")
        return self.__name == other.name


class Variables:
    def __init__(self, ls: List[str]):
        if not ls:
            raise VariableException("Variable list cannot be empty")
        self.__variables: List[Variable] = list()
        for name in set(ls):
            variable: Variable
            try:
                variable = Variable(name)
            except VariableException:
                continue
            self.__variables.append(variable)

        if not self.__variables:
            raise VariableException("Variable list cannot be empty")

    def __contains__(self, item: str):
        if not type(item) == str:
            raise VariableException("Inside the list of variables can only be strings")

        for variable in self.__variables:
            if item == variable.name:
                return True
        return False
