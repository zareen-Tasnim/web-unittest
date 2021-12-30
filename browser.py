from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By


class BongoWeb():

    def __init__(self):
        self.URL_PATH = "https://bongobd.com/"
        self.DRIVER_PATH = "C:\\Program Files\\chromedriver.exe"
        self.driver = webdriver.Chrome()

        self.driver.get(self.URL_PATH)
        self.driver.maximize_window()
    
    def get_title(self, ):
        time.sleep(2)
        return self.driver.title
    
    def get_categories(self):
        all_categories_classes = self.driver.find_elements(By.CLASS_NAME, """MuiListItemText-root""")
        return [category.text for category in all_categories_classes]
    
    def exit(self):
        self.driver.quit()
        return True



bongo = BongoWeb()
print(bongo.get_title())
print(bongo.get_categories())
bongo.exit()




