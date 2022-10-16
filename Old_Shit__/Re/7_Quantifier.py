import re

dates = """
hello
01.04.2020

2020.04.01

2020-04-01
2020-05-01
2020-06-01
2020-07-01
2020-08-01

2020/04/01

2020_04_04
2020_04_04
"""

pattern = re.compile(r"\d{4}[-/]0[5-8][-/]\d{2}")
matches = pattern.finditer(dates)

for match in matches:
    print(match)
