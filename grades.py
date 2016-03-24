import smtplib
import time
import selenium
from selenium import webdriver
from time import gmtime, strftime, localtime
import creds

def trim_classes(class_name):
    return {
        'World Cultures':'World Cultures',
        'Art MS 1':'Art',
        'Beg. Band: Flute':'Band',
        'Language Arts 6':'Language',
        'Math 6 Accel':'Math',
        'Science 6':'Science',
        'Wellness Ed 6':'Wellness'
        }[class_name]

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

text = "Bella\n"
change = br.find_elements_by_tag_name('button')
for s in change:
    if s.text == "Change Student":
        s.click()

time.sleep(1)
radio = br.find_element_by_name("studentId")
radio.click()
change = br.find_elements_by_tag_name('button')
for s in change:
    if s.text == "Submit":
        s.click()

grades = br.find_elements_by_id('average')
subjects = br.find_elements_by_id('courseName')
b_grades = dict()

for i, (g, s) in enumerate(zip(grades, subjects)):
    b_grades[s.text] = g.text

del b_grades['Advisory/Lunch']

for key, value in sorted(b_grades.items()):
        text += "{0} in {1}\n".format(value, trim_classes(key))

br.close()

server.sendmail(fromaddr, toaddr, text)
print(text)
