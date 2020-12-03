#email slicer program
email=[]
username=[]
mail_server=[]
top_level_domain=[]

n=int(input("ENTER THE NUMBER OF EMAILS : "))
print("\n")
for i in range(1,n+1):
    name=input("PLEASE ENTER THE EMAIL ID : ").strip()
    email.append(name)
    
for j in email:
    a=j[:j.index('@')]
    b=j[j.index('@')+1:j.index('.')]
    c=j[j.index('.'):]
    username.append(a)
    mail_server.append(b)
    top_level_domain.append(c)
for k in range(0,n):
    print("\n{} .USERNAME : {}\n\nMAIL SERVER NAME : {}\n\nTOP LEVEL DOMAIN : {}".format(k+1,username[k],mail_server[k],top_level_domain[k]))
    print("\n")
    print("***************************************************************************")




