from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from Credentials import Username, Password
from time import sleep
from selenium.webdriver.common.by import By

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
            sleep(1)
            i = 2
            try:
                sleep(1)
                bot.driver.switch_to.frame(0)
                bot.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[{0}]/td[7]/button'.format(i)).click()
                bot.completeEval()
                i += 1
            except:
                try:
                    sleep(1)
                    i += 1
                    bot.driver.find_element_by_xpath('/html/body/div[1]/table/tbody/tr[{0}]/td[7]/button'.format(i)).click()
                    bot.completeEval()
                    i+= 1
                except:
                    print("Completed!")
                    break

    def completeEval(self):
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".btnCerrarModal:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(1) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(2) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.ID, "btnNext").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(3) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(4) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(5) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(6) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(7) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(8) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(9) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(10) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.ID, "btnNext").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(11) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(12) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(13) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.ID, "btnNext").click()
        sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(14) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(15) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(16) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.CSS_SELECTOR, ".option-row:nth-child(17) > .option:nth-child(6) > .css-label").click()
        self.driver.find_element(By.ID, "btnNext").click()
        sleep(1)
        self.driver.find_element(By.ID, "Respuestas_17__OpcionValorText").click()
        self.driver.find_element(By.ID, "Respuestas_17__OpcionValorText").send_keys("Excelente Profesor!")
        self.driver.find_element(By.ID, "btnNext").click()
        sleep(1)
        #bot.login()

           

bot = Bot()
bot.login()
bot.profCheck()