import time
import sys
user_info={1234:'kavyashree',5678:'user-2',5638:'user-3'}
user_amount={1234:3300,5678:2100,5638:1000}
user_accno={1234:1111111111111111,5678:1234567890111111,5638:1111111234567890}
def introduction():
    print('welcome to atm simulation '.upper())
    print('\n')
    print('THERE WILL BE A TWO STEP VERIFICATION OF PIN,PLEASE COOPERATE....')
    print('\n')
    print('1.BALENCE ENQUIRY\n2.UPDATE PIN\n3.CASH WITHDRAWL\n4.CASH DEPOSIT\n5.MONEY TRANSFER\n6.EXIT')
    
def choice():
    a=int(input("CHOOSE THE OPTION : "))
    if a == 1:
        balence()
    elif a == 2 :
        updatepin()
    elif a == 3 :
        withdrawl()
    elif a == 4 :
        deposit()
    elif a == 5:
        transfer()
    elif a == 6:
        exite()
    else:
        print('INCORRECT OPTION')
        choice()
def error():
    try:
        s=int(input('enter your atm pin : '.upper()))
        print(user_info[s])
    except LookupError:
        print('INCORRECT PIN,THIS IS YOUR LAST TRY,ELSE ACCOUNT GETS BLOCKED')

def balence():
    error()
    s=int(input('enter your atm pin : '.upper()))
    print('WELCOME {}\n'.format(user_info[s]))
    time.sleep(1)
    amount=user_amount[s]
    print('your account balence : ',amount)
    print('\n')
    introduction()
    choice()
    
def updatepin():
    error()
    s=int(input('enter your atm pin : '.upper()))
    print('WELCOME {}\n'.format(user_info[s]))
    time.sleep(1)
    x=int(input('PLEASE ENTER THE PIN YOU WANT TO UPDATE : '))
    user_info[x]=user_info.pop(s)
    time.sleep(1)
    print('YOUR PIN IS UPDATED : ',user_info)
    print('\n')
    introduction()
    choice()
    
def withdrawl():
    error()
    s=int(input('ENTER YOUR ATM PIN : '))
    print('WELCOME {}\n'.format(user_info[s]))
    time.sleep(1)
    b=float(input('ENTER THE AMOUNT FOR WITHDRAWL : '))
    amount=user_amount[s]-b
    if amount<0:
        print('CASH INSUFFICIENT')
    else:
        print('YOUR BALENCE AMOUNT : ',amount)
    print('\n')        
    introduction()
    choice()

def deposit():
    error()
    s=int(input('enter your atm pin : '.upper()))
    print('WELCOME {}\n'.format(user_info[s]))
    time.sleep(1)
    c=float(input('ENTER THE AMOUNT FOR CASH DEPOSIT : '))
    amount=user_amount[s]+c
    print('YOUR TOTAL AMOUNT : ',amount)
    print('\n')
    introduction()
    choice()
def transfer():
    error()
    s=int(input('enter your atm pin : '.upper()))
    print('WELCOME {}\n'.format(user_info[s]))
    time.sleep(1)
    v=int(input('PLEASE ENTER THE ACCOUNT NUMBER  : '))
    d=float(input('PLEASE ENTER THE AMOUNT TO TRANSFER : '))
    c=user_amount[s]-d
    key_list=list(user_accno.keys())
    val_list=list(user_accno.values())
    key=key_list[val_list.index(v)]
    print('YOUR BALENCE : ',c)
    o=input('do you want to check your to account balence : '.upper())
    o=o.lower()
    if o == 'yes':
        amount=user_amount[key]+d
        print('ACCOUNT BALENCE : ',amount)
    print('\n')
    introduction()
    choice()

def exite():
    print("***THANK YOU FOR USING THE BANKING SERVICE***")
    sys.exit()
    
    
       
print('\n\n')
introduction()
print('\n\n')
choice()
