from unittest import TestCase

from inherence_check.parser import SequencyParser, SequencyParserException


class TestSequencyParser(TestCase):
    def test_parse(self):
        parser = SequencyParser()
        self.assertTrue(parser.parse('A |- A'))
        self.assertTrue(parser.parse('G, A |-'))
        self.assertTrue(parser.parse('G |- (A & B)'))
        self.assertTrue(parser.parse('G |- -A'))
        self.assertTrue(parser.parse('G1 |- (A V B)'))
        self.assertTrue(parser.parse('G1, G2, G3 |- C'))
        self.assertTrue(parser.parse('G |- (A => B)'))
        self.assertFalse(parser.parse('A |- AB'))

    def test_transform_sequency(self):
        parser = SequencyParser()
        self.assertEqual(parser.transform_sequency('A |- A'), ['A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('A  |-   A'), ['A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('A|-A'), ['A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('G1, G2, G3 |- C'), ['G1', 'G2', 'G3', '|-', 'C'])
        self.assertEqual(parser.transform_sequency('G1 ,  G2,  G3 |- C'), ['G1', 'G2', 'G3', '|-', 'C'])
        self.assertEqual(parser.transform_sequency('G1,G2,G3 |- C'), ['G1', 'G2', 'G3', '|-', 'C'])

        self.assertEqual(parser.transform_sequency('G |- -A'), ['G', '|-', '-', 'A'])
        self.assertEqual(parser.transform_sequency('G1 |- (A V B)'), ['G1', '|-', '(', 'A', 'V', 'B', ')'])
        self.assertEqual(parser.transform_sequency('G1 |- (A => B)'), ['G1', '|-', '(', 'A', '=>', 'B', ')'])
