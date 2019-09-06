import random

print('\t\t\t    SoftLock solutions,Ink\n'+'\t\t\tYour Security is Our Security\n\n')

count=0

while (1==1):
    login=input('Enter your login: ')
    password=input('Enter your password: ')

    
    if ((login=='Worker_986') and (password=='qwerty1234')):
        print('\a') 
        input('Welcome! Press enter to continue')
        dept=input('In which department do you want to work today? Choose the needed number\n1)Welding\n2)Stamping\n3)Milling\n')
        if (dept=='1'):
            print ('Your worklplace in welding department today is: '+str(random.randint(1,30)))
        elif (dept=='2'):
            print ('Your worklplace in stamping department today is: '+str(random.randint(31,60)))
        elif (dept=='2'):
            print ('Your worklplace in mining department today is: '+str(random.randint(61,90)))
            
        break

    
    else:
        count=count+1
        if (count==2):
            print('Last try!')
        if (count>2):
            input('Your account is blocked')
            break
        print('Incorrect login/password, please try again')



