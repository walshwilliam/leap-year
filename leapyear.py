import random
def leap():
    x = random.randint(1600, 2400)
    print(x)
    if x % 4 == 0 and x % 400 != 100 and x % 400 != 200 and x % 400 != 300:
        print("leap year")
    else:
       print("not a leap year")
leap()
