from selenium import webdriver
from selenium.webdriver.common.keys import Keys                    #FORM ENABLEING KEY PRESSES
from time import sleep
#GmailAccount creator Script          Half
#driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

driver = webdriver.Chrome("/usr/local/share/chromedriver")
#driver.get("https://google.com")
#searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
#searchbox.send_keys("facebook")
#searchbutton=driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[3]/center/input[1]')
#searchbutton.click()
#searchbutton.send_keys(Keys.ENTER)    #using ENTER key of
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get('https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')
fname=driver.find_element_by_xpath('//*[@id="firstName"]')
fname.send_keys("fraz")
lname=driver.find_element_by_xpath('//*[@id="lastName"]')
lname.send_keys("shabbir")
sleep(3)
pass1=driver.find_element_by_xpath('//*[@id="passwd"]/div[1]/div/div[1]/input')
#passwordforuser=fname+lname
pass1.send_keys("passwordforuser")
pass2=driver.find_element_by_xpath('//*[@id="confirm-passwd"]/div[1]/div/div[1]/input')
pass2.send_keys("passwordforuser")

next1=driver.find_element_by_xpath('//*[@id="accountDetailsNext"]/span/span')
next1.click()