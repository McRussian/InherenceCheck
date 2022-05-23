from unittest import TestCase

from inherence_check.parser import FactorComparator, PatternComparator


class TestPatternComparator(TestCase):
    def test_compare_pattern(self):
        comparator: PatternComparator = FactorComparator['sequency']

        self.assertTrue(comparator.compare_pattern('G |- ( F1 ==> F2 )', '|- ( F1 ==> - - F1 )'))
        self.assertTrue(comparator.compare_pattern('G |- - F1', 'F1 |- - - F1'))
        self.assertTrue(comparator.compare_pattern('G |-', 'F1, -F1 |-'))
        self.assertTrue(comparator.compare_pattern('G F1 |- F2', 'F1 |- --F1'))

        self.assertFalse(comparator.compare_pattern('G |- ( F1 ==> F2 )', '|- ( F1 V --F1)'))
        self.assertFalse(comparator.compare_pattern('G |- ( F1 ==> F2 )', '|- F1 , --F1'))
