from unittest import TestCase
from random import choice
from typing import List

from tests.lib import random_string

from inherence_check.inherence_lib import Variable, Variables, VariableException, ALL_LEXEMES


class TestVariables(TestCase):
    def test_create_variable(self):
        self.assertRaises(VariableException, Variable, '')

        for _ in range(10):
            lexem = choice(ALL_LEXEMES)
            self.assertRaises(VariableException, Variable, lexem)

    def test_equals_variable(self):
        for _ in range(10):
            name = random_string(4)
            var_a = Variable(name)
            var_b = Variable(name)
            self.assertEqual(var_b, var_a)
            self.assertEqual(var_a, var_b)
            var_c = Variable(name + '_')
            self.assertNotEqual(var_a, var_c)
            self.assertNotEqual(var_b, var_c)

    def test_create_variables(self):
        self.assertRaises(VariableException, Variables, [])
        self.assertRaises(VariableException, Variables, ALL_LEXEMES)

    def test_contains_variables(self):
        ls: List[str] = [random_string(4) for _ in range(10)]
        variables = Variables(ls)
        for name in ls:
            self.assertTrue(name in variables)
            self.assertFalse(name + '_' in variables)

        for _ in range(20):
            name = random_string(4)
            self.assertFalse(name in variables)
