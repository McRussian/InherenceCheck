from re import split, sub
from typing import Any, Dict, List, Optional

from nltk import CFG
from nltk import ChartParser

from inherence_check.parser import SequencyParserException


class SequencyParser:
    def __init__(self,
                 follow: str = '==>',
                 formulas: List[str] = ['A', 'B', 'C'],
                 default_sequency: List[str] = ['G', 'D'],
                 ):
        self.__follow = follow
        self.__names_formulas = formulas.copy()
        self.__default_sequency = default_sequency.copy()

        self.__create_list_rules()

        self.__sequency_grammar = CFG.fromstring(self.__rules)
        self.__sequency_parser = ChartParser(self.__sequency_grammar)
        self.__sequency_trees: Dict[str, List[Any]] = dict()

    def parse(self, sequency: str) -> bool:
        lexems: List[str] = self.__transform_sequency(sequency)
        try:
            tree = self.__sequency_parser.parse(lexems)
        except ValueError as err:
            return False

        if tree is None:
            return False
        self.__sequency_trees[sequency] = tree
        print(self.__sequency_trees[sequency])
        return True

    def __create_list_rules(self):
        pattern = """
        S -> SEQUENCY FOLLOW SEQUENCY
        FOLLOW -> {}
        SEQUENCY -> '' | NAME_FORMULA SEQUENCY | SEQUENCY NAME_FORMULA | NAME_SEQUENCY SEQUENCY | SEQUENCE NAME_SEQUENCY
        NAME_SEQUENCY -> {}
        NAME_FORMULA -> {} 
        """
        rules = pattern.format(f"'{self.__follow}'", self.__create_list_variables(self.__default_sequency),
                                      self.__create_list_variables(self.__names_formulas))
        self.__rules = rules

    @staticmethod
    def __create_list_variables(ls: List[str]) -> str:
        return " | ".join([f"'{name}'" for name in ls])

    def __transform_sequency(self, seqeuncy: str) -> List[str]:
        sequency = seqeuncy.replace(self.__follow, f' {self.__follow} ')
        sequency = sub(r" {2,}", " ", sequency)
        pattern = r'[ ,]'

        return split(pattern, sequency)

    def __equal_tree(self, tree_a, tree_b) -> bool:
        '''
        Функция проверяет совпадение двух деревеьев вывода.
        Два дерева считаются одинаковыми, если они совпадают всюду,
        кроме конечных узлов (тех где формируются терминалы с именами формул, секвенций и переменных)
        '''
        print(type(tree_a))
        print(tree_b)
        return False

    def sequency_equal(self, seq_a: str, seq_b: str) -> bool:
        '''
        Функция проверт две секвенции на равенство
        Две секвенции считаются равными, если совпадают
        какие-нить деревья вывода из их список деревьев
        :param seq_a:
        :param seq_b:
        :return:
        '''
        if not self.parse(seq_a) or not self.parse(seq_b):
            return False
        tree_seq_a: List[Any] = self.__sequency_trees[seq_a]
        tree_seq_b: List[Any] = self.__sequency_trees[seq_b]

        for tree_a in tree_seq_a:
            for tree_b in tree_seq_b:
                if self.__equal_tree(str(tree_a), str(tree_b)):
                    return True
        return False
