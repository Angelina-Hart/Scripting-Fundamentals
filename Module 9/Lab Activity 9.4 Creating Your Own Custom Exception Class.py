class RandomError(Exception):
    def __init__(self):
        self.message = "A random error has occurred!"

# Test you custom exception class below
try:
    raise RandomError
except RandomError:
    print(RandomError.message)
