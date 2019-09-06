import random 


print('\t\t\t\t\t\t Программа "УГАДАЙ ЧИСЛО"\n')
print('\t\t\t\t\t\t    Добро пожаловать\n')


lucklevel1='Везунчик от бога'
lucklevel2='Счастливчик'
lucklevel3='Удачливый'
lucklevel4='Более-менее'
lucklevel5='Невезучий'
lucklevel6='Неудачник'
lucklevel7='33 несчастья'



start=input('Хотите начать игру? (да/нет):')
try1=0
if (start=='да'):
    print('\n')
    print('Правила игры очень просты, программа загадывает вам число от 1 до 500 \n'\
          +'и через пару-тройку ходов начнет давать вам подсказки, чтобы облегчить вашу участь,\n'\
          +'и вы смогли наконец угадать это число. Также она оценит уровень вашей удачи.\n')
    input('Если вы прочли правила, нажмите Enter, чтобы продолжить\n')

    
    number=random.randint(1,500)



    
    while True:
        
        while True:
            guess=input('Введите ваше число:')
            try:
                guess=int(guess)
                break
            except ValueError:
                print('Ошибка ввода, попробуйте еще раз: ')
                
        try1=try1+1
        
        if (try1==10 or try1==20 or try1==30 or try1==40):
            question=input('Хотите сдаться? Если уже устали от этой пытки-наберите "да", если вы мазохист-жмите Enter\n ')
            if (question=='да'):
                input('Разблокировано достижение - "Слабак", нажмите Enter, чтобы выйти')
                break

        if (try1>3):
            if (guess>number):
                print('Подсказка: ваше число больше загаданного')
            else:
                print('Подсказка: ваше число меньше загаданного')
        
        if (int(guess)==number):
            print ('Поздравляем, вы угадали число с '+str(try1)+' попыток')
            print ('Ваш уровень удачи - ',end=" ")
            if (try1==1):
                print(lucklevel1)
            elif(try1>1 and try1<=3):
                print(lucklevel2)
            elif(try1>3 and try1<=6):
                print(lucklevel3)
            elif(try1>6 and try1<=10):
                print(lucklevel4)
            elif(try1>10 and try1<=20):
                print(lucklevel5)
            elif(try1>20 and try1<=30):
                print(lucklevel6)
            elif(try1>30):
                print(lucklevel7)
            print('\n')
            check=input('Хотите сыграть еще разок? (да/нет):')
            if (check=='да'):
                try1=0
                number=random.randint(1,500)
                continue
            else:
                 break
            
        else:
            print('Не угадали, попробуйте еще разок')
            
            
           
        
            
            
    

