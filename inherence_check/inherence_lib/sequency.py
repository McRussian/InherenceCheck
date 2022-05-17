from re import split
from typing import Dict, List

from inherence_check.inherence_lib import SequencyException
from inherence_check.parser import FactoryParser, SequencyParser, SequencyParserException


class Sequency:
    def __init__(self, sequency: str):
        self.__parser: SequencyParser = FactoryParser['sequency']

        self.__part_sequency: Dict[str, str] = dict()
        self.__operator = '==>'
        self.__parse_sequency(sequency)

    @staticmethod
    def __create_pattern(part: str) -> str:
        # TODO: Здесь будет вызываться парсер и создаваться паттерны для левой и правой части
        #       Пока простая заглушка
        # TODO: Верхняя часть может содержать несколько формул, разделенных ;
        #       Подумать что именно будет возвращаться, список формул?
        return part.strip()

    def __parse_sequency(self, sequency: str):
        if not self.__parser.parse(sequency):
            raise SequencyException('The entered string is not a sequence')

        left_part, right_part = split(self.__operator, sequency, maxsplit=1)
        self.__part_sequency['left_part'] = self.__create_pattern(left_part)
        self.__part_sequency['right_part'] = self.__create_pattern(right_part)

    def get_part_sequency(self, name):
        if name in self.__part_sequency.keys():
            return self.__part_sequency[name]
        raise AttributeError

    def __str__(self) -> str:
        return f"{self.__part_sequency['left_part']} {self.__operator} {self.__part_sequency['right_part']}"

    def __eq__(self, other):
        if not isinstance(other, str) and not isinstance(other, Sequency):
            raise SequencyException('Sequency I can only compare with a string or another axiom')

        other_sequency: Sequency
        if isinstance(other, str):
            other_sequency = Sequency(other)
        else:
            other_sequency = other
        return self.__parser.sequency_equal(str(self), str(other_sequency))


class Sequencys:
    def __init__(self, sequencys: List[str]):
        if not sequencys:
            SequencyException('Sequencys list cannot be empty')
        self.__sequency: List[Sequency] = list()
        for rule in set(sequencys):
            try:
                sequency = Sequency(rule)
            except SequencyException:
                continue
            self.__sequency.append(sequency)

