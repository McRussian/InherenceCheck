import logging
from argparse import ArgumentParser
from typing import List, Optional

from inherence_check.inherence_exception import InherenceException
from inherence_check.inherence import InherenceCheck
from inherence_check.logger import Logger


logger = Logger('log.txt')


def read_items_from_file(filename: str) -> List[str]:
    items: List[str]
    with open(filename) as fin:
        items = fin.readlines()

    return items


def initialize(fname_variables: str, fname_formulas: str, fname_sequencys: str, fname_rules: str) -> InherenceCheck:
    try:
        variables: List[str] = read_items_from_file(fname_variables)
    except FileNotFoundError:
        raise ValueError(f"File {fname_variables} not found")
    try:
        formulas: List[str] = read_items_from_file(fname_formulas)
    except FileNotFoundError:
        raise ValueError(f"File {fname_variables} not found")
    try:
        sequencys: List[str] = read_items_from_file(fname_sequencys)
    except FileNotFoundError:
        raise ValueError(f"File {fname_sequencys} not found")
    try:
        rules: List[str] = read_items_from_file(fname_rules)
    except FileNotFoundError:
        raise ValueError(f"File {fname_rules} not found")

    return InherenceCheck(logger=logger, formulas=formulas, rules=rules,
                          variables=variables, sequencys=sequencys)


def running_check(checker: InherenceCheck):
    while True:
        filename = input('Enter Filename with Inherence Tree: ')
        try:
            tree: List[str] = read_items_from_file(filename)
        except Exception as err:
            logger.error(err)

        try:
            checker.check_inherence(tree)
        except InherenceException as err:
            logger.error(err)


if __name__ == '__main__':
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--variable', '-v',
                            dest='variable', default='data/variable',
                            help='Enter filename with list name of variables')
    arg_parser.add_argument('--formula', '-f',
                            dest='formula', default='data/formula',
                            help='Enter filename with list name of formulas')
    arg_parser.add_argument('--sequency', '-s',
                            dest='sequency', default='data/sequency',
                            help='Enter filename with list of sequencys')
    arg_parser.add_argument('--rule', '-r',
                            dest='rule', default='data/rule',
                            help='Enter filename with list of rules')
    args = arg_parser.parse_args()
    checker: Optional[InherenceCheck] = None
    try:
         checker = initialize(fname_variables=args.variable, fname_formulas=args.formula,
                                             fname_rules=args.rule, fname_sequencys=args.sequency)
    except ValueError as err:
        logger.error(str(err))

    if checker is not None:
        running_check(checker)
    