# the way of program, variable,statement,expresion
print("hello world")
print(type("hello world"))
print(type(3.2))
message = "hello world"
print(message)

# Numeric Literals
a = 0b1010 # Binary Literals
b = 100 # Decimal Literal
c = 0o310 # Octal Literal
d = 0x12c # Hexadecimal Literal

# Float Literal
float_1 = 10.5
float_2 = 1.5e2

# Complex Literal
x = 3.14j

print(a, b, c, d)
print(float_1, float_2)
print(x, x.imag, x.real)

# String literals

strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

# Boolean literals

x = (1 == True)
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)


# Literal Collections
fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)

n = 2
m = 1.2
print(type(m))
a = 1 + 1
b = 1 - 1
c = 1 * 1
d = 1 / 1
e = 2 ** 2
f = 5 % 3
print(d)
print(f)
g = 59 / 60
print(g)
# print("g is :" + g);
print("g is :", g)

v1, v2, v3 = 5, 3.2, "Hello"

print(v1)
print(v2)
print(v3)
