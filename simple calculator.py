import random

op = ["+", "-", "*", "/", "p", "%", "!", "s", "r"]


a = input("the first number =\n")


def factorial(a):
    a = int(a)
    r = a
    for i in range(1, a):
        r = r * i
    return(r)


try:
    a = float(a)
except:
    while type(a) == str:
        a = input("please insert the first number in numbers")
        try:
            a = float(a)
        except:
            pass


bb = input("please insert the operation and the second number \n")
b = bb[0]
while b in op:
    if b == "!":
        r = factorial(a)
        print(f"{int(a)}{b} = {r} ")
        a = r
    elif b == "r":
        a = int(a)
        r = random.randint(1, a)
        print(r)
    else:
        c = bb[1:]
        try:
            c = float(c)
        except:
            while type(c) == str:
                c = input("please insert the second number in numbers")
                try:
                    c = float(c)
                except:
                    pass

        if b == "+" or b == "plus":
            r = a + c
        elif b == "-":
            r = a - c
        elif b == "*":
            r = a * c
        elif b == "/":
            if c == 0:
                print(" you can not do it hhhhhhhh")
            else:
                r = a / c
        elif b == "%":
            if c == 0:
                print(" you can not do it hhhhhhhh")
            else:
                k = a / c * 100
                r = (f"{k} %")
        else:
            print("you inserted a undefined operation ")

        print(f"{a} {b} {c} = {r}")
        a = r
    bb = input("please insert the operation and the second number \n")
    b = bb[0]
else:
    print(f"bad operation your final result is = {r}")
