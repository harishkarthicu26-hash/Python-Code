print("Welcome to python pizza delivery")
size=input("Enter the pizza size you want(s,m,l)")
p=input("do you want pepporoni?(y/n)")
c=input("do you want extra cheese?(y/n)")
dollar=0
if size == "s":
    dollar += 15
    if p=="y":
        dollar +=2
elif size == "m":
    dollar += 20
    if p=="y":
        dollar +=3
elif size == "l":
    dollar +=25
    if p=="y":
        dollar +=3
if c=="y":
    dollar+=1
print(f"Your total bill is ${dollar}")

    
