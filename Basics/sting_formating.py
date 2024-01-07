x = "Python Class"
y = "RCV Academy"

print("Welcome to " + x + " from " + y)
print("Welcome to %s from %s" %(x, y))
print("Welcome to %s from %s" %("Java Class", y))

print("Welcome to {} from {}".format(x, y))
print("Welcome to {1} from {0}".format(x, y))
print("Welcome to {classname} from {academyname}".format(classname=x, academyname=y))
print("Welcome to {classname} from {academyname}".format(classname="Java", academyname=y))