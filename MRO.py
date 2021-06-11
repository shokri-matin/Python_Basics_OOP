class X:
    i = 0


class Y:
    i = 1


class Z:
    i = 2


class A(X, Y):
    pass


class B(Y, Z):
    pass


class M(B, A, Z):
    pass


AObj = A()
print(AObj.i)

BObj = B()
print(BObj.i)

MObj = M()
print(MObj.i)

# Output:
# [<class '__main__.M'>, <class '__main__.B'>,
# <class '__main__.A'>, <class '__main__.X'>,
# <class '__main__.Y'>, <class '__main__.Z'>,
# <class 'object'>]

print(A.mro())
print(B.mro())
print(M.mro())