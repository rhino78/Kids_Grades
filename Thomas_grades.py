import time
import selenium
from selenium import webdriver

def trim_classes(class_name):
    return {
        'Homeroom':'HR',
        'Reading':'Reading',
        'Written Comp':'Writing',
        'Social Studies':'Soc Studies',
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
    radio = br.find_elements_by_name("studentId")[2]
    radio.click()
    change = br.find_elements_by_tag_name('button')
    
    for s in change:
        if s.text == "Submit":
            s.click()

    grades = br.find_elements_by_id('average')
    subjects = br.find_elements_by_class_name('sg-font-larger')    
        
    t_grades = dict()

    ave_list = []
    for g in grades:
        test = g.text.strip()
        if not test:
            ave_list.append('none')
        else:
            ave_list.append(g.text)

    #in the first week, the grades are empty
    if not any(ave_list):
        early_text = "no grades for Thomas yet"
        return early_text
    
    subj_list = []       
    for s in subjects:
        subj_list.append(s.text.split("\n")[0])

    
    del subj_list[0]
    
    for i, (g, s) in enumerate(zip(ave_list, subj_list)):
        t_grades[s] = g
        
    for key, value in sorted(t_grades.items()):    
        text += "{0} in {1}\n".format(value, trim_classes(key))

    return text
