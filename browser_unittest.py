#unittest to go to bongo website
import unittest
import HtmlTestRunner
from browser import BongoWeb


MAIN_CATEGORIES = [
    'MOVIES', 'SHOWS','DRAMA','TV', 
    'MUSIC','SPORTS','BOOM', 'KIDS', 
    
]

class TestBongoWeb(unittest.TestCase):

    def setUp(self):
        self.bongo = BongoWeb()

    def test_title(self, ):
        self.assertEqual("BONGO | Watch Live Tv, Bangla Movies, Natoks Anytime Anywhere",self.bongo.get_title(), msg = "Title doesn't match")

        
    def test_main_categories(self, ):
        """
        Assuming MOVIES, SHOWS and DRAMA are main categories
        """
        bongo_categories = self.bongo.get_categories()

        for category in MAIN_CATEGORIES:
            self.assertEqual(category in bongo_categories, True, "Not Matched")

    def tearDown(self):
        self.assertEqual(self.bongo.exit(), True)

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="D:/BONGO_TEST/reports"))