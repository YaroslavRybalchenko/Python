import random
x1=int(input('Введите начальное число диапазона загадывания:'))
x2=int(input('Введите конечное число диапазона загадывания:'))
task=input('Введите число, которое вы хотите мне загадать:')
while True:
    guess=random.randrange(x1,x2)
    print(guess)
    if (guess!=task):
         clue=input('Дайте подсказку пожалуйста. Ваше число больше, меньше или равно '+str(x2-((x2-x1)//2))+' ?')
         if clue=='больше':
             x1=x2-((x2-x1)//2)
         elif clue=='меньше':
             x2=x2-((x2-x1)//2)
         elif clue=='равно':
             input('Ура,я угадал')
             break
         else:
             print('Ошибка ввода')
    else:
        input('Ура,я угадал')
        break
         
   
    
