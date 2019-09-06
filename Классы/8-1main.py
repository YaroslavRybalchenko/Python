import shelve


class Critter(object):
    total=0
    
    #@staticmethod
    def counter():
        print('Всего на ферме {} животных'.format(counter))
        
    def __init__(self,name,species,color,age,boredom=0,hunger=0,b_speed=1,h_speed=1,mood='прекрасно'):
        Critter.total+=1
        self.name=name
        self.species=species
        self.color=color
        self.age=age
        self.__boredom=boredom
        self.__hunger=hunger
        self.__b_speed=b_speed
        self.__h_speed=h_speed
        self.mood=mood

    def __str__(self):
        status=''
        status+=self.name+' '
        status+=self.species+' '
        status+=self.color+' '
        status+=self.age+' '
        status+=str(self.__boredom)+' '
        status+=str(self.__hunger)+' '
        status+=self.__b_speed+' '
        status+=self.__h_speed+' '
        status+=self.mood+' '
        return status
        

    def time_passes(self):
        self.__boredom+=int(self.__b_speed)
        self.__hunger+=int(self.__h_speed)

    #@property
    def mood_f(self):
        if self.__hunger+self.__boredom<=5:
            self.mood='прекрасно'
        elif 5<self.__hunger+self.__boredom<=10:
            self.mood='хорошо'
        elif 10<self.__hunger+self.__boredom<=15:
            self.mood='нормально'
        elif 15<self.__hunger+self.__boredom<=20:
            self.mood='плохо'
        elif 20<self.__hunger+self.__boredom:
            self.mood='ужасно'
        return self.mood

    def talk(self):
        self.mood_f()
        print('Я чувтствую себя {} {}'.format(self.mood,self.__hunger+self.__boredom))
        self.time_passes()
        return self.__boredom,self.__hunger

    def feeding(self,food):
        self.__hunger-=food
        print('{}:*хрустит едой*'.format(self.name))
        print('{}:"Спасибо!"'.format(self.name))
        self.time_passes
        return self.__hunger

    def play(self,play):
        self.__boredom-=play
        print('{}:"Уии!"'.format(self.name))
        self.time_passes
        return self.__boredom

def checker(ctrl,inp_message,error_message,alg):
    if alg=='1':
        while True:
            inp=input(inp_message)
            if inp==ctrl:
                print(error_message)
            else:
                return inp
                break
    if alg=='2':
        while True:
            inp=input(inp_message)
            if inp!=ctrl:
                print(error_message)
            else:
                return inp
                break
    if alg=='3':
        while True:
            inp=input(inp_message)
            if inp.lower() not in ctrl:
                print(error_message)
            else:
                return inp
                break
    


def add_creature():
    while True:
        question=input('Хотите поселить животное?(y/n)\n')
        if question in 'Yy':
            name=checker('','Введите имя: ','Недопустимое имя','1')
            text_file=open('species.txt','r')
            inp=text_file.read()
            print(type(inp))
            species=checker(inp,'Введите название особи: ','Недопустимый ввод','3')
            text_file.close()
            color=checker('','Введите цвет животного: ','Недопустимый ввод','1')
            age=checker('0123456789','Введите возраст животного: ','Недопустимый ввод','3')
            boredom=0
            hunger=0
            b_speed=(checker('0123456789','Введите скорость скуки животного: ','Недопустимый ввод','3'))
            h_speed=(checker('0123456789','Введите скорость голода животного: ','Недопустимый ввод','3'))
            mood='прекрасно'
            tmp=shelve.open('creatures.dat')
            tmp[name]=[species,color,age,boredom,hunger,b_speed,h_speed,mood] 
            tmp.close()            
        elif question in 'Nn':
            print('Возвращение в подменю поселения...')
            break
        else:
            print('Недопустимый ввод, попробуйте еще раз:\n')
            
def del_creature():
    while True:
        question=input('Хотите выселить животное?(y/n)\n')
        if question in 'Yy':
            display_creature()
            name=input('\n Введите имя животного, которого вы хотит выселить:')
            tmp=shelve.open('creatures.dat')
            deleted=tmp.pop(name,'Такой объект не найден.')
            tmp.close()
            if deleted=='Такой объект не найден.':
                print(deleted)
            else:
                print('Животное {} было выселено с фермы. Обновленный список обитателей:'.format(name))
                display_creature()            
        elif question in 'Nn':
            print('Возвращение в подменю поселения...')
            break
        else:
            print('Недопустимый ввод, попробуйте еще раз:\n')

