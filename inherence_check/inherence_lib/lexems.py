from typing import List


LOGICAL_OPERATORS: List[str] = [
    'and',
    'not',
    'or',
]

LOGICAL_RELATIONS: List[str] = [
    '===',
    '->',
    '<-',
]

BRACKETS: List[str] = [
    '(',
    ')',
    '[',
    ']',
    '\|',
]

KEY_WORDS: List[str] = [
    'forall',
    'exist',
]

SPECIAL_SYMBOLS: List[str] = [
    '_',
    '^',
    '{',
    '}',
    '\\',
]

GROUP_FORMULAS: List[str] = [
    'G',
    'SG',
    'GG',
]

ALL_LEXEMES = [*LOGICAL_OPERATORS, *LOGICAL_RELATIONS, *BRACKETS, *KEY_WORDS, *SPECIAL_SYMBOLS, *GROUP_FORMULAS]
