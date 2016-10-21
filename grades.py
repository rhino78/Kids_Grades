import smtplib
import time
import selenium
from selenium import webdriver
from time import gmtime, strftime, localtime
import creds
import Bella_grades
import Luisa_grades
import Thomas_grades



username = creds.USERNAME
password = creds.PASSWORD
fromaddr = creds.FROMADDR
toaddr = creds.TOADDR
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username, password)

br = webdriver.Firefox()
url = 'https://accesscenter.roundrockisd.org/HomeAccess/Account/LogOn?ReturnUrl=%2fhomeaccess%2f'
br.get(url)
time.sleep(5)

Username = br.find_element_by_id('LogOnDetails_UserName')
Username.send_keys(creds.LOGIN)
password = br.find_element_by_id('LogOnDetails_Password')
password.send_keys(creds.LOGINPW)
search = br.find_element_by_tag_name('button')
search.click()

luisa = Luisa_grades.grades(br)
#server.sendmail(fromaddr, toaddr, luisa)
bella = Bella_grades.grades(br)
#server.sendmail(fromaddr, toaddr, bella)
thomas = Thomas_grades.grades(br)
#server.sendmail(fromaddr, toaddr, thomas)
br.close()


print(bella)
print(luisa)
print(thomas)
