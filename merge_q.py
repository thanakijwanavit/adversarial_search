import argparse
import json
import os
import pprint
def merge_dict_add_value(dict1, dict2):
   ''' Merge dictionaries and keep values of common keys in list'''
   dict3 = {**dict1, **dict2}
   for key, value in dict3.items():
       if key in dict1 and key in dict2:
               dict3[key] = value + dict1[key]
 
   return dict3

files = os.listdir('./q')
files_without_main_q = [file for file in files if file not in ['q.json','q_updated.json']]
print(files_without_main_q)
with open('./q/q.json', 'r') as f:
    q=json.load(f)

print('len of q is {}'.format(len(q.keys())))
    
for qs_name in files_without_main_q:
    with open('./q/'+qs_name, 'r') as f:
        qs = json.load(f)
    for key in qs.keys():
        if key in q.keys():
            q[key] = merge_dict_add_value(q[key],qs[key])
        else:
            q[key] = qs[key]
    print(' len of qs is {}, len of new q is {}'.format(len(qs.keys()),len(q.keys())))

with open('./q/q_updated.json', 'w') as f:
    q=json.dump(q,f)

for file_name in files_without_main_q:
    os.remove('./q/'+file_name)
os.rename('./q/q_updated.json','./q/q.json')