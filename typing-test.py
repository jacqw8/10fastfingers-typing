# 10fastfingers-typing
import time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

PATH = "/Users/alliewu/Desktop/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://10fastfingers.com/typing-test/english")

time.sleep(3)
res = driver.execute_script('return document.documentElement.outerHTML') #executes Javascript
soup = BeautifulSoup(res, 'lxml') #html of website after Javascript run

wordlist = soup.find('div', {'id': 'wordlist'}).text
# print(wordlist.split('|'))

txt = wordlist

txt = txt.split('|')
type = driver.find_element_by_id('inputfield')
endTime = datetime.datetime.now() + datetime.timedelta(minutes=1)
while True:
    for t in txt:
        type.send_keys(t)
        time.sleep(0.2) #can change this for faster results
        type.send_keys(' ')
        if datetime.datetime.now() >= endTime:
            break
    if datetime.datetime.now() >= endTime:
        break


