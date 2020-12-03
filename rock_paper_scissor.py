import time
import random
opt=["rock","paper","scissor"]
user_points=0
comp_points=0
def intro():
    print('IN THIS GAME THE COMPUTER WILL BE PLAYING WITH YOU\nALL YOU NEED TO DO IS TYPE EITHER\nROCK OR\nPAPER OR\nSCISSOR\nTHERE WILL BE 5 TRIALS\nWHO SCORES THE MAXIMUM IS THE WINNER')
    print('\n\n')
    
def draw():
    global user_points
    global comp_points
    print('DRAW MATCH\n')
    time.sleep(1)
    print('your score : '.upper(),user_points)
    print('computer score :'.upper(),comp_points)
    print('\n\n')

def win():
    global user_points
    global comp_points
    print('YOU WON THE GAME\n')
    user_points=user_points+1
    time.sleep(1)
    print('your score :'.upper(),user_points)
    print('computer score :'.upper(),comp_points)
    print('\n\n')

def loose():
    global user_points
    global comp_points
    print('COMPUTER WON THE GAME\n')
    comp_points=comp_points+1
    time.sleep(1)
    print('your score :'.upper(),user_points)
    print('computer score :'.upper(),comp_points)
    print('\n\n')

def give():
    global b
    b=input('ENTER YOUR OPTION : ')
    b=b.lower()
    if(b!='rock')and(b!='paper')and(b!='scissor'):
        print('YOU HAVE WRITTEN THE INCORRECT OPTION\nPLEASE ENTER AGAIN\n')
        give()
        
intro()
name=input("enter your name : ".upper())
name=name.upper()
print('\n\n')
      
i=1
while i<6:
    print('TRIAL {}'.format(i))
    give()
    a=random.choice(opt)
    print('COMPUTERS OPTION :',a)
    print('\n')
    if a=='rock' and b=='rock':
        draw()
    elif a=='rock' and b=='paper':
        win()
    elif a=='rock' and b=='scissor':
        loose()
    elif a=='paper' and b=='rock':
        loose()
    elif a=='paper' and b=='paper':
        draw()
    elif a=='paper' and b=='scissor':
        win()
    elif a=='scissor' and b=='rock':
        win()
    elif a=='scissor' and b=='paper':
        loose()
    else:
        draw()
    i=i+1        
            

if user_points > comp_points:
    print('CONGRADULATIONS {} YOU WON THE GAME!!!'.format(name))
    time.sleep(2)
elif user_points==comp_points:
    print('EQUAL-EQUAL...DRAW MATCH')
    time.sleep(2)
else:
    print('OOPS! COMPUTER WON THE GAME')
    time.sleep(2)
        
        
        
        

