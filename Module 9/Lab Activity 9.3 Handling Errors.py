import random

try:
    print(random.randinteger(5,15))
except AttributeError:
    print("Double check the attributes in your code and try again.")
