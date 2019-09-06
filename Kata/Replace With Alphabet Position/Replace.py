def alphabet_position(text):
    text=text.lower()
    alpha='abcdefghijklmnopqrstuvwxyz'
    positions=''
    for x in text:
        if x in alpha:
            positions+=(str(alpha.index(x)+1)+' ')
    positions=positions.rstrip() 
    return(positions)
