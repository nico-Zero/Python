str = "Hello World"
print(str)

str = """Hello 
World"""

print(str)

str = """Hello \
World"""

print(str)

str = "Hello World"
char = str[9]
charx = str[-3]

print(char)
# print(charx)

substr = str[:5]
print(substr)

rev = str[::-1]  # it reverses the string.
print(rev)

greeting = "Hello"
name = "Tom"

sentence = greeting + " " + name

print(sentence)

for i in greeting:
    print(i)

str = "     Hello World     "
str = str.strip()
print(str)

print(str.upper())
print(str.lower())
print(str.startswith("Hello"))
print(str.endswith("World"))

print(str.find("o"))
print(str.count("l"))

print(str.replace("World", "Universe"))

str = "how are you doing"
strx = "how,are,you,doing"

list = str.split()
listx = strx.split(",")

print(list)
print(listx)

str_ = " ".join(list)
print(str_)

var = "just a string"
str = "the variable is %s" % var
print(str)

var = 69
str = "the variable is %d" % var
print(str)

var = 69.69
str = "the variable is %.2f" % var
print(str)

var = "just a string"
varx = ".I am a god."
str = "the variable is {:}{}".format(var, varx)
print(str)

var = "just a string"
varx = "I am a god."
str = f"the variable is {var} and {varx}"
print(str)
