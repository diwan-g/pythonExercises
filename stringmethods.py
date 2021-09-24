mystr = "Welcome to Heaven!"

# Slicing (start:end(+1):step)
print(mystr[0:5])
print(mystr[::-1])
print(mystr[-1:])
print(mystr[0::3])

# misc methods
print(mystr.lower())
print(mystr.title())
print(mystr.upper())

print(mystr.find("Heaven"))
print(mystr.split())
print(mystr.split("o"))
print(mystr.count("o"))
print(mystr.replace("!", "!!"))

spaced_str = " Hello, I am spaced string       "
print(spaced_str.strip())
print(spaced_str.rstrip())
print(spaced_str.lstrip())

print(mystr.isalnum()) #False
print(mystr.isdigit()) # False
print(mystr.istitle()) # False
print(mystr.isspace()) # False

