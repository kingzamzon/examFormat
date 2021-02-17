#!python3
import re
import json
import sys
from pathlib import Path

'''
Format to run file: python directoryPath:
python jsonFormater.py 'pop/content/EdSofta SSCE 2021 Objectives/Biology/'

Script format json files in a folder to this format:
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

directory_path = "%s" % sys.argv[1]

basepath = Path(directory_path)
files_in_basepath = basepath.iterdir()
for item in files_in_basepath:
    if item.is_file() and item.name != '2008.json' and item.name != '2013.json' and item.name != '2015.json':
        print(item.name)
        json_li = []
        
        # 'pop/content/EdSofta SSCE 2021 Objectives/Biology/2006.json'
        full_directiory = directory_path+item.name

        #fields in the sample file
        fields = ['question', 'option_a', 'option_b', 'option_c', 'option_d', 'answer', 'answer_meta', 'topic', 'difficulty']

        with open(full_directiory, 'r') as read_file:
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
                    dict2["question_no"] = answer_i
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
                    if fields[k] == "topic" and 'Topic' in data[j]:
                        dict2[fields[k]] = data[j]['Topic']
                    if fields[k] == "difficulty"  and 'Topic' in data[j]:
                        dict2[fields[k]] = data[j]['Difficulty']
                    k = k + 1

                answer_i = answer_i + 1

                json_li.append(dict2)

                # print(json.dumps(json_li, indent=4))

            out_file = open(item.name, 'w')
            json.dump(json_li, out_file, indent = 4)
            out_file.close()
    
