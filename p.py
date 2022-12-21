from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time

options = webdriver.FirefoxOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')
driver = webdriver.Firefox()
driver.get('https://www.youtube.com/')
time.sleep(3)
button = driver.find_element('xpath', '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a/yt-touch-feedback-shape/div/div[2]')
button.click()
time.sleep(3)
login = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input'
driver.find_element('xpath', login).send_keys('popuvaychic@gmail.com')
time.sleep(3)
next = '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span'
n_button = driver.find_element('xpath', '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[2]/div/div[1]/div/div/button/span')
n_button.click()
time.sleep(5)
