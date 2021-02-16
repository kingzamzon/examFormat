#!python3
import re
import json
import sys
from pathlib import Path

'''
Format to run file: python directoryPath:
python 'pop/content/EdSofta SSCE 2021 Objectives/Accounts/'
'''

directory_path = "%s" % sys.argv[1]

basepath = Path('pop/content/EdSofta SSCE 2021 Objectives/Accounts/')
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file():
        print(item.name)

'''
{
    question_no: number;
    question: string;
    option_a: string|null;
    option_b: string|null;
    option_c: string|null;
    option_d: string|null;
    option_e: string|null;
    answer: string; where answer is either A-E
    answer_meta:string;
    topic:string;
    difficulty:string;
}
'''

json_li = []

#fields in the sample file
fields = ['question', 'option_a', 'option_b', 'option_c', 'option_d', 'answer', 'answer_meta', 'topic', 'difficulty']

with open('pop/content/EdSofta SSCE 2021 Objectives/Accounts/2006.json', 'r') as read_file:
    #Variable declaration
    data = json.load(read_file)
    i = 1
    answer_i = 0

    list_data_items = list(data.items())

    print("Datatype:", type(data))
    print("Length:", len(data))
    print("Available Keys", data['Question 1'].keys())

    #looping
    for j in data:
        i = i + 1
        
        if(i > len(data)):
            break

        # initialize empty object
        new_fmt = {}
        dict2 = {}

        k = 0
        while k < len(fields):
            dict2["question_no"] = i
            if fields[k] == "question":
                dict2[fields[k]] = data[j]['Question']
            if fields[k] == "option_a":
                dict2[fields[k]] = re.findall(r'<span style="font-family:serif;">(.+?)<span>', data[j]['Options'][0]['Value'])[0]
            if fields[k] == "option_b":
                dict2[fields[k]] = re.findall(r'<span style="font-family:serif;">(.+?)<span>', data[j]['Options'][1]['Value'])[0]
            if fields[k] == "option_c":
                dict2[fields[k]] = re.findall(r'<span style="font-family:serif;">(.+?)<span>', data[j]['Options'][2]['Value'])[0]
            if fields[k] == "option_d":
                dict2[fields[k]] = re.findall(r'<span style="font-family:serif;">(.+?)<span>', data[j]['Options'][3]['Value'])[0]
            if fields[k] == "answer":
                dict2[fields[k]] = data['Answers'][answer_i]
            if fields[k] == "answer_meta":
                dict2[fields[k]] = ''
            if fields[k] == "topic":
                dict2[fields[k]] = data[j]['Topic']
            if fields[k] == "difficulty":
                dict2[fields[k]] = data[j]['Difficulty']
            k = k + 1

        answer_i = answer_i + 1

        json_li.append(dict2)

        # print(dict2)
        # print(json.dumps(json_li, indent=4))

    out_file = open('kok.json', 'w')
    json.dump(json_li, out_file, indent = 4)
    out_file.close()

    # while i < len(data):
        # print(i)
        # print(list_data_items[i][1])
        # print( list(data.items())[i][1]['Difficulty'])
        # i = i + 1

    # Question 
    # print(data['Question 32']['Question'])

    # Options
    # print(data['Question 1']['Options'])

    #Options 
    # print(type(data['Question 1']['Options']))
    # options = data['Question 1']['Options']
    # for option in options:
    #     # get options
    #     print(option['Key'])
    #     print( re.findall(r'<span style="font-family:serif;">(.+?)<span>',option['Value']) )

    # Answers
    # Get the first answer
    # print(data['Answers'][0])
