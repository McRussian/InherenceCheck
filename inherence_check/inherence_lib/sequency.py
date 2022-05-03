from re import split
from typing import Dict, List

from inherence_check.inherence_lib import SequencyException


class Sequency:
    def __init__(self, sequency: str):
        self.__part_sequency: Dict[str, str] = dict()
        self.__operator = '==>'
        self.__parse(sequency)

    @staticmethod
    def __create_pattern(part: str) -> str:
        # TODO: Здесь будет вызываться парсер и создаваться паттерны для левой и правой части
        #       Пока простая заглушка
        # TODO: Верхняя часть может содержать несколько формул, разделенных ;
        #       Подумать что именно будет возвращаться, список формул?
        return part.strip()

    def __parse(self, sequency: str):
        if self.__operator not in sequency:
            raise SequencyException('Wrong sequency format, no relation between parts')
        upper_part, lower_part = split(self.__operator, sequency, maxsplit=1)
        self.__part_sequency['upper_part'] = self.__create_pattern(upper_part)
        self.__part_sequency['lower_part'] = self.__create_pattern(lower_part)

    def get_part_sequency(self, name):
        if name in self.__part_sequency.keys():
            return self.__part_sequency[name]
        raise AttributeError

    def __eq__(self, other):
        if not isinstance(other, str) and not isinstance(other, Sequency):
            raise SequencyException('Sequency I can only compare with a string or another axiom')

        other_sequency: Sequency
        if isinstance(other, str):
            other_sequency = Sequency(other)
        else:
            other_sequency = other

        return all([self.__part_sequency[name] == other_sequency.get_part_sequency(name) for name in self.__part_sequency.keys()])


class Sequencys:
    def __init__(self, rules: List[str]):
        if not rules:
            SequencyException('Sequencys list cannot be empty')
        self.__sequency: List[Sequency] = list()
        for rule in set(rules):
            try:
                sequency = Sequency(rule)
            except SequencyException:
                continue
            self.__sequency.append(sequency)

        if not rules:
            SequencyException('Sequencys list cannot be empty')
