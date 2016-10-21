import time
import selenium
from selenium import webdriver


def trim_classes(class_name):
    return {
        'Homeroom':'Tx Hist',
        'Reading':'Art',
        'Writtn Comp':'Band',
        'Social Studies':'Lan Arts',
        'Math':'Math',
        'Science':'Science',
        'PE Kimsey':'PE',
        'Music/Kimsey':'Music',
        'Art/Kimsey':'Art'
        }[class_name]

def grades(br):
    text = "Thomas\n"
    change = br.find_elements_by_tag_name('button')
    
    for s in change:
        if s.text == "Change Student":
            s.click()

    time.sleep(1)
    #need to click the 3rd button here
    #radio = br.find_element_by_name("studentId")
    radio = br.find_elements_by_name("studentId")[3]
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

    for key, value in sorted(b_grades.items()):
        text += "{0} in {1}\n".format(value, trim_classes(key))

    return text
