import os
import time
import json
import pickle

# load database
with open('./db.p', 'rb') as f:
    db = pickle.load(f)
    
# global variables
with open('./interested_authors.txt') as f:
    interested_authors = f.read().splitlines()
    
with open('./keywords.txt') as f:
    keywords = f.read().splitlines()

keys = sorted(list(db.keys()))
newest_time = db[keys[-1]]['updated'].split('T')[0]

# define rules
def in_interested_authors(data):
    flag = False
    for author in data['authors']:
        if author['name'] in interested_authors:
            flag = True
            break
    return flag

def in_keywords(data):
    flag = False
    title = data['title'].lower()
    abstract = data['summary'].lower()
    for kw in keywords:
        if '+' in kw:
            to_contain = [x.lower() for x in kw.split('+')]
        else:
            to_contain = [kw.lower()]
        sub_flag = True
        for word in to_contain:
            if word not in title + abstract:
                sub_flag = False
                break
        if sub_flag:
            flag = True
            break
    return flag

def filter_data(data, rules_or, rules_and):
    for name, rule in rules_and.items():
        if not rule(data):
            return False
    
    flag = False
    for name, rule in rules_or.items():
        if rule(data):
            flag = True
            break
    return flag

def is_newest(data):
    return data['published'].startswith(newest_time)

# composite rules
rules_or = {'Interested authors': in_interested_authors,
         'Keywords': in_keywords}
rules_and = {'Today': is_newest}

# filter data
filter_results = []
for k, v in db.items():
    if filter_data(v, rules_or, rules_and):
        filter_results.append(k)
filter_results = list(reversed(sorted(filter_results)))
print(f'Filtered {len(filter_results)} papers on {newest_time}')

# write results
filter_dict = {data: db[data] for data in filter_results}
with open(f'./daily_results/{newest_time}.json', 'w') as f:
    json.dump(filter_dict, f, indent=2)
    
write_str = ''
for idx, k in enumerate(filter_results):
    data = db[k]
    write_str += data['link'] + '\n' + '\n'
    write_str += data['title'].replace('\n ', '') + '\n' + '\n'
    
    write_str += ', '.join([x['term'] for x in data['tags']]) + '\n' + '\n'
    
    write_str += ', '.join([x['name'] for x in data['authors']]) + '\n' + '\n'
    write_str += data['summary'].replace('\n', ' ')+ '\n' + '\n'
    if idx < len(filter_results) - 1:
        write_str += '-' * 88 + '\n' + '\n'
with open(f'./daily_results/{newest_time}.txt', 'w') as f:
    f.write(write_str)

os.system('cp ' + f'./daily_results/{newest_time}.txt' + ' /home/zhenyu/Desktop/arxiv-newest.txt')