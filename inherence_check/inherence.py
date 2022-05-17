from typing import List

from inherence_check.inherence_lib import (
    Sequency, Sequencys, SequencyException,
    Rule, Rules, RuleException,
    Tree, TreeException
)
from inherence_check.parser import FactoryParser, SequencyParser

from inherence_check.logger import Logger


class InherenceCheck:
    def __init__(self, logger: Logger,
                 formulas: List[str], variables: List[str],
                 sequencys: List[str], rules: List[str]):
        self.__logger = logger
        self.__init_factory_parsers(variables, formulas)

        try:
            self.__sequencys = Sequencys(sequencys)
            self.__rules = Rules(rules)
        except InherenceCheck as err:
            self.__logger.error(str(err))

    def __init_factory_parsers(self, variables: List[str], formulas: List[str]):
        try:
            FactoryParser['sequency'] = SequencyParser(formulas=formulas)
        except InherenceCheck as err:
            self.__logger.error(str(err))

    def check_inherence(self, tree: Tree) -> bool:
        pass
