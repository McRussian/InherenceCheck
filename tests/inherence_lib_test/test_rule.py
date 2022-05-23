from unittest import TestCase

from inherence_check.inherence_lib import Rule


class TestRule(TestCase):
    def test_equal_rules(self):
        rule1 = Rule(left='G, A |- B', right='G |- (A => B)')
        rule2 = Rule(left='A |- --A', right='|- (A => --A)')
        self.assertEqual(rule2, rule1)
