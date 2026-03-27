import unittest

from .ConverterTests import ConverterTestCase


def run_suite():
    suite = unittest.TestSuite()
    suite.addTest(ConverterTestCase('test_convert'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(run_suite())
