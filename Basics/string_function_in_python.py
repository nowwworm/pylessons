#len(s): Return the number of items in an object, if an object is string it will return
#the length of the string
#  str(): "Converts specified value into a String
# upper() : Converts a string into upper case
# count(sub[, start[, end]]) : Returns the number of times a specified value is found
# isupper() : Returns True if all characters in the string are upper case
# islower() : Returns True if all characters in the string are lower case
# split(sep=None, maxsplit=-1) : Splits the string at the specified separator, and returns
# split : Splits a string into a list, starting from the right.
# strip(): Returns a trimmed version of the string
# lstrip([chars]): Removes any leading characters
# rstrip([chars]): Removes any trailing characters
# replace(old, new[, count]): Replaces a specified phrase with another specified phrase.
# find(sub[, start[, end]]) : Searches the string for a specified value and returns the position

x = "lex corp academy"
print(len(x))

num_1 =  88005553555
print(str(num_1))

z = str(num_1)
print(z.find("5"))

print(x.upper())

xy = "lex corp academy Lex CORP ACADEMY lex corp academy Lex CORP ACADEMY"

print(xy.count("lex"))

xyz = "rcv academy rcv Academy rcv Academy rcv Academy"


print(xyz.count("rcv", 10, 30))

a = xyz.upper()
print(a.isupper())
print(a.islower())


xyz_1 = "rcv academy rcv Academy rcv Academy rcv Academy"


print(xyz_1.split())

print(xyz_1.rsplit())

xyz_2 = "     :::'''' rcv academy rcv Academy rcv Academy rcv Academy 777"
print(xyz_2.strip())
print(xyz_2.strip(':;7 \''))
print(xyz_2.lstrip(':;7 \''))
print(xyz_2.rstrip(':;7 \''))

print(xyz_2.replace("rcv", "lex"))
print(xyz_2.replace("rcv", "lex", 2))

print(xyz_2.find("rcv"))
print(xyz_2.index("rcv"))





