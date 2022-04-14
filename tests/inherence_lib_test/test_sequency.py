from unittest import TestCase

from inherence_check.inherence_lib import Sequency, SequencyException


class TestSequency(TestCase):
    def test_create_sequency(self):
        self.assertRaises(SequencyException, Sequency, 'left => right')

