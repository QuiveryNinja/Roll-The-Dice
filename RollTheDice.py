import random

def Roll():
    n = int(input("Numnber of rolls: "))
    i = 0
    m = 1
    pair = 0
    for i in range(1,n+1):
        res = random.randint(1,6)
        print(res)
        if res % 2==0:
            pair += 1
        i -= 1
    print("You rolled "+ str(pair) + " even numbers.")

Roll()