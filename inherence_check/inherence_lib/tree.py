from re import split
from typing import List, Tuple

from .rule import Rule, RuleException
from .inherence_lib_exception import TreeException
from .sequency_parser import SequencyParser
from .factory import FactoryParser


class Tree:
    """
    Объект этого класса представляет собой дерево вывода.
    На вход подается список строк - каждая строка представляет собой список секвенций
    Каждая пара смежных строк представляет список правил
    Секвенции принадлежащие одному правилу должны отделяться от секвенций другого правила спецсимволом
    """

    def __init__(self, tree: Tuple[str], separator: str = '||'):
        self.__parser_sequency: SequencyParser = FactoryParser['sequency']
        self.__tree_inherence: List[List[Rule]] = list()
        self.__separator: str = separator
        if not tree:
            raise TreeException('Tree of Inherence is Empty')
        self.__parse(tree)

    def __parse(self, tree: Tuple[str]):
        for index in range(len(tree) - 2, -1, -1):
            ls_rules: List[Rule] = self.__create_list_rules(*tree[index: index + 2])
            self.__tree_inherence.append(ls_rules)

    def __create_list_rules(self, first: str, second: str) -> List[Rule]:
        upper_ls: List[str] = split(r'\|\|', first)
        lower_ls: List[str] = list(split(r'; ', second.replace(self.__separator, '; ')))
        if len(upper_ls) < len(lower_ls):
            for lexem in lower_ls:
                self.__parser_sequency.parse(lexem)
                if self.__parser_sequency.is_axiom(lexem):
                    lower_ls.remove(lexem)
        if len(upper_ls) != len(lower_ls):
            raise TreeException('Count of items not Valid.')
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
