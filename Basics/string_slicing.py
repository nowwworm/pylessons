# s [i:j] - slice of s from i to j
#  s [i:j:k] - slice of s from i to j with step k
# s[startindex:endindex:step]

s = "WelcomeeR to software testing mentor and rcv academy"

print(s[0])

print(s[-1]) #end of line

print(s[0:8])
print(s[4:8])
print(s[4:8:1])
print(s[4:8:2])
print(s) #print the whole string
print(s[0:]) #print the whole string
print(s[0:-1]) #print the whole string leave last element
print(s[:]) #print the whole string leave last element
print(s[20:])
print(s[44:]) #the same
print(s[-7:]) #the same

s = "WelcomeeR to software testing mentor and rcv academy"
print(s[-7:-2])

print(s[::-1]) #reverse the string

s1 = "WelcomeeR,to,  software testing mentor and rcv academy"
y = "name, age, city"
print(y.index(','))
print(y[0:y.index(',')])
