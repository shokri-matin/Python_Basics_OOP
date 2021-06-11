# Hence, in Python, a file operation takes place in the following order.
# 1-Open a file
# 2-Read or write (perform operation)
# 3-Close the file

# f = open("test.txt")    # open file in current directory
# f = open("C:/Python33/README.txt")  # specifying full path

# f = open("test.txt")      # equivalent to 'r' or 'rt'
# f = open("test.txt",'w')  # write in text mode
# f = open("img.bmp",'r+b') # read and write in binary mode

# f = open("test.txt",mode = 'r',encoding = 'utf-8')
# f.close()

with open("test.txt",'w',encoding = 'utf-8') as f:
    f.write("my first file\n")
    f.write("This file\n\n")
    f.write("contains three lines\n")

f = open("test.txt", 'r', encoding='utf-8')
f.read(4)  # read the first 4 data : 'This'
f.read(4)  # read the next 4 data : ' is '
f.read()   # read in the rest till end of file : 'my first file\nThis file\ncontains three lines\n'
f.read()   # further reading returns empty sting
f.tell()   # get the current file position: 56
f.seek(0)   # bring file cursor to initial position: 0
f.read()  # read the entire file
# This is my first file
# This file
# contains three lines

for line in f:
    print(line, end = '')
# This is my first file
# This file
# contains three lines

f.readline()
# 'This is my first file\n'

f.readline()
# 'This file\n'

f.readline()
# 'contains three lines\n'

f.readline()
# ''

f.readlines()
# ['This is my first file\n', 'This file\n', 'contains three lines\n']
