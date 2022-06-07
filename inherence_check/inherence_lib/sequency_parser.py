from re import split, sub
from typing import Any, Dict, List, Tuple

from nltk import CFG
from nltk import ChartParser

from .inherence_lib_exception import SequencyParserException


class SequencyParser:
    def __init__(self,
                 follow: str = '|-',
                 formulas: Tuple[str] = ('A', 'B', 'C'),
                 default_sequency: str = 'G',
                 variables: Tuple[str] = ('x', 'y', 'z'),
                 unary_operations: Tuple[str] = ('-', ),
                 binary_operations: Tuple[str] = ('&', 'V', '=>'),
                 ):
        self.__follow = follow
        self.__names_formulas: Tuple[str] = formulas
        self.__default_sequency: List[str] = [default_sequency + str(i) for i in range(10)]
        self.__variables: Tuple[str] = variables
        self.__default_sequency[0] = default_sequency
        self.__unary_operations: Tuple[str] = unary_operations
        self.__binary_operations: Tuple[str] = binary_operations

        self.__create_list_rules()

        self.__sequency_grammar = CFG.fromstring(self.__rules)
        self.__sequency_parser = ChartParser(self.__sequency_grammar)
        self.__sequency_trees: Dict[str, List[Any]] = dict()
        self.__sequency_patterns: Dict[str, str] = dict()

    def parse(self, sequency: str) -> bool:
        lexems: List[str] = self.transform_sequency(sequency)
        try:
            tree = self.__sequency_parser.parse(lexems)
        except ValueError as err:
            return False

        if tree is None:
            return False
        self.__sequency_trees[sequency] = tree
        self.__sequency_patterns[sequency] = self.__create_pattern(lexems)
        return True

    def transform_sequency(self, seqeuncy: str) -> List[str]:
        sequency = seqeuncy.replace(self.__follow, f' {self.__follow} ')
        sequency = sub(r" {2,}", " ", sequency)
        pattern = r'[ ,]+'

        temps: List[str] = split(pattern, sequency)
        lexems: List[str] = list()
        for lexem in temps:
            if not lexem:
                continue
            if lexem in self.__names_formulas or lexem in self.__default_sequency or lexem == self.__follow:
                lexems.append(lexem)
                continue
            lexems.extend(self.__transform_operation(lexem))
        return lexems

    def pattern(self, sequency: str) -> str:
        if sequency not in self.__sequency_patterns.keys():
            raise SequencyParserException('There is no such sequence in the parser')
        return self.__sequency_patterns[sequency]

    def is_axiom(self, sequency: str) -> bool:
        if sequency not in self.__sequency_patterns.keys():
            raise SequencyParserException('There is no such sequence in the parser')

        return self.__sequency_patterns[sequency] == "F1 |- F1" or \
               self.__sequency_patterns[sequency] == "- F1 |- - F1" or \
               self.__sequency_patterns[sequency] == "- - F1 |- - - F1"

    def __create_list_rules(self):
        pattern = """
        S -> SEQUENCY FOLLOW SEQUENCY
        FOLLOW -> {}
        SEQUENCY -> '' | ARGUMENT SEQUENCY | SEQUENCY ARGUMENT | NAME_SEQUENCY SEQUENCY | SEQUENCE NAME_SEQUENCY
        NAME_SEQUENCY -> {}
        NAME_FUNCTION -> {} 
        ARGUMENT -> UNARY NAME_FUNCTION | NAME_FUNCTION | '(' ARGUMENT BINARY ARGUMENT ')' | SELECTOR
        UNARY -> {}
        BINARY -> {}
        SELECTOR -> QUANTOR VARIABLE NAME_FUNCTION
        QUANTOR -> '%forall' | '%exist'
        VARIABLE -> {}
        """
        rules = pattern.format(f"'{self.__follow}'", self.__create_list_variables(tuple(self.__default_sequency)),
                               self.__create_list_variables(self.__names_formulas),
                               self.__create_list_variables(self.__unary_operations),
                               self.__create_list_variables(self.__binary_operations),
                               self.__create_list_variables(self.__variables)
                               )
        self.__rules = rules

    @staticmethod
    def __create_list_variables(ls: Tuple[str]) -> str:
        return " | ".join([f"'{name}'" for name in ls])

    def __transform_operation(self, lexem: str) -> List[str]:
        all_operations: Tuple[str] = self.__unary_operations + self.__binary_operations + ('(', ')')
        for operator in all_operations:
            lexem = lexem.replace(operator, f' {operator} ')

        return lexem.split()

    @staticmethod
    def __replace_item_list(ls: List[str], old_value: str, new_value: str):
        while True:
            try:
                index = ls.index(old_value)
                ls[index] = new_value
            except ValueError:
                break

    def __create_pattern(self, lexems: List[str]) -> str:
        """
        Функция, которая создает для секвенции шаблон
        Шаблон понадобится в дальнейшем, для сравнения секвенций
        При сравнении двух секвенций, будем сравнивать шаблоны этих секвенций, чтобы убрать лишнее
        :param sequency:
        :return:
        """
        # Первым делом заменяем все имена формул на Fi, согласно порядку, в котором они встречаются в формуле
        index_formulas: Dict[str, int] = dict()
        for formula in self.__names_formulas:
            if formula in lexems:
                index_formulas[formula] = lexems.index(formula)
        index_variables: Dict[str, int] = dict()
        for variable in self.__variables:
            if variable in lexems:
                index_variables[variable] = lexems.index(variable)
        number: int = 1
        for key, value in sorted(index_formulas.items(), key=lambda item: item[1]):
            self.__replace_item_list(lexems, key, f'F{number}')
            number += 1
        number = 1
        for key, value in sorted(index_variables.items(), key=lambda item: item[1]):
            self.__replace_item_list(lexems, key, f'x{number}')
            number = number + 1
        pattern: str = ' '.join(lexems)
        return pattern
