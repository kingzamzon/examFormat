#!python3
import mammoth
import re
import json
import sys
'''
Format to run file: python readDocFile.py useFul.docx
useFul.docx serve as filename
'''
fileName = "%s" % sys.argv[1]
jsonFileName = "%s" % sys.argv[2]

json_li = []

#fields in the sample file
fields = ['Questions', 'OptionA', 'OptionB', 'OptionC', 'OptionD', 'OptionE', 'Answers']

with open(fileName, "rb") as doc_file:
    result = mammoth.convert_to_html(doc_file)
    html = result.value
    messages = result.messages
    # print('sdsd', messages)

    # check if the value is <ol> because some appear to be <p>
    check_ol = html[:4]
    if(check_ol == "<ol>"):
        array_html = re.findall(r'<li>(.+?)</li>', html)
    else:
        array_html = re.findall(r'<p>(.+?)</p>', html)

    tupuleArr = list(zip(*[iter(array_html) ]*7 ))
    l = 1

    for k in tupuleArr:
        # convert loop tupule to list
        y = list(k)
        i = 0

        dict2 = {}

        while i < len(fields):
            dict2["QuestNo"] = l
            if fields[i] != "Answers":
                dict2[fields[i]] = '<p>'+y[i][2:].strip().replace('.', '')+'</p>'
            else:
                dict2[fields[i]] = y[i][2:].strip().replace('.', '')
            i = i + 1
        l = l + 1

        json_li.append(dict2)
    print(json.dumps(json_li, indent=4))

    # Print to json file
    out_file = open(jsonFileName, 'w')
    json.dump(json_li, out_file, indent = 4)
    out_file.close()
