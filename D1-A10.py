from fuzzywuzzy import fuzz
from fuzzywuzzy import process
def fuzzy_name_matching(list1, list2):
    matches = []
    for name in list1:
        match = process.extractOne(name, list2, scorer=fuzz.ratio)
        matches.append((name, match[0], match[1]))
    return matches
list1 = ['John Doe', 'Jane Smith', 'Mary Jane', 'William Brown']
list2 = ['Jon Doe', 'Jane Smtih', 'Marie Jane', 'William Browne']
result = fuzzy_name_matching(list1, list2)
for name, match, score in result:
    print(f"'{name}' matches with '{match}' with a similarity score of {score}")
