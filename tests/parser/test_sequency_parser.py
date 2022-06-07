from unittest import TestCase

from inherence_check.inherence_lib.sequency_parser import SequencyParser, SequencyParserException


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
        self.assertTrue(parser.parse('|- (A => --A)'))
        self.assertTrue(parser.parse('G, %forall x A |- A'))
        self.assertTrue(parser.parse('G , %forall x A |-  A'))
        self.assertTrue(parser.parse('G, %exist x A |- A'))
        self.assertTrue(parser.parse('G , %exist x A |-  A'))

        self.assertFalse(parser.parse('A |- AB'))
        self.assertFalse(parser.parse('G , %%exist x A |-  A'))

    def test_transform_sequency(self):
        parser = SequencyParser()
        self.assertEqual(parser.transform_sequency('A |- A'), ['A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('A  |-   A'), ['A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('A|-A'), ['A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('G1, G2, G3 |- C'), ['G1', 'G2', 'G3', '|-', 'C'])
        self.assertEqual(parser.transform_sequency('G1 ,  G2,  G3 |- C'), ['G1', 'G2', 'G3', '|-', 'C'])
        self.assertEqual(parser.transform_sequency('G1,G2,G3 |- C'), ['G1', 'G2', 'G3', '|-', 'C'])
        self.assertEqual(parser.transform_sequency('G, %forall x A |- A'), ['G', '%forall', 'x', 'A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('G , %forall x A |-  A'), ['G', '%forall', 'x', 'A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('G, %exist x A |- A'), ['G', '%exist', 'x', 'A', '|-', 'A'])
        self.assertEqual(parser.transform_sequency('G , %exist x A |-  A'), ['G', '%exist', 'x', 'A', '|-', 'A'])

        self.assertEqual(parser.transform_sequency('G |-'), ['G', '|-'])
        self.assertEqual(parser.transform_sequency('G |- -A'), ['G', '|-', '-', 'A'])
        self.assertEqual(parser.transform_sequency('G1 |- (A V B)'), ['G1', '|-', '(', 'A', 'V', 'B', ')'])
        self.assertEqual(parser.transform_sequency('G1 |- (A => B)'), ['G1', '|-', '(', 'A', '=>', 'B', ')'])

    def test_create_pattern(self):
        parser = SequencyParser()
        sequency = "A |- A"
        parser.parse(sequency)
        self.assertEqual("F1 |- F1", parser.pattern(sequency))
        sequency = "G |-"
        parser.parse(sequency)
        self.assertEqual("G |-", parser.pattern(sequency))

        sequency = "G, B, A, G |- G, A, B, G"
        parser.parse(sequency)
        self.assertEqual("G F1 F2 G |- G F2 F1 G", parser.pattern(sequency))

        sequency = "G, %forall x A, %exist y C |- B, C"
        parser.parse(sequency)
        self.assertEqual("G %forall x1 F1 %exist x2 F2 |- F3 F2", parser.pattern(sequency))

        self.assertRaises(SequencyParserException, parser.pattern, "G |- B")

    def test_check_axioms(self):
        parser = SequencyParser()
        sequency = "A |- A"
        parser.parse(sequency)
        self.assertTrue(parser.is_axiom(sequency))
        sequency = "-A  |- -A"
        parser.parse(sequency)
        self.assertTrue(parser.is_axiom(sequency))
        sequency = "--A  |- --A"
        parser.parse(sequency)
        self.assertTrue(parser.is_axiom(sequency))

        sequency = "B  |- B"
        parser.parse(sequency)
        self.assertTrue(parser.is_axiom(sequency))

        sequency = "-B |- -B"
        parser.parse(sequency)
        self.assertTrue(parser.is_axiom(sequency))

        sequency = "B |- A"
        parser.parse(sequency)
        self.assertFalse(parser.is_axiom(sequency))

        self.assertRaises(SequencyParserException, parser.is_axiom, "G |- B")
