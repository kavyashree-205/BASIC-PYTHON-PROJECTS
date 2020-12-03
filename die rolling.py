import random
import sys
import time
MAX1=6
MIN1=1
MAX2=12
MIN2=2
print("*****WELCOME TO ROLLING DICE SIMULATION*****\n")
def roll():
    print("DO YOU WANT TO ROLL\n1.A SINGLE DIE?\n2.TWO DICE?\n3.MULTIPLE DICE?\n4.IMMEDIATE EXIT!!!\n")
    time.sleep(1)
    b=input("PLEASE ENTER YOUR CHOICE : ")
    b=b.lower()
    if b == "1":
        a=random.randint(MIN1,MAX1)
        print("SINGLE DIE VALUE : ",a)
        print("\n")
        time.sleep(0.5)
        roll()
    elif b == "2":
        c=random.randint(MIN2,MAX2)
        print("TWO DICE VALUE : ",c)
        print("\n")
        time.sleep(0.5)
        roll()
    elif b == "3":
        n=int(input("PLEASE ENTER THE NUMBER OF DICE YOU WANT TO ROLL : "))
        MINN=n
        MAXN=6*n
        d=random.randint(MINN,MAXN)
        time.sleep(0.5)
        print("{} DICE VALUE : {}".format(n,d))
        time.sleep(0.5)
        print("\n")
        roll()
    elif b == "4":
        print("THANK YOU FOR YOUR TIME AND CONSIDERATION")
        sys.exit()
    else:
        print("PLEASE ENTER THE CORRECT CHOICE\n")
        time.sleep(0.5)
        roll()

roll()        
        
        
