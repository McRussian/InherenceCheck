from re import split
from typing import Dict, List

from inherence_check.inherence_lib import SequencyException
from inherence_check.parser import FactoryParser, FactorComparator, \
    SequencyParser, SequencyParserException, \
    PatternComparator, PatternComparatorException


class Sequency:
    def __init__(self, sequency: str, operator: str = '==>'):
        self.__parser: SequencyParser = FactoryParser['sequency']
        self.__comparator: PatternComparator = FactorComparator['sequency']
        self.__operator: str = operator
        self.__sequency: str = sequency
        self.__parse_sequency(sequency)
        self.__pattern: str = ''

    def __parse_sequency(self, sequency: str):
        if not self.__parser.parse(sequency):
            raise SequencyException('The entered string is not a sequence')

        self.__pattern = self.__parser.pattern(self.__sequency)

    def __str__(self) -> str:
        return self.__sequency

    def __eq__(self, other) -> bool:
        if not isinstance(other, str) and not isinstance(other, Sequency):
            raise SequencyException('Sequency I can only compare with a string or another axiom')

        return self.__comparator.compare_pattern(str(self), str(other))


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

    def __contains__(self, item):
        if not isinstance(item, Sequency):
            raise SequencyException('The list of sequency cannot contain objects of a different type')

        return item in self.__sequency
