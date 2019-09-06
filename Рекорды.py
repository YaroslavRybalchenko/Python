ctrl=('1240')
score=[]
while (1==1):
    menu=input(''' ВЫБЕРИТЕ ПУНКТ МЕНЮ:
0 - Выйти
1 - Показать рекорды
2 - Добавить рекорд
3 - Удалить рекорд
4 - Сортировать список
''')
    print('Ваш выбор:', menu)
    if menu=='0':
        print('До свидания!')
        break
    elif menu=='1':
        if score==[]:
            print('Список рекордов пуст')
        else:
            print(score)
    elif menu=='2':
        addition=input('Введите значение: ')
        score.append(addition)
    elif menu=='3':
        print(score)
        delete=input('Введите номер удаляемого рекорда:')
        del score [int(delete)-1] 
    elif menu=='4':
        score.sort()
        print(score)
    else:
        print('Ошибка ввода')
        continue
         
        



    
