from internetSpeed import InternetSpeed
from twitterbot import TwitterBot

PROMISED_DOWNLOAD = 100
PROMISED_UPLOAD = 10

down_speed = InternetSpeed().get_internet_speed()[1].text
up_speed = InternetSpeed().get_internet_speed()[0].text
TWEET_MESSAGE = f'Hi @UPC_Polska my internet speed is {down_speed}down/{up_speed}up instead of {PROMISED_DOWNLOAD}down/{PROMISED_UPLOAD}up'
TwitterBot().tweet_at_provider(TWEET_MESSAGE)