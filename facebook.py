from selenium import webdriver
from selenium.webdriver.common.keys import Keys                    #FORM ENABLEING KEY PRESSES
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains 

# Chrome drivers
driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

#CODE FOR INCOGNITO MODE
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)
#ACTUAL OPENING LINK
e=driver.get('https://web.whatsapp.com/')
email=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
email.send_keys('fraz.shabbir54@gmail.com')
#pass1=driver.find_element_by_xpath('//*[@id="pass"]')
#pass1.send_keys('----')
#submit=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div[1]/div/div/div[2]/div[1]/div[1]')
email.send_keys(Keys.ENTER)
#driver.close()
