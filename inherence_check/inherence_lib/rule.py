from re import split
from typing import Dict, List, Set

from inherence_check.inherence_lib import Sequency, SequencyException, RuleException


class Rule:
    def __init__(self, left: str, right: str):
        self.__upper_part: Set[Sequency] = set()
        self.__lower_part: Sequency

        try:
            sequency = Sequency(right)
        except SequencyException as err:
            raise RuleException(str(err))
        self.__lower_part = sequency

        patterns = split('; +', left)
        for pattern in patterns:
            try:
                sequency = Sequency(pattern)
            except SequencyException as err:
                raise RuleException(str(err))
            self.__upper_part.add(sequency)

    def __eq__(self, other):
        if isinstance(other, Rule):
            raise RuleException('Rule I can only compare with another rule')

        return self.__lower_part == other.__lower_part and self.__upper_part == other.__upper_part

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
            raise RuleException('The list of rules cannot contain objects of a different type')

        return item in self.__rules

    def __len__(self) -> int:
        return len(self.__rules)

