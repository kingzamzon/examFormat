import docx2txt
import json
import collections
import re

#get docx text
text = docx2txt.process('useFul.docx')

# resultant dictionary
dict1 = {}

#fields in the sample file
fields = ['Questions', 'OptionA', 'OptionB', 'OptionC', 'OptionD']

#convert to list
li = [x for x in text.split('\n')]
# li = li.split()
newArr = []

newVal = li[0].split(' ')

i = 0
while i < len(newVal):
    # newVal[i]
    for d in newVal[i]:
        print(d)
    # newArr.append(io)
    i += 1

print(newArr)

# print((li[0].split(' '))

# for j in li[0].split(' '):
#     # print(j[0])
#     io = ""
#     if not j:
#         io += ','
#         newArr.append(io)
#     else:
#         io += str(j)
#         # print(io)
#         print(io)
# #remove ''s i.e NOnes
# li = list(filter(None, li))

# print(newArr)

# for x in li:
#     x = x[2:]
#     print(x)
    # li = re.sub(",", ".", li)
#     print(x.strip("."))
#     y = x.rsplit('.')
    # print(y)
