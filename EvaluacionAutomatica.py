from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from Credentials import Username, Password, UltimoAnoCursado, UltimoMesCursado
from time import sleep

class Bot():
    def __init__(self):
        #self.chrome_options = Options()
        #self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome()#options=self.chrome_options

bot = Bot()