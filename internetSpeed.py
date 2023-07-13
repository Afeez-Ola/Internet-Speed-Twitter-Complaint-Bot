from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


CHROME_DRIVER_PATH = r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class InternetSpeed:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        cookie_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]')
        cookie_button.click()
        start_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        start_button.click()
        time.sleep(20)
        down = self.driver.find_element(By.XPATH,
                                        '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
        time.sleep(20)
        up = self.driver.find_element(By.XPATH,
                                      '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
        return up, down
