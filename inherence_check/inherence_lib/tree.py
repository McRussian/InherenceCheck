from re import split
from typing import List

from inherence_check.inherence_lib import Rule, RuleException, TreeException


class Tree:
    """
    Объект этого класса представляет собой дерево вывода.
    На вход подается список строк - каждая строка представляет собой список секвенций
    Каждая пара смежных строк представляет список правил
    Секвенции принадлежащие одному правилу должны отделяться от секвенций другого правила спецсимволом
    """

    def __init__(self, tree: List[str], separator: str = '||'):
        self.__tree_inherence: List[List[Rule]] = list()
        self.__separator: str = separator
        if not tree:
            raise TreeException('Tree of Inherence is Empty')
        self.__parse(tree)

    def __parse(self, tree: List[str]):
        for index in range(len(tree) - 1):
            ls_rules: List[Rule] = self.__create_list_rules(*tree[index: index + 2])
            self.__tree_inherence.append(ls_rules)

    def __create_list_rules(self, first: str, second: str) -> List[Rule]:
        upper_ls: List[str] = split(self.__separator, first)
        lower_ls: List[str] = list(second.replace(self.__separator, ' ').split())
        if len(upper_ls) != len(lower_ls):
            raise TreeException('Count of rules is invalid')

        ls_rules: List[Rule] = list()
        for left, right in zip(upper_ls, lower_ls):
            try:
                rule = Rule(left, right)
            except RuleException as err:
                raise TreeException(str(err))
            ls_rules.append(rule)
        return ls_rules

    def __len__(self) -> int:
        return len(self.__tree_inherence)

    def __iter__(self):
        return iter(self.__tree_inherence)
