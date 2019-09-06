import re
def to_camel_case(text):
    res=re.split(r'[_-]',text)
    for i in range(1,len(res)):
        res[i]=res[i].capitalize()
    final=''
    for i in res:
        final+=i
    return(final)
