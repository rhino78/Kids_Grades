import time
import selenium
from selenium import webdriver

class grades():
	class_average = ""
	assignments = {}
	
	def __init__(self, name):
		self.name = name

def missing(br):
    table = br.find_element_by_class_name("sg-homeview-table")
    list_of_grades =[]
    for row in table.find_elements_by_tag_name("tr"):
        the_length = len(row.text.split("\n"))        
        if the_length > 4 and the_length < 17:
            n = grades(row.text.split("\n")[0])
            n.class_average = row.text.split("\n")[3]
            n.assignments = row.text.split("\n")[4:the_length]
            list_of_grades.append(n)

    prev = ""
    text = "Bella missing \n"

    for l in list_of_grades:
        for t in l.assignments:
                if t == "M" or t == "0/100":
                        text = text + "{1} in {0} \n".format(l.name, prev)
                        
                prev = t

    return text



