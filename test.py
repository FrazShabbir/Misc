from selenium import webdriver
from selenium.webdriver.common.keys import Keys                    #FORM ENABLEING KEY PRESSES
from time import sleep

def gsearch():
    driver = webdriver.Chrome("/usr/local/share/chromedriver")
    driver.get('https://www.google.com/')
    sleep(2)
    fname=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
    fname.send_keys("Hazrat Muhammad SAW")
    sleep(1)
    next1=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
    next1.click()
    driver.quit()

for x in range(1100):  
    gsearch() 
