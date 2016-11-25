import time
import selenium
from selenium import webdriver


def trim_classes(class_name):
    return {
        'Reading':'Reading',
        'Homeroom':'Homeroom',
        'Written Comp':'Writing',
        'Social Studies':'Soc Stu',
        'Math':'Math',
        'Science':'Science',
        'PE/Gray':'PE',
        'Music/Gray':'Music',
        'Art/Gray':'Art'
        }[class_name]

def grades(br):
    text = "Luisa\n"

    grades = br.find_elements_by_id('average')
    subjects = br.find_elements_by_class_name('sg-5px-margin')
    l_grades = dict()

    ave_list = []
    for g in grades:
        test = g.text.strip()
        if not test:
            ave_list.append('none')
        else:
            ave_list.append(g.text)

    #in the first week, the grades are empty
    if not any(ave_list):
        early_text = "no grades for Luisa yet"
        return early_text
    
    subj_list = []       
    for s in subjects:
        subj_list.append(s.text.split("\n")[0])

    del subj_list[0]
    del subj_list[0]
    
    for i, (g, s) in enumerate(zip(ave_list, subj_list)):
        l_grades[s] = g
        
    for key, value in sorted(l_grades.items()):
        text += "{0} in {1}\n".format(value, trim_classes(key))

    return text
