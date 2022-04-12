from unittest import TestCase

from inherence_check.inherence_lib import Axiom, AxiomException


class TestAxiom(TestCase):
    def test_create_axiom(self):
        self.assertRaises(AxiomException, Axiom, "fgfcfdsg cbjhdfbd")
        self.assertRaises(AxiomException, Axiom, '{f} === {g}')

    def test_equal_axiom(self):
        axiom_a = Axiom('{f} === {f}')
        axiom_b = Axiom('{f} === {f}')
        self.assertEqual(axiom_b, axiom_b)

        axiom_c = Axiom('{g} === {g}')
        self.assertNotEqual(axiom_a, axiom_c)
        self.assertNotEqual(axiom_b, axiom_c)
