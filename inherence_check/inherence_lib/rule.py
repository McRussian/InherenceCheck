from re import split
from typing import Dict, List

from .sequency import Sequency, SequencyException
from .inherence_lib_exception import RuleException


class Rule:
    def __init__(self, left: str, right: str):
        self.__upper_part: List[Sequency] = list()
        self.__lower_part: Sequency

        try:
            sequency = Sequency(right)
        except SequencyException as err:
            raise RuleException(str(err))
        self.__lower_part = sequency

        try:
            patterns = split('; +', left)
        except Exception as err:
            print(left)
            print(f'Error split: {err}')

        for pattern in patterns:
            try:
                sequency = Sequency(pattern)
            except SequencyException as err:
                raise RuleException(str(err))
            self.__upper_part.append(sequency)

    def __eq__(self, other):
        if not isinstance(other, Rule):
            raise RuleException(f'Rule {self} I can only compare with another rule {other}')
        if self.__lower_part != other.__lower_part:
            return False
        if len(self.__upper_part) != len(other.__upper_part):
            return False
        for seq1, seq2 in zip(self.__upper_part, other.__upper_part):
            if seq1 != seq2:
                return False
        return True

    def __str__(self) -> str:
        upper: str = '; '.join(map(str, self.__upper_part))
        count: int = max(len(str(self.__lower_part)), len(upper))
        return upper.center(count, ' ') + "\n" + "-" * count + "\n" + str(self.__lower_part).center(count, ' ')


class Rules:
    def __init__(self, rules: List[str], separator: str = '==='):
        self.__separator = separator
        if not rules:
            RuleException('Rules list cannot be empty')
        self.__rules: List[Rule] = list()
        for rule in set(rules):
            if self.__separator not in rule:
                raise RuleException('Format error, no valid delimiter')
            left, right = split(self.__separator, rule, maxsplit=2)
            try:
                rule = Rule(left, right)
            except RuleException:
                continue
            self.__rules.append(rule)

    def __contains__(self, item) -> bool:
        if not isinstance(item, Rule):
            raise RuleException('The list of rules cannot contain objects %r of a different type', item)

        return item in self.__rules

    def __len__(self) -> int:
        return len(self.__rules)

