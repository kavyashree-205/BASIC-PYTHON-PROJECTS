import random
from wordslist import list_words
import sys
import time

print("WELCOME TO HANGMAN GAME\n")
print("YOU WILL BE GIVEN BLANKS\n")
print("GUESS THE WORD BEFORE MAN GETS HANGED\n\n")

list_words=[words for words in list_words if 4<=len(words)<=10]

track=0
stage=0


hangman_stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

word=random.choice(list_words)


blank="_ "*len(word)

characters=[]

for i in word:
    characters.append(i)

blank_list=blank.split()

def instruction():
    print("1.PLAY\n")
    print("2.DEVELOPER CONTACT\n")
    print("3.EXIT\n")

def getinput():
    global enter
    enter=input("\nEnter an Alphabet : ").lower()
    if enter.isalpha()==False:
        print("\n\nPLEASE ENTER ALPHABETS (A-Z OR a-z)\n\n")
        getinput()
    elif len(enter)>1 or len(enter)==0:
        print("\n\nPLEASE ENTER A SINGLE ALPHABET\n\n")
        getinput()
    check()

def check():
    global track,stage
    track=0
    guess=""
    for j in range(0,len(characters)):
        if enter==characters[j]:
            blank_list[j]=enter
        else:
            track=track+1
            
    for p in blank_list:
        guess=guess+p+" "


    if track==len(characters):
        stage=stage+1
        if stage>=6 and blank_list != characters:
            out()
        elif stage<6 and blank_list != characters:
            print(hangman_stages[stage])
            print(guess)
    else:
        print(hangman_stages[stage])
        print(guess)

    if blank_list==characters and stage<6:
        won()
    elif blank_list != characters and stage<6:
        getinput()

def out():
    print("GAME OVER...MAN GOT HANGED!!!")
    time.sleep(10)
    sys.exit()
    
def won():
    print("\nYOU WON THE GAME !!!")
    time.sleep(10)
    sys.exit()
    
def choice():
    n=int(input("ENTER YOUR CHOICE : "))
    if n<=0 or n>=4:
        print("\n\nENTER A VALID CHOICE...BETWEEN 1 TO 3\n\n")
        choice()   
    if n==1:
        print(hangman_stages[0])
        print(blank)
        getinput()
        check()
    elif n==2:
        print("\n\nK.G KAVYASHREE\nEmail:kavyashree3513@gmail.com\n\n")
        time.sleep(10)
    elif n==3:
        sys.exit()

instruction()
choice()

    
    







