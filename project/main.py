import random
from statistics import meanf

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

print("comp turn: snake(s),Gun(g),Water(w)")
randNo =random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
print(randNo)


you=input("player's turn: snake(s),Gun(g),Water(w)")

a=gameWin(comp,you)
if a==None:
    print("The game is a tie!")
elif a:
    print("you win!")
else :
    print("you lose!")
