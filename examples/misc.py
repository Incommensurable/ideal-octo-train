# some things that are helpful when working with python

# shows you the definition, and any documentation that exists for a function
help(print)

# returns all available attributes of an object, including functions
dir("some string")

# for example this^^ tells you that there is a function called .upper() that you can use on strings, and it will return the string in uppercase
print("hello world".upper)  # shows that upper is a function, but doesn't call it
print("hello world".upper())  # actually calls the function, and returns the result
