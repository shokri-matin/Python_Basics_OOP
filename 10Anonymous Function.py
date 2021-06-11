# Program to show the use of lambda functions


def power(x, y):
    return x**y


anonymous_power = lambda x, y: x**y
print(anonymous_power(10, 2))


my_list = [1, 5, 4, 6, 8, 11, 3, 12]
print(list(filter(lambda x: x % 2, my_list)))


my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x * 2, my_list))

# Output: [2, 10, 8, 12, 16, 22, 6, 24]
print(new_list)