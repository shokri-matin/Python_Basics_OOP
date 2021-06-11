# Multi-line statement

a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9

b = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)

colors = ['red',
          'blue',
          'green']

c = 1; d = 2; e = 3

# Python Indentation

for i in range(1, 11):
    print(i)
    if i == 5:
        break

# Python Comments

# Single comments
# This is a comment
# print out Hello
print('Hello')


# Multi-line comments
"""This is also a
perfect example of
multi-line comments"""


# Docstring in Python

def double(num):
    """Function to double the value"""
    return 2*num


print(double.__doc__)



