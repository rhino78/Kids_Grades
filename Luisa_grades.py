import time
import selenium
from selenium import webdriver


def trim_classes(class_name):
    return {
        'Reading':'Reading',
        'Homeroom':'Homeroom',
        'Written Comp':'Writing',
        'Social Studies':'Social Studies',
        'Math':'Math',
        'Science':'Science',
        'PE/Gray':'PE',
        'Music/Gray':'Music',
        'Art/Gray':'Art'
        }[class_name]

def grades(br):
    text = "Luisa\n"

    grades = br.find_elements_by_id('average')
    subjects = br.find_elements_by_id('courseName')
    b_grades = dict()

    for i, (g, s) in enumerate(zip(grades, subjects)):
        b_grades[s.text] = g.text

    for key, value in sorted(b_grades.items()):
        text += "{0} in {1}\n".format(value, trim_classes(key))

    return text
