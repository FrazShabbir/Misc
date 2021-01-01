from selenium import webdriver
from selenium.webdriver.common.keys import Keys                    #FORM ENABLEING KEY PRESSES
from time import sleep
from bs4 import BeautifulSoup
import requests

def gsearch():
    driver = webdriver.Chrome("/usr/local/share/chromedriver")
    
    what = input("Enter Job title:")
    where = input("Enter destination:")

    link="https://pk.indeed.com/jobs?q="+what+"&l="+where
    driver.get(link)
    next1=driver.find_element_by_css_selector("h2.title")
    next1.click()

    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')
    ass = soup.find('li').text
    # for tag in soup.find_all("div",{"id":"vjs-desc"}):
    #     print("{0}: {1}".format(tag.name, tag.text))
    headline = ass
    print(headline)
    sleep(4000)
    
    
gsearch()























    # fname=driver.find_element_by_xpath('//*[@id="text-input-what"]')
    # fname.send_keys(what)

    # fname=driver.find_element_by_xpath('//*[@id="text-input-where"]')
    # fname.send_keys(where)

    # next1=driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
    # next1.click()