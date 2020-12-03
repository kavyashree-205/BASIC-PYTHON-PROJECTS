import random
import time
import numpy as np
import csv
import sys

def game():
    score=0
    with open('words.csv',mode='r') as data:
        data=np.array(data.readlines()[0].split(','))
        b=np.random.choice(data,5)
    print('WELCOME TO TERMINAL BASED FAST TYPING GAME\n')
    time.sleep(1)
    print('IN THIS GAME FIVE WORDS ARE GIVEN TO YOU\nYOU NEED TO TYPE IT CORRECTLY\nFOR EACH CORRECT WORD 10 POINTS WILL BE AWARDED\n')
    time.sleep(2)
    print('THE GAME STARTS IN 3 SECONDS')
    time.sleep(1)
    print('three....')
    time.sleep(1)
    print('two......')
    time.sleep(1)
    print('one......\n')
    print('START')
    start_time=time.time()
    for x in b:
        print(x)
        user_input=input(':').strip().lower()
        if user_input == x:
            score=score+10

    end_time=time.time()
    print('HEY...YOU HAVE COMPLETED THE GAME')
    time.sleep(1)
    print('YOUR SCORE IS : ',score)
    time.sleep(1)
    total_time=end_time-start_time
    print('TIME TAKEN TO FINISH THE GAME : ',str(total_time)+'sec')
    
    print('\n')

def again():
    key=input('DO YOU WANT TO TRY AGAIN ?(yes/no) ')
    key=key.lower()
    if key == 'yes':
        game()   
    else:
        sys.exit()

game()
print('\n')
again()
    
