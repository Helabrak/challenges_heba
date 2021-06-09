import re

def abbreviate(str):
    # COACHES' NOTE: don't use reserved keywords for variable names.
    case=[]
    case= re.findall(r'[A-Z](?:[a-z]+|[A-Z]*(?=[A-Z]|\s| $))|[a-z]+', str)
    print(case)
    acronym=""
    for i in case:
        acronym+=i[0].upper()
    return acronym
    # COACHES' NOTE: don't forget to clean up your print statements.
    print(abbreviate())

# COACHES' NOTE: Nice work.
