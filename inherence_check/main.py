from pathlib import Path
from argparse import ArgumentParser
from typing import List, Optional, Tuple

from inherence_lib import Tree, InherenceException
from inherence import InherenceCheck
from logger import Logger


logger = Logger('log.txt')


def read_items_from_file(filename: Path) -> Tuple[str]:
    items: Tuple[str]
    with open(filename) as fin:
        items = tuple(map(lambda s: s.strip('\n'), fin.readlines()))

    return items


def initialize(fname_variables: Path, fname_formulas: Path,
               fname_sequencys: Path, fname_rules: Path) -> InherenceCheck:
    try:
        variables: Tuple[str] = read_items_from_file(fname_variables)
    except FileNotFoundError:
        raise ValueError(f"File {fname_variables} not found")
    try:
        formulas: Tuple[str] = read_items_from_file(fname_formulas)
    except FileNotFoundError:
        raise ValueError(f"File {fname_variables} not found")
    try:
        sequencys: Tuple[str] = read_items_from_file(fname_sequencys)
    except FileNotFoundError:
        raise ValueError(f"File {fname_sequencys} not found")
    try:
        rules: Tuple[str] = read_items_from_file(fname_rules)
    except FileNotFoundError:
        raise ValueError(f"File {fname_rules} not found")

    return InherenceCheck(logger=logger, formulas=formulas, rules=rules,
                          variables=variables, sequencys=sequencys)


def running_check(checker: InherenceCheck):
    data: Path = Path.cwd().parent / 'data'
    while True:
        filename = input('Enter Filename with Inherence Tree: ')
        if filename == 'exit' or filename == 'quit':
            break
        tree: Tuple[str] = list()
        try:
            tree = read_items_from_file(data / filename)
        except Exception as err:
            logger.error(err)

        try:
            checker.check_inherence(Tree(tree))
            print(f"Tree in filename {filename} - It is correct inherence...")
        except Exception as err:
            logger.error(err)
            print(err)



if __name__ == '__main__':
    data: Path = Path.cwd().parent / 'data'
    arg_parser = ArgumentParser()
    arg_parser.add_argument('--variable', '-v',
                            dest='variable', default='variable',
                            help='Enter filename with list name of variables')
    arg_parser.add_argument('--formula', '-f',
                            dest='formula', default='formula',
                            help='Enter filename with list name of formulas')
    arg_parser.add_argument('--sequency', '-s',
                            dest='sequency', default='sequency',
                            help='Enter filename with list of sequencys')
    arg_parser.add_argument('--rule', '-r',
                            dest='rule', default='rule',
                            help='Enter filename with list of rules')
    args = arg_parser.parse_args()
    checker: Optional[InherenceCheck] = None
    try:
         checker = initialize(fname_variables=data / args.variable, fname_formulas=data / args.formula,
                                             fname_rules=data / args.rule, fname_sequencys=data / args.sequency)
    except ValueError as err:
        logger.error(str(err))

    if checker is not None:
        running_check(checker)
    