import re

def abbreviate(str):
    case=[]
    case= re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|\s| $))|[a-z]+', str)
    print(case)
    acronym=""
    for i in case:
        acronym+=i[0].upper()
    return acronym

    print(abbreviate())


