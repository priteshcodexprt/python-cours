import random
from statistics import mean

def gameWin(comp,you):
    if comp==you:
            return None
    if comp=='s':
        if you=='w':
            return False
    elif you=='g':
            return True
    elif comp=='w':
        if you=='s':
            return False
        elif you=='s':
            return True
    elif comp=='w':
        if you=='g':
            return False
    elif you=='w':
            return True

print ("comp turn :snake(s),water(w),Gun(g)")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='g'
elif randNo==3:
    comp='w'
print(randNo)

you=input("plyer's turn :snake(s),water(w),Gun(g)")
a=gameWin(comp,you)
if a ==None:
    print("this game is tei!")
elif a:
    print("you lose game")
elif a:
    print("you win game")
    
    