def display_creature():
    tmp=shelve.open('creatures.dat')
    print('Сейчас на ферме живут:')
    for key in tmp:
        values=tmp[key]
        print(key,' - ',values[0])
    print('\n')
    tmp.close() 
            

def manager():
    while True:
        choice=input('''~~~Подменю поселения животных~~~:
\t0)Вернуться в главное меню
\t1)Поселить животное на ферму
\t2)Выселить животное с фермы
\t3)Посмотреть, кто сейчас живет на ферме\n''')
        if choice=='0':
            break
        elif choice=='1':
            add_creature()
        elif choice=='2':
            del_creature()
        elif choice=='3':
            display_creature()
        else:
            print('В меню нет такого пункта, попробуйте еще раз.')
    
def choose_creature():
    tmp=shelve.open('creatures.dat')
    print('Сейчас на ферме живут:')
    for key in tmp:
        values=tmp[key]
        print(key,' - ',values[0])
    print('\n')
    key=input('Введите имя животного, к которому вы хотите подойти: ')
    if key in tmp:
        values=tmp[key]
        print(values)
        print('Перед вами {} по имени {}. Цвет этого животного - {}. Ему - {}.'.format(values[0],key,values[1],values[2]))
        creature=Critter(key,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7])
        while True:
            choice=input('''Что вы хотите сдеалть с этим животным?:
\t0)Уйти
\t1)Покормить
\t2)Поиграть
\t3)Узнать самочувствие\n''')
            if choice=='0':
                break
            elif choice=='1':
               food=checker('0123456789','Сколько еды вы хотите дать животному?','Недопустимый ввод','3')
               hunger=creature.feeding(int(food))
               mood=creature.mood_f()
               print(mood)
               values[4]=hunger
               values[7]=mood
               tmp[key]=values
            elif choice=='2':
               play=checker('0123456789','Сколько времени вы хотите поиграть с животным?','Недопустимый ввод','3')
               boredom=creature.play(int(play))
               mood=creature.mood_f()
               values[3]=boredom 
               tmp[key]=values
            elif choice=='3':
               boredom,hunger=creature.talk()
               values[3]=boredom
               values[4]=hunger
               tmp[key]=values
    tmp.close()
    

def all_creatures():
    tmp=shelve.open('creatures.dat')
    print('Сейчас на ферме живут:')
    for key in tmp:
        values=tmp[key]
        print(key,' - ',values[0])
    print('\n')
    while True:
            choice=input('''Что вы хотите сделать??:
\t0)Уйти
\t1)Накормить всех
\t2)Поиграть со всеми\n''')
            if choice=='0':
                break
            elif choice=='1':
               food=checker('0123456789','По сколько еды вы хотите дать животным?','Недопустимый ввод','3')
               for key in tmp:
                    values=tmp[key]
                    creature=Critter(key,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7])
                    hunger=creature.feeding(int(food))
                    mood=creature.mood_f()
                    values[4]=hunger
                    values[7]=mood
                    tmp[key]=values
            elif choice=='2':
               play=checker('0123456789','Сколько времени вы хотите поиграть с животным?','Недопустимый ввод','3')
               for key in tmp:
                    values=tmp[key]
                    creature=Critter(key,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7])
                    boredom=creature.play(int(play))
                    mood=creature.mood_f()
                    values[3]=boredom
                    values[7]=mood
                    tmp[key]=values
    tmp.close()
    
def status_check():
    tmp=shelve.open('creatures.dat')
    for key in tmp:
        values=tmp[key]
        creature=Critter(key,values[0],values[1],values[2],values[3],values[4],values[5],values[6],values[7])
        print(creature)
    tmp.close()
    

def menu():
    while True:
        choice=input('''~~~ВЫБЕРИТЕ ПУНКТ МЕНЮ:~~~
\t0)Выход
\t1)Подменю поселения животных
\t2)Подойти к какому-то из животных
\t3)Поухаживать за всеми сразу\n''')
        if choice=='0':
            print('\nДо свидания')
            break
        elif choice=='1':
            manager()
        elif choice=='2':
            choose_creature()
        elif choice=='3':
            all_creatures()
        elif choice=='4':
            status_check()
        else:
            print('В меню нет такого пункта, попробуйте еще раз.')

menu()

