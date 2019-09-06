def find_it(seq):
    deck=[]
    ind=[]
    for x in seq:
        deck.append([x,seq.count(x)])
    deck.sort(key=lambda x:x[1])
    pattern=0
    for i in range(len(deck)-1):
        if deck[i][1]==deck[i+1][1] and deck[i][0]!=deck[i+1][0]:
            pattern=deck[i][1]
            break
        elif (deck[i][1]==deck[i+1][1]):
            pattern=deck[i][1]
    for x in deck:
        if x[1]!=pattern:
            return(x[0])
            break
