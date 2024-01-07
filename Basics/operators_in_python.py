
"""
Arithmetic operators)
Assignment operators / Операторы присваивание
Comparison operators
Logical operators
Identity operators / Операторы индентичности проверки идентичности объектов,
то есть они позволяют определить, ссылаются ли две переменные на один и тот же объект в памяти.
Membership operators - операторы принадлежности
Bitwise operators - побитовые операторы применяются к двоичным представлениям чисел на уровне отдельных битов
"""

# Arithmetic operators
'''
x = 15
y = 4
print(x + y)
print(x - y)
print(x * y)
print(x % y) #Modulo Operation
print(x ** y)
print(x // y)
'''

# Assignment operators
# x = 10
# print(x)
# x += 2
# print(x)
# x -= 4
# print(x)
# x *= 4
# print(x)
# x /= 4
# print(x)
# x **= 4
# print(x)

#Comparison operators
# x = 10
# y = 6
# print(x == y)
# print(x > y)
# print(x < y)
# print(x <= y)
# print(x >= y)
# print(x != y)

# #Logical operators (and / or)
# x = 10
# y = 4
# print(x == y and x > y)
# print(x == y or x > y)

#Identity operators
# x = ["rcvacademy", "stm"]
# y = ["rcvacademy", "stm"]
#
# print(x == y)
# print(x is y)
# print(x is not y)

#Membership operators
x = ["rcvacademy", "stm"]
y = ["rcvacademy", "stm"]

print("stm" in y)
print("stm" not in y)

#Bitwise operators
# & - AND
# Операция конъюнкции (Логическое Или)
# Возврашает True
# If true & true -> true
# if false & true -> false

# | - OR
# Операция дезюнкции (Логическое Или)
# Возврашает True
# If true & true -> true
# if false & false -> true
# if false & true -> true

# ~ Not
# ^ - XOR

# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11

x = 0
y = 1
print(x & y)

x = 1
y = 3
print(x & y)

x = 1
y = 3
print(x | y)



