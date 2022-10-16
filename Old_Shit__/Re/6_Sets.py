import re

test = "hello 123_-HELLO heyho hohey"

pattern = re.compile(r"[]")
matches = pattern.finditer(test)

for match in matches:
    print(match)
