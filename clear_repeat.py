with open('./info/interested_authors.txt') as f:
    interested_authors = f.read().splitlines()
    
interested_authors = list(set(interested_authors))
with open('./info/interested_authors.txt', 'w') as f:
    f.write('\n'.join(interested_authors) + '\n')

with open('./info/title_keywords.txt') as f:
    title_keywords = f.read().splitlines()

title_keywords = list(set(title_keywords))
with open('./info/title_keywords.txt', 'w') as f:
    f.write('\n'.join(title_keywords) + '\n')

with open('./info/abstract_keywords.txt') as f:
    abstract_keywords = f.read().splitlines()

abstract_keywords = list(set(abstract_keywords))
with open('./info/abstract_keywords.txt', 'w') as f:
    f.write('\n'.join(abstract_keywords) + '\n')