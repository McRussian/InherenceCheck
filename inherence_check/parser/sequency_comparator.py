from typing import Dict, List, Tuple, Optional
from re import split

from inherence_check.parser import PatternComparatorException


class PatternComparator:
    def __init__(self, separator: str = '|-',
                 default_sequency: str = 'G',
                 unary: Tuple[str] = ('-', ),
                 binary: Tuple[str] = ('=>', '&', 'V'),
                 ):
        self.__separator: str = separator
        self.__default_sequency: List[str] = [default_sequency + str(i) for i in range(10)]
        self.__default_sequency[0] = default_sequency
        self.__unary: Tuple[str] = unary
        self.__binary: Tuple[str] = binary

    def compare_pattern(self, pattern_left: str, pattern_right: str) -> bool:
        """
        функция проверят два шаблона секвенции на равенство.
        :param pattern_left:
        :param pattern_right:
        :return:
        """
        left_lexems: List[str] = ['', '']
        right_lexems: List[str] = ['', '']
        left_lexems[0], right_lexems[0] = split(r"\|-", self.__remove_unary_operations(pattern_left))
        left_lexems[1], right_lexems[1] = split(r"\|-", self.__remove_unary_operations(pattern_right))

        if not self.__check_left_parts(*left_lexems):
            return False

        if not self.__check_structure_with_binary(*right_lexems):
            return False
        return True

    def __remove_unary_operations(self, pattern: str) -> str:
        for operator in self.__unary:
            while operator in pattern:
                pattern = pattern.replace(f'{operator} ', '')
        return pattern

    def __check_forall_sequency(self, pattern: str) -> bool:
        lexems: List[str] = pattern.split()
        if not lexems:
            return True
        if sum([lexems.count(seq) for seq in self.__default_sequency]) == 1 and \
            sum([lexems.count(operator) for operator in self.__binary]) == 0:
            return True
        return False

    def __check_left_parts(self, left: str, right: str) -> bool:
        if self.__check_forall_sequency(left) and self.__check_forall_sequency(right):
            return True
        if not self.__check_forall_sequency(left) and not self.__check_forall_sequency(right):
            return len(left.split()) == len(right.split())
        return False

    def __check_structure_with_binary(self, left: str, right: str) -> bool:
        if len(left.split()) != len(right.split()):
            return False
        for operator in self.__binary:
            if len(split(operator, left)) != len(split(operator, right)):
                return False
        return True
