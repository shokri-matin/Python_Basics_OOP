# Iterator

# Python for Loop
# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
sum = 0

# iterate over the list
for val in numbers:
    sum = sum+val


# Output: The sum is 48
print("The sum is", sum)

# The range() function  -  range(start,stop,step size)
# Output: range(0, 10)
print(range(10))

# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(10)))

# Output: [2, 3, 4, 5, 6, 7]
print(list(range(2, 8)))

# Output: [2, 5, 8, 11, 14, 17]
print(list(range(2, 20, 3)))

# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in range(len(genre)):
    print("I like", genre[i])


# for loop with else

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


# Python while Loop

n = 10
while n > 0:
    print("n:", n)
    n -= 1

n = 10
while n > 0:
    print("n:", n, '\t', 10-n+1)
    n -= 1

# while loop with else
counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")

# Python break
for val in "string":
    if val == "i":
        break
    print(val)


# Python continue
for val in "string":
    if val == "i":
        continue
    print(val)

# Syntax of pass

sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass
