import re

test_string = "123abc456789abc123ABC"

# pattern = re.compile(r"abc")
# matches = pattern.finditer(test_string)

matches = re.finditer(r"[0-9]+", test_string)


for i in matches:
    print(i)