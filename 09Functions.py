# Create Function
# def Name (List Of Parameter) :
# Statement


def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num


# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))


def power_x(x):
    xp2 = x ** 2
    print(xp2)


power_x(10)


def my_func():
    x = 10
    print("Value inside function:", x)


x = 20
my_func()
print("Value outside function:", x)


def func1(a, b):
    c = a+b
    d = a*b
    e = a/b
    return c, d, e


print(func1(4, 2), ' ')

# Python Arbitrary Arguments
def greet(*names):
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello",name)


greet("Monica","Luke","Steve","John")

# Example of recursive function
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

print(fact(5))
