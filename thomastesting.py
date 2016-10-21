import time
import selenium
from selenium import webdriver
import time
from time import gmtime, strftime, localtime
import creds


br = webdriver.Firefox()
url = 'https://accesscenter.roundrockisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fhomeaccess%2f'
br.get(url)
time.sleep(5)
print('logging in')
Username = br.find_element_by_id('LogOnDetails_UserName')
Username.send_keys(creds.LOGIN)
password = br.find_element_by_id('LogOnDetails_Password')
password.send_keys(creds.LOGINPW)
search = br.find_element_by_tag_name('button')
search.click()
print('logged in')
change = br.find_elements_by_tag_name('button')

for s in change:
    if s.text == "Change Student":
        s.click()
print('change student clicked, looking through radio buttons')
time.sleep(1)
#need to click the 3rd button here
#radio = br.find_element_by_name("studentId")
radio = br.find_elements_by_name("studentId")
print(br.find_elements_by_name("studentId")[1])
print(br.find_elements_by_name("studentId")[2])
