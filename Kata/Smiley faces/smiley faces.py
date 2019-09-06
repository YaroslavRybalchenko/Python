import re
def count_smileys(arr):
    counter=0
    for face in arr:
        res=re.match(r'[:;][-~]?[\)D]',face)
        if res!=None:
            counter+=1
    return(counter)
    return
