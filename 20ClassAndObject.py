class ClassName:
    pass

# define class


class Student:
    name = ''
    age = 0
    avg = 0

    def get_avg(self):
        return self.avg

    def show_student(self):
        print('name :', self.name, 'age: ', self.age, 'avg: ', self.avg)


std1 = Student()
std1.name = 'ali'
std1.age = 20
std1.avg = 14
std1.show_student()
del std1

# constructor
# destructor


class Rectangle:
    width = 0
    height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def __del__(self):
        del self
        print('Rec destroyed!!')

    def area(self):
        return self.height * self.width


rec1 = Rectangle(10, 5)
print(rec1.area())


def add(a, b):
    return a + b


def add(a, b, c):
    return a + b + c

add(2, 3)
