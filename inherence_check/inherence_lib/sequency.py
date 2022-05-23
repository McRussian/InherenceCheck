from re import split
from typing import Dict, List
import sys
sys.path.append(".")

from .inherence_lib_exception import SequencyException, SequencyParserException, PatternComparatorException
from .sequency_parser import SequencyParser
from .sequency_comparator import PatternComparator
from .factory import FactorComparator, FactoryParser


class Sequency:
    def __init__(self, sequency: str, operator: str = '|-'):
        self.__parser: SequencyParser = FactoryParser['sequency']
        self.__comparator: PatternComparator = FactorComparator['sequency']
        self.__operator: str = operator
        self.__sequency: str = sequency
        self.__pattern: str = ''
        self.__parse_sequency(sequency)

    def __parse_sequency(self, sequency: str):
        if not self.__parser.parse(sequency):
            raise SequencyException(f'The entered string {sequency} is not a sequence')

        self.__pattern = self.__parser.pattern(self.__sequency)

    @property
    def pattern(self) -> str:
        return self.__pattern

    def __str__(self) -> str:
        return self.__sequency

    def __eq__(self, other) -> bool:
        if not isinstance(other, str) and not isinstance(other, Sequency):
            raise SequencyException('Sequency I can only compare with a string or another axiom')
        return self.__comparator.compare_pattern(self.__pattern, other.__pattern)

    def __hash__(self):
        return hash(self.__sequency)


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
