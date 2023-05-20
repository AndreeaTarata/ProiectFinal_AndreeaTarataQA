import unittest

import HtmlTestRunner

from home_page_tests import TestArtelierHomePage
from rezervare_tests import TestArtelierRezervare


class MyTestSuites(unittest.TestCase):

    # se ruleaza testele si se vor crea rapoarte
    def test_suite(self):
        smoketest = unittest.TestSuite()

        smoketest.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestArtelierHomePage),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestArtelierRezervare),
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            report_title='Reportexamen', report_name='smokeTest', combine_reports=True
        )
        runner.run(smoketest)
