#unittest to go to bongo website
import unittest
import HtmlTestRunner
from play import BongoWebRandomVideo



class TestBongoWebRandomVideo(unittest.TestCase):

    def setUp(self):
        self.bongo = BongoWebRandomVideo()

    def test_url(self, ):
        self.assertTrue(self.bongo.get_current_url)

    def tearDown(self):
        self.assertEqual(self.bongo.exit(), True)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/BONGO_TEST/reports"))