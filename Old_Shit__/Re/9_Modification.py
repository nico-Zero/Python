import re

# split , sub

test_string1 = "hello world, you are the best world."
urls = """
http://python-engineer.com
https://www.python-engineer.com
http://www.pyeng.net
"""

# pattern = re.compile(r"\W")
# splitted = pattern.split(n)

# print(splitted)

pattern = re.compile(r"https?://(www\.)?([a-zA-Z0-9-]+\.)([a-zA-Z]+)")
sub = pattern.finditer(urls)

for i in sub:
    print(i.group(2)+i.group(3))

# subbed_urls = pattern.sub(r"\2\3",urls)
# print(subbed_urls)