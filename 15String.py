# String

name = "Matin"
letter = name[0]  # Zero Based
print("letter", letter)
print("length", len(name))

# Traversal String
index = 0
while index < len(name):
    letter = name[index]
    print(letter)
    index += 1

for havij in name:
    print(havij)

print("name[1:5]", name[1:5])
print("name[:5]", name[:5])
print("name[0:]", name[0:])
print("name[:]", name[:])

# name[0] = 'n'
# print(name)
name = 'a' + name[1:]
print(name)

print(str.find(name, 'a'))
print(str.lower(name))
