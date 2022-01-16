def leap():
    x = input("enter year: ")
    y = int(x)
    if y % 4 == 0 and y % 400 != 100 and y % 400 != 200 and y % 400 != 300:
        print(y, "is a leap year")
    else:
        print(y, "is not a leap year")
    leap()
leap()
