#!python3
import docx
import json
import sys
'''
Format to run file: python readDocFile.py useFul.docx
useFul.docx serve as filename
'''
fileName = "%s" % sys.argv[1]
doc = docx.Document(fileName)

newArr = []

json_li = []

#fields in the sample file
fields = ['Questions', 'OptionA', 'OptionB', 'OptionC', 'OptionD']

for para in doc.paragraphs:
    newArr.append(para.text)

# remove empty element ""
while("" in newArr):
    newArr.remove("")

# split array into a list of tupule of 5 element
tupuleArr = list(zip(*[iter(newArr) ]*5 ))
l = 1

for k in tupuleArr:
    # convert loop tupule to list
    y = list(k)
    i = 0

    dict2 = {}

    while i < len(fields):
        dict2["QuestNo"] = l
        dict2[fields[i]] = y[i][2:].strip()
        i = i + 1
    l = l + 1

    json_li.append(dict2)
print(json.dumps(json_li, indent=4))
