def abbreviate(words):
    words = words.replace('-', ' ')
    acronym = [word.strip('_')[0].upper() for word in words.split()]
    return "".join(acronym)

import re
def camel_case_split(str):
    return re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|$))', str)

str = "HyerText"
print(camel_case_split(str))