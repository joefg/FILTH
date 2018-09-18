from unittest import TestCase
import FILTH.Harness.harness as fh
import FILTH.Tests.test as ft

class TestHarness(TestCase):

    def setUp(self):
        self.test_harness = fh.Harness()
        self.tests  = [
            ft.Test(1, 1),
            ft.Test(1, 0),
            ft.Test(0, 1),
            ft.Test(0, 0),
        ]
        for t in self.tests: self.test_harness.add_test(t)

    def test___init__(self):
        # testing the construction of an empty harness
        test1 = fh.Harness()
        self.assertEqual(test1.true_positives, 0)
        self.assertEqual(test1.true_negatives, 0)
        self.assertEqual(test1.false_positives, 0)
        self.assertEqual(test1.false_negatives, 0)

    def test_add_test(self):
        # testing the addition of a valid test to an empty harness
        test_harness1 = fh.Harness()
        test_test1 = ft.Test(1, 1)

        test_harness1.add_test(test_test1) # len(test_harness1) should = 1

        self.assertEqual(len(test_harness1.test_suite), 1)

    def test_run_tests(self):
        self.assertEqual(self.test_harness.run_tests(), (1, 1, 1, 1))

    def test_calculate_precision(self):
        self.test_harness.run_tests()
        self.assertEqual(self.test_harness.calculate_precision(), 0.5)

    def test_calculate_recall(self):
        self.test_harness.run_tests()
        self.assertEqual(self.test_harness.calculate_recall(), 0.5)

    def test_calculate_accuracy(self):
        self.test_harness.run_tests()
        self.assertEqual(self.test_harness.calculate_accuracy(), 0.5)

    def test_calculate_specificity(self):
        self.test_harness.run_tests()
        self.assertEqual(self.test_harness.calculate_specificity(), 0.5)
