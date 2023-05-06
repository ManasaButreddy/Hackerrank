#Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
import re
def set_of_characters(x):
    y = re.compile(r'[a-zA-Z0-9]')
    x = y.search(x)
    return bool(x)

print(set_of_characters("ABCDEefghij12345"))
print(set_of_characters("@#$%"))
                   
# Write a Python program to replace all occurrences of space, comma, or dot with a colon.
import re
mystring = "To replace spaces dots. and commas, with colon"
print(re.sub("[ ,.]",":",mystring))
