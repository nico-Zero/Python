import re

test_string = "123abc456789abc123ABC"

pattern = re.compile(r"abc")

# ### finditer()
# matches = pattern.finditer(test_string)

# ### Another way to finditer
# # matches = re.finditer(r"abc", test_string)

# ### findall()
# # matches = pattern.findall(test_string)

# for i in matches:
#     print(i)

# ### match() 
# matches = pattern.match(test_string)

# print(matches)

### search()
matches = pattern.search(test_string)

print(matches)

