import sys,shelve,datetime

def open_file(filename,mode):
    try:
        file=open(filename,mode)
        print('Файл успешно найден!')
    except IOError as error:
        print('Файл не найден, программа завершена с ошибкой: ',error)
        sys.exit()
    return file

def next_line(file):
    line=file.readline()
    return line

def next_task(file):
    theme=next_line(file)
    task=next_line(file)
    answers=[]
    for i in range(5):
        answers.append(next_line(file))
    cor_answer=next_line(file)
    emtptyspot=next_line(file)
    return (theme,task,answers,cor_answer)

def coungurations():
    print('Спасибо за игру')

def records(filename,mode,score):
    r_file=shelve.open(filename,mode)
    name=input('Введите ваше имя: ')
    r_file[name]=str(score)+'  '+datetime.datetime.now().strftime('%H:%M %d/%m/%Y')
    ctrl=input('Хотите увидеть результаты всех игроков?(Y/N)')
    if ctrl=='Y':
        for i in r_file:
            print(i,' - ',r_file[i])

def main():
    score=0
    file=open_file('Tasks.txt','r')
    theme=next_line(file)
    print(theme)
    theme,task,answers,cor_answer=next_task(file)
    while theme:
         print(theme)
         print(task)
         counter=1
         for i in answers:
             print(counter,')',i)
             counter+=1
         print()
         answer=input('Ваш ответ(выберите номер ответа): ')
         if answer==cor_answer[0]:
             print('Верно!')
             score+=1
         else:
             print('Неверно! ')
         theme,task,answers,cor_answer=next_task(file)
    print('Ваш счет в игре: ',score)
    records('records.dat','c',score)
    
main()
             



        
