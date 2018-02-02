#snakeandladder
import random
count=0
while(count<=100):
    n=input("enter 'r' to roll a dice")
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random number is ",r)
        print("you r in position",count)
    if(count>100):
        print("try again")
        count=count-r
    elif count==8:
        count=37
        print("you r in position",count)
    elif count==11:
        count=2
        print("you r in position",)
    elif count==13:
        count=34
        print("you r in position",count)
    elif count==25:
        count=4
        print("you r in position",count)
    elif count==38:
        count=9
        print("you r in position",count)
    elif count==40:
        count=68
        print("you r in position",count)
    elif count==52:
         count=81
         print("you r in position",count)
    elif count==65:
        count=46
        print("you r in position",count)
    elif count==76:
        count=97
        print("you r in position",count)
    elif count==89:
        count=70
        print("you r in position",count)
    elif count==93:
         count=64
         print("you r in position",count)
    elif count==100:
         print("you won")
    else:
         print("continue the game")
