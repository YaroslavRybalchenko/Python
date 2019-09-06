'''
Простые делители числа 13195 - это 5, 7, 13 и 29.

Каков самый большой делитель числа 600851475143, являющийся простым числом?
'''

def eiler(N):
    memo=[]
    limit=1
    for i in range(1,round(N/2)+1):
        limit=1
        for j in range(2,i):
            if i%j==0:
                break
            elif j==i-1 and (N%i==0):
                memo.append(i)
                print(i)
                for s in memo:
                    print(s)
                    limit=s*limit
                if limit==N:
                    print(memo)
                    print(memo[len(memo)-1])
                    return
eiler(600851475143)
print('Последнее число-ответ')
