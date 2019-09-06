def cakes(recipe, available):
    number=float('inf')
    for x in recipe:
        if x in available:
            temp=available[x]//recipe[x]
            if temp<number:
                number=temp
        else:
            return 0
    return(number)
