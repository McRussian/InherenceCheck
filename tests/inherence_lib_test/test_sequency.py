from unittest import TestCase

from inherence_check.inherence_lib import Sequency, SequencyException


class TestSequency(TestCase):
    def test_create_sequency(self):
        self.assertRaises(SequencyException, Sequency, 'left => right')

    def test_equals(self):
        seq1 = Sequency('G, A |- B')
        seq2 = Sequency('A |- --A')
        print(seq1.pattern)
        print(seq2.pattern)
        self.assertEqual(seq1, seq2)
