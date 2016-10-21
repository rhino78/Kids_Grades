import time
import selenium
from selenium import webdriver


def trim_classes(class_name):
    return {
        'Tx Hist & Geo':'Tx Hist',
        'Art MS 2':'Art',
        'Band: Intermediate MS 2':'Band',
        'Language Arts 7':'Lan Arts',
        'Math 7 Accel':'Math',
        'Science 7':'Science',
        'Girls Ath 7':'Athletics'
        }[class_name]

def grades(br):
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

    del b_grades['Lunch/Advisory']

    for key, value in sorted(b_grades.items()):
        text += "{0} in {1}\n".format(value, trim_classes(key))

    return text
