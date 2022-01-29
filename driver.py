from io import StringIO
from tabulate import tabulate
import csv
import numpy
import pandas
import pandas as pd
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser




###OPEN THE RESUME
output_string = StringIO()

newVar = int(input("Which resume do you want to use? (1, 2, 3):   "))

if newVar ==1:
    name = "John"
    with open('29051656.pdf', "rb") as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
elif newVar == 2:
    name = "Krishna"
    with open('Krishna_Reddy_E.pdf', "rb") as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)
elif newVar == 3:
    name = "Lisa"
    with open('Lisa Shrestha Minimal.pdf', "rb") as in_file:
        parser = PDFParser(in_file)
        doc = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(doc):
            interpreter.process_page(page)

"""""""""
with open('29051656.pdf', "rb") as in_file:
    parser = PDFParser(in_file)
    doc = PDFDocument(parser)
    rsrcmgr = PDFResourceManager()
    device = TextConverter(rsrcmgr, output_string, laparams=LAParams())
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.create_pages(doc):
        interpreter.process_page(page)
"""
resume_text=output_string

####OPEN THE FILE WITH THE KEYWORDS
file = open("skill_keywords.csv", "r")
csv_reader = csv.reader(file)

list_of_keywords = [word for line in file for word in line.split()]

###OPEN THE FILE WITH JOBS AND THEIR DESCRIPTIONS
###SET THEM UP IN AN ARRAY

dict_from_csv = pd.read_csv('job_skills - job_skills.csv')
myarr = dict_from_csv.to_numpy()
print(myarr[0][0])



class job:   #CREATE A JOB CLASS WITH VARIABLES NEEDED FOR CLASS
    def __init__(self):
        self.skill = []
        self.percentage_match = 0.0
        self.company = ""
        self.title = ""
        self.qual = ""

    def set_skill(self, myskill):
        self.skill = myskill

    def set_percentage(self, percentage):
        self.percentage_match = percentage

    def set_company(self, mycompany):
        self.company = mycompany

    def set_title(self, mytitle):
        self.title = mytitle

    def set_qual(self, myqual):
        self.qual = myqual

    def get_qual(self):
        return self.qual

joblist = []

for i in range(len(myarr)):
    newjob = job()
    newjob.set_company(myarr[i][0])
    newjob.set_title(myarr[i][1])
    newjob.set_qual(myarr[i][2])
    joblist.append(newjob)

jobqualsplit = []

for i in range(len(joblist)):
    jobqualsplit = str(joblist[i].get_qual()).split()
    new_job_qual = [x for x in jobqualsplit if x in list_of_keywords]
    joblist[i].set_skill(new_job_qual)

new_resume_list = []

new_resume_text = str(resume_text.getvalue())
resume_text_array = new_resume_text.split(" ")

new_resume_list = [x for x in resume_text_array if x in list_of_keywords]


i=0
j=0
counter=0
k=0
calc = 0




for i in range(len(joblist)):
    words_rem = [x for x in new_resume_list if x in joblist[i].skill]
    if (len(joblist[i].skill) != 0):
        calc = (len(words_rem)/len(joblist[i].skill)) * 100
        if calc > 100:
            calc = 100
        joblist[i].set_percentage(calc)

joblist.sort(key=lambda x: x.percentage_match, reverse=True)

print("Results for", name)
table = [['Company', 'Title', 'Percentage']]

p = 0

while p <len(joblist):
    if 101 > joblist[p].percentage_match and joblist[p].title != joblist[p - 1].title and int(joblist[p].percentage_match) != 0:
        table.append([joblist[p].company, joblist[p].title, int(joblist[p].percentage_match)])
    p += 1

print(tabulate(table))