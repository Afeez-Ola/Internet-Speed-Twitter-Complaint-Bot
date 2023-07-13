from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


CHROME_DRIVER_PATH = r"C:\Users\user\Downloads\chromedriver_win32\chromedriver.exe"
TWITTER_EMAIL = "yourtwitteremail"
TWITTER_PASSWORD = "yourtwitterpassword"
TWITTER_NUMBER = "your_twitter_number"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


class TwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=chrome_options)

    def tweet_at_provider(self, tweet_message):
        self.driver.get('https://twitter.com/login?username_disabled=false&redirect_after_login=%2F')
        time.sleep(5)
        email_field = self.driver.find_element(By.NAME, "text")
        next_button = self.driver.find_element(By.XPATH,
                                               '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
        email_field.send_keys(TWITTER_EMAIL)
        next_button.click()
        time.sleep(2)
        captcha = self.driver.find_element(By.XPATH,
                                           '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        captcha.send_keys(TWITTER_NUMBER)
        next2_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div')
        next2_button.click()
        time.sleep(2)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(TWITTER_PASSWORD)
        login_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
        login_button.click()
        TWEET_MESSAGE = tweet_message
        time.sleep(5)
        accept_button = self.driver.find_element(By.XPATH,
                                                 '//*[@id="layers"]/div/div/div/div/div/div[2]/div[1]/div/span/span')
        accept_button.click()
        time.sleep(2)
        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')
        tweet_button.click()
        tweet_input = self.driver.find_element(By.CSS_SELECTOR,
                                               '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1habvwh.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-rsyp9y.r-1pjcn9w.r-htvplk.r-1udh08x.r-1potc6q > div > div > div > div:nth-child(3) > div.css-1dbjc4n.r-14lw9ot.r-1pp923h.r-1moyyf3.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-1dbjc4n.r-18u37iz.r-184en5c > div.css-1dbjc4n.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div > div > div > div > div > div > div.css-1dbjc4n.r-16y2uox.r-bnwqim.r-13qz1uu.r-1g40b8q > div > div > div > div > label > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2 > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div > span > br')
        # tweet_input.click()
        tweet_input.send_keys(f"{TWEET_MESSAGE}\nThis is from my bot tho :)")
        # time.sleep(5)
        tweet_button = self.driver.find_element(By.XPATH,
                                                '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[4]/div/span/span')
        tweet_button.click()
