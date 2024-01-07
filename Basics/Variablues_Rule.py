import keyword

""" Python variables rules
 - Variable name must start with a letter or the
underscore character

 - Variable name cannot start with a number

 - Variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )

- Variable names are case-sensitive (rcv_academy, RCV_Academy, RCV_ACADEMY are 3 different
variables)
"""


keywordlist = keyword.kwlist
print(keywordlist)
print(keyword.iskeyword("try"))

_test = "Lex_corp"
rcv8_test = 333

print(_test)
print(rcv8_test)

RCV8_test = 5656
rcv8_test = 897988

print(RCV8_test)
print(rcv8_test)

returnn = 3133
print(returnn)