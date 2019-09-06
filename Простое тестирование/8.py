f=open('Test.txt','r')
points=0
counter=0
while True:
    question=f.readline().strip()
    if (not question):
        break
    answer1=f.readline().strip()
    answer2=f.readline().strip()
    answer3=f.readline().strip()
    check=f.readline().strip()
    print(question)
    print('1)'+str(answer1))
    print('2)'+str(answer2))
    print('3)'+str(answer3))
    inp=str(input('Введите номер ответа:\n'))
    counter=counter+1
    if (inp==check):
        points=points+1
print('Вы набрали '+str(points)+' очков из '+str(counter)+' возможных')
f.close()
