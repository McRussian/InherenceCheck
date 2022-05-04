from unittest import TestCase

from inherence_check.parser import SequencyParser, SequencyParserException


class TestSequencyParser(TestCase):
    def test_parse(self):
        parser = SequencyParser()
        self.assertTrue(parser.parse('A ==> A'))
        self.assertFalse(parser.parse('A ==> AB'))

    def test_equal(self):
        parser = SequencyParser()
        self.assertTrue(parser.sequency_equal('A ==> A', 'B ==> B'))

