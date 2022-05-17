from re import split
from typing import Dict, List, Set

from inherence_check.inherence_lib import Sequency, SequencyException, RuleException


class Rule:
    def __init__(self, rule: str, separator: str = "==="):
        self.__upper_part: Set[Sequency] = set()
        self.__lower_part: Sequency
        self.__separator = separator
        self.__parse(rule)

    def __parse(self, rule: str):
        if self.__separator not in rule:
            raise RuleException('Format error, no valid delimiter')

        left, right = split(self.__separator, rule, maxsplit=2)
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


class Rules:
    def __init__(self, rules: List[str]):
        if not rules:
            RuleException('Rules list cannot be empty')
        self.__rules: List[Rule] = list()
        for rule in set(rules):
            try:
                rule = Rule(rule)
            except RuleException:
                continue
            self.__rules.append(rule)
