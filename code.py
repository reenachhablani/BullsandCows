import random
number=[]
attempts=0
def MakeNumber():
    for i in range(4):
        x=random.randrange(0,9)
        number.append(x)
    if len(number)>len(set(number)):
        number.clear()
        MakeNumber()
def PlayGame():
    global attempts
    attempts+=1 
    cows=0
    bulls=0
    print(number)
    choice=input("enter number")
    for i in range(4):
        for j in range(4):
                if(guess[i]==number[j]):
                    cows+=1 
            if i==j:
                if(guess[i]==number[i]):
                    bulls+=1 
    print("bulls ",bulls)
    print("cows ",cows)
    if bulls==4:
        print("congratulations you won in ",attempts," attempts")
        exit()
    if bulls!=4:
        PlayGame()
MakeNumber()
PlayGame()