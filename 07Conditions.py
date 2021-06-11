# Conditions
x = 6

# If Else If
if x < 5:
    print("x < 5")
else:
    print("x >= 5")


def printParity(x):
    if x % 2 == 0:
        print("x is even :", x)
    else:
        print("x is odd :", x)

printParity(10)

# Nested If
y = 10
if x < y:
    print("x < y")
elif x > y:
    print("x > y")
else:
    print("x == y")


if x < y:
    print("x < y")
else:
    if x > y:
        print("x > y")
    else:
        print("x == y")

if x > 0 and x < 10:
    print("x > 0 and x < 10")

if 0 < x < 10:
    print("x > 0 and x < 10")



