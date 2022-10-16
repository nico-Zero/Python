import re

test = "123abc456789abc123ABC"

pattern = re.compile(r"abc")
matches = pattern.finditer(test)

matches = re.finditer(r"abc",test)

# group, start, end , span

# # span:  gives the start and end index in tuple formate
# # start: gives start index 
# # end:   gives end index
# for match in matches:
#     print(match.span(),match.start(),match.end())

# group: returns the string which was being serched.
for match in matches:
    print(match.group(0))
