import re

test = "123abc456789abc123ABC"

pattern = re.compile(r"abc")
matches = pattern.finditer(test)
# match(),search(),findall()

# matches = re.finditer(r"abc",test)
# matches = re.findall(r"abc",test)
# matches = re.match(r"abc",test) # the match function returns None if it doesn't find any matches at the bigning of the string.
# matches = re.search(r"abc",test)

print(matches)

# for match in matches:
#     print(match)
