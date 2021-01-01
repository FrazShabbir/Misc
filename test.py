from selenium import webdriver
from selenium.webdriver.common.keys import Keys                    #FORM ENABLEING KEY PRESSES
from time import sleep
from bs4 import BeautifulSoup
import requests

def gsearch():
    driver = webdriver.Chrome("/usr/local/share/chromedriver")
    

    what = input("Enter Job title:")
    where = input("Enter destination:")
    # fname=driver.find_element_by_xpath('//*[@id="text-input-what"]')
    # fname.send_keys(what)

    # fname=driver.find_element_by_xpath('//*[@id="text-input-where"]')
    # fname.send_keys(where)

    # next1=driver.find_element_by_xpath('//*[@id="whatWhereFormId"]/div[3]/button')
    # next1.click()
    link="https://pk.indeed.com/jobs?q="+what+"&l="+where
    driver.get(link)
    source = requests.get(link).text
    soup = BeautifulSoup(source,'lxml')
    
    
    
gsearch()
