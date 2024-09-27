import re

test = "123abc456789abc123ABC"

pattern = re.compile(r"abc")
matches = pattern.finditer(test)

matches = re.finditer(r"abc",test)

for match in matches:
    print(match)
