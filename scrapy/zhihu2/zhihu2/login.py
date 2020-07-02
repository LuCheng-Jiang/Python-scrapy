from selenium import webdriver
import time
import requests
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support.select import By
from selenium.webdriver.support import expected_conditions as EC
from chaojiying import Chaojiying_Client
class Login:


    def __init__(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.zhihu.com/signin?"

    def login(self):
        self.driver.get(self.url)
        self.driver.implicitly_wait(3)
        div_switch = self.driver.find_element_by_xpath("//div[@class='SignFlow-tab']")
        div_switch.click()
        username = self.driver.find_element_by_xpath("//input[@name='username']")
        username.send_keys("17670743808")
        time.sleep(3)

        password = self.driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys('wk19990223')

        time.sleep(3)
        button = self.driver.find_element_by_xpath("//button[@type='submit']")
        button.click()
        img_src  =self.driver.find_element_by_xpath("//div[@class='Captcha-englishContainer']/img").get_attribute("src")
        print(img_src)
        response = requests.get(img_src)
        print(response)
        with open("test.png","wb") as f:
            f.write(response)

        code = Chaojiying_Client.identify("test.png")
        print(code)

        captcha = self.driver.find_element_by_xpath("//input[@name='captcha']")
        captcha.send_keys(code)

        time.sleep(4)
        button = self.driver.find_element_by_xpath("//button[@type='submit']")
        time.sleep(4)
        button.click()
        time.sleep(10)
        self.driver.close()

    def main(self):
        self.login()


if __name__  ==  "__main__":
    login = Login()
    login.main()
