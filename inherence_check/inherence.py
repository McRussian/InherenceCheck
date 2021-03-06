from typing import List, Tuple

from inherence_lib import (
    Sequency, Sequencys, SequencyException,
    Rule, Rules, RuleException,
    Tree, TreeException,
    FactoryParser, SequencyParser, InherenceException)
from logger import Logger


class InherenceCheck:
    def __init__(self, logger: Logger,
                 formulas: Tuple[str], variables: Tuple[str],
                 sequencys: Tuple[str], rules: Tuple[str]):
        self.__logger = logger
        self.__init_factory_parsers(variables, formulas)

        try:
            self.__sequencys = Sequencys(sequencys)
            self.__rules = Rules(rules)
        except InherenceException as err:
            self.__logger.error(str(err))

    def __init_factory_parsers(self, variables: Tuple[str], formulas: Tuple[str]):
        try:
            FactoryParser['sequency'] = SequencyParser(formulas=formulas)
        except InherenceException as err:
            self.__logger.error(str(err))

    def check_inherence(self, tree: Tree) -> bool:
        for ls_rules in tree:
            for rule in ls_rules:
                print(rule)
                if rule not in self.__rules:
                    print(f'Rule {rule} not found')
                    raise InherenceException(f'Error of inherense: {ls_rules}')
