
def least():
    optimal = [11, 13, 14, 16, 17, 18, 19, 20]
    for i in range(20, 1000000000, 20):
        if all(i % j == 0 for j in optimal):
            return i
    return None

print(least())
