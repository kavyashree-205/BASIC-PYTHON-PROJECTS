import time
import sys
import random
number=random.randint(1,100)
def intro():
    print("WELCOME TO GUESS THE NUMBER GAME\nHERE YOU NEED TO GUESS THE NUMBER")
    time.sleep(1)
    print("BETWEEN 1 TO 100\n5 CHANCES WILL BE GIVEN\nWITH SOME INTRESTING HINTS\n\n")

def lesser_or_greater(guess):
    global number
    if guess>number:
        print("THE NUMBER IS LESS THAN YOUR GUESS\n")
    elif guess==number:
        print("CONGRATS..YOU GUESSED THE RIGHT NUMBER\n")
        sys.exit()
    else:
        print("THE NUMBER IS GREATER THAN YOUR GUESS\n")


def divisible(guess):
    global number
    if guess==number:
        print("CONGRATS..YOU GUESSED THE RIGHT NUMBER\n")
        sys.exit()
    lesser_or_greater(guess)
    time.sleep(1)
    num_list=list()
    for x in range(1,9):
        if number%x == 0:
            num_list.append(x)
    if len(num_list)==1:
        print("THE NUMBER IS ONLY DIVISIBLE BY 1\n")
    else:
        print("THE NUMBER IS DIVISIBLE BY ",random.choice(num_list[1:]))
        print("\n")


def sum_digits(guess):
    global number
    if guess==number:
        print("CONGRATS..YOU GUESSED THE RIGHT NUMBER\n")
        sys.exit()
    divisible(guess)        
    time.sleep(1)
    total=0
    num1=number
    while num1 != 0:
        total=total+int(num1%10)
        num1=int(num1/10)
    print("THE SUM OF DIGITS OF THE NUMBER IS ",total)
    print("\n")

def diff(guess):
    global number
    if guess==number:
        print("CONGRATS..YOU GUESSED THE RIGHT NUMBER\n")
        sys.exit()
    divisible(guess)
    time.sleep(1)
    difference=abs(number-guess)
    if difference<=10:
        print("YOUR GUESS IS ATMOST 10 NUMBERS AWAY FROM THE CORRECT NUMBER\n")
    else:
        print("YOUR GUESS IS ATLEAST 11 NUMBERS AWAY FROM THE CORRECT NUMBER\n")

    
def error_handling(guess):
    if guess<1:
        print("GUESS NUMBER SHOULD NOT BE NEGETIVE\n")
        guess=int(input("PLEASE ENTER THE GUESS NUMBER : "))
    else:
        if guess>100:
            print("GUESS NUMBER SHOULD NOT EXCEED 100\n")
            guess=int(input("PLEASE ENTER THE GUESS NUMBER : "))
                  
        
intro()
guess=int(input("FIRST GUESS : "))
error_handling(guess)
lesser_or_greater(guess)
guess=int(input("SECOND GUESS : "))
error_handling(guess)
divisible(guess)
guess=int(input("THIRD GUESS : "))
error_handling(guess)
sum_digits(guess)
guess=int(input("FOURTH GUESS : "))
error_handling(guess)
diff(guess)
guess=int(input("FIFTH GUESS : "))
if guess==number:
    print("HURREY..FINALLY YOU WON\n")
    time.sleep(5)
else:
    print("YOU LOST,THE NUMBER IS",number)
    time.sleep(5)
    
    
        
        
    
