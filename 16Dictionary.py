dic = {}
dic['one'] = 1
dic[1] = '123'
print(dic[1])
print(dic['one'])
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic)


try:
    d = 1/0
except IOError:
    print('IO Error')
except ZeroDivisionError:
    print('ZeroDivisionError')
