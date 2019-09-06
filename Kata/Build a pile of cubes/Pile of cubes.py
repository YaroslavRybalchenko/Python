def find_nb(m):
    ctr=round((m**(1/4)))
    summ=0
    tmp=ctr
    while tmp!=0:
        summ+=(tmp**3)
        tmp-=1
    while True:
        if summ==m:
            return ctr
        ctr+=1
        summ+=ctr**3
        if summ>m:
            return -1
