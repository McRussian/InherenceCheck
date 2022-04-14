from re import split
from typing import Dict, Tuple

from inherence_check.inherence_lib import LOGICAL_RELATIONS, AxiomException


class Axiom:
    def __init__(self, axiom: str):
        self.__pattern_rule: Dict[str, str] = dict()
        self.__parse(axiom)

    @staticmethod
    def __split_for_operation(axiom: str) -> Tuple[str, str, str]:
        for operation in LOGICAL_RELATIONS:
            if operation in axiom:
                left, right = split(operation, axiom, maxsplit=1)
                return left, operation, right
        raise AxiomException('Wrong axiom format, no logical relation operation')

    @staticmethod
    def __create_pattern(part: str) -> str:
        # TODO: Здесь будет вызываться парсер и создаваться паттерны для левой и правой части
        #       Пока простая заглушка
        return part.strip()

    def __parse(self, axiom: str):
        left, operation, right = self.__split_for_operation(axiom)
        self.__pattern_rule['left_pattern'] = self.__create_pattern(left)
        self.__pattern_rule['operator'] = operation
        self.__pattern_rule['right_pattern'] = self.__create_pattern(right)
        # Считаем что аксиома должна быть вида {f} op {f}, другие шаблоны не рассматриваем
        if self.__pattern_rule['left_pattern'] != self.__pattern_rule['right_pattern']:
            raise AxiomException('Wrong Axiom pattern, left part different form right part.')

    def __len__(self) -> int:
        return len(self.__pattern_rule)

    def get_part_axiom(self, name):
        if name in self.__pattern_rule.keys():
            return self.__pattern_rule[name]
        raise AttributeError

    def __eq__(self, other):
        if not isinstance(other, str) and not isinstance(other, Axiom):
            raise AxiomException('Axiom I can only compare with a string or another axiom')

        other_axiom: Axiom
        if isinstance(other, str):
            other_axiom = Axiom(other)
        else:
            other_axiom = other

        return all([self.__pattern_rule[name] == other_axiom.get_part_axiom(name) for name in self.__pattern_rule.keys()])
