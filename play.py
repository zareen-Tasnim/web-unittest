from selenium import webdriver
import random
import requests
from selenium.webdriver.common.by import By
import time


BONGO_BD_VIDEO_ELEMENT_CLASSNAME = "MuiCardMedia-root"

class BongoWebRandomVideo():

    def __init__(self):
        self.URL_PATH = "https://bongobd.com/"
        self.DRIVER_PATH = "C:\\Program Files\\chromedriver.exe"
        self.driver = webdriver.Chrome()

        self.driver.get(self.URL_PATH)
        self.driver.maximize_window()
    
    def get_random_video(self, ):
        time.sleep(7)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        all_videos = self.driver.find_elements(By.CLASS_NAME,(BONGO_BD_VIDEO_ELEMENT_CLASSNAME))
        video = all_videos[random.randint(0, len(all_videos) - 1)]
        video.click()
        time.sleep(5)
        return video


    def get_current_url(self, ):
        return self.driver.current_url
    
    def exit(self):
        self.driver.quit()
        return True



bongo = BongoWebRandomVideo()
print(bongo.get_random_video())
print(bongo.get_current_url())
bongo.exit()




