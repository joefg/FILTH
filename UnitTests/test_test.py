from unittest import TestCase
import FILTH.Tests.test as ft


class TestTest(TestCase):

    def test___init__(self):
        test1 = ft.Test(1, 1)
        self.assertEqual(test1.expected_output, 1)
        self.assertEqual(test1.actual_output, 1)

    def test_run_test(self):
        # testing for booleans
        test1 = ft.Test(True, True) # True positive
        test2 = ft.Test(True, False) # False positive
        test3 = ft.Test(False, True) # False negative
        test4 = ft.Test(False, False) # True negative

        # Running tests
        self.assertEqual(test1.run_test(), ('T', 'T'))
        self.assertEqual(test2.run_test(), ('T', 'F'))
        self.assertEqual(test3.run_test(), ('F', 'T'))
        self.assertEqual(test4.run_test(), ('F', 'F'))
