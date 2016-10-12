import string

s = "a\n"
for c in string.lowercase:
    s += c + "\n"
s += "a\n"*((37*2 - len(s))/2)

"""
s = "a\n"
for c in string.uppercase:
    s += c + "\n"
s += "a\n"*((37*2 - len(s))/2)
################
s = "a\n"
for c in "01234567890_{}":
    s += c + "\n"
s += "a\n"*((37*2 - len(s))/2)
"""

print s
