'''
2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.

Какое самое маленькое число делится нацело на все числа от 1 до 20?
'''

import datetime
a = datetime.datetime.now()
def least_one():
    number=1
    while True:
        for i in range(20,0,-1):
            if number%i!=0:
                break
            elif i==1:
                b = datetime.datetime.now()
                return(number, b-a)
        number+=1
print(least_one())
