from selenium import webdriver
from selenium.webdriver.common.keys import Keys                    #FORM ENABLEING KEY PRESSES
from time import sleep
#GmailAccount creator Script          Half
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--incognito")
# driver = webdriver.Chrome(chrome_options=chrome_options) 
# 

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





# lname=driver.find_element_by_xpath('//*[@id="lastName"]')
# lname.send_keys("shabbir")
# sleep(3)
# pass1=driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
# #passwordforuser=fname+lname
# pass1.send_keys("passwordforuser")
# pass2=driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
# pass2.send_keys("passwordforuser")

# next1=driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/span/span')
# next1.click()