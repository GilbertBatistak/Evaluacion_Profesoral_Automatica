from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from Credentials import Username, Password
from time import sleep

class Bot():
    def __init__(self):
        #self.chrome_options = Options()
        #self.chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome()#options=self.chrome_options

        
    def login(self):
        self.driver.get("https://procesos.intec.edu.do")
        #sleep(0.7)
        IdPath = bot.driver.find_element_by_xpath('//*[@id="txtID"]')
        IdPath.send_keys(Username)
        PassPath = bot.driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/form/div[2]/input')
        PassPath.send_keys(Password)        
        login_btn = bot.driver.find_element_by_xpath('//*[@id="btnEntrar"]').click()
        #sleep(1)
        x_close = bot.driver.find_element_by_xpath('//*[@id="AvisoEvaluacion"]/div/a').click()
        prof_Eval = bot.driver.find_element_by_xpath('//*[@id="opEvaluacion"]').click()
    
    def profCheck(self):
        while 1:
            i = 0
            try:
                profC = bot.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[{0}]/td[7]/button'.format(i)).click()
            except:
                print("Completed")

bot = Bot()
bot.login()