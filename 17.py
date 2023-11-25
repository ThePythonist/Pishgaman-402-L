x = int(input("Enter x : "))
y = int(input("Enter y : "))

# if not x == y:
if x != y:
    if x > y:
        print(x, "Is bigger")
    else:
        print(y, "Is bigger")
else:
    print("X and Y are equal")

# -----------------------------------------------

if x > y:
    print(x, "Is bigger")
elif x < y:
    print(y, "Is bigger")
else:
    print("Equal")
