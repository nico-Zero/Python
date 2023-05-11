import re

# \d \D \s \S \w \W \b \B


def match(x, test_string=["123abc456abc123789abc@#$%^123ABC\t\n\s\e"],ans="group"):
    for string in test_string:
        print(f"{x} Example:-")
        print(f"Test String:- {repr(string)}", end="\n")

        pattern = re.compile(x)
        matches = pattern.finditer(string)
        for match in matches:
            match = eval("match" if ans == "" else "match."+ans+"()")
            print(f"\t {match}", end="\n")


# match(r".")
# match(r"^123")
# match(r"ABC$")
# match(r"\d")
# match(r"\D")
# match(r"\s")
# match(r"\S")
# match(r"\w")
# match(r"\W")
# match(r"\b123")
# match(r"\Babc")
# match(r"[ab]")
# match(r"[a-zA-Z]")
# match(r"\d*", test_string=["hello_123"])
# match(r"\d+", test_string=["hello_123"])
# match(r"_\d", test_string=["hello_123"])
# match(r"_?\d", test_string=["hello123"])
# match(r"_?\d", test_string=["hello_1_2_3"])
# match(r"\d{3}", test_string=["hello_123"])
# match(r"\d{1,4}", test_string=["hello_12", "hello_12345", "hello_5645"])

# date = [""" 
# hello_123
# 01.04.2020

# 2020.04.01

# 2020-04-01
# 2020-05-23
# 2020-06-11
# 2020-07-11
# 2020-08-11

# 2020/04/02

# 2020_04_04
# 2020_04_04
# """]

# match(r"\d{4}[-/]0[5-7][-/]\d{2}",test_string=date)

dmy_string = ["""
hello world
1223
2020-05-20
Mr Simpson
Mrs Simpson
Mr. Brown
Ms Smith
Mr. T
pythonengineer@gmail.com
Python-engineer@gmx.de
python-engineer123@my-domain.org
"""]

# match(r"(Mr|Mrs|Ms)\.? \w+",test_string=dmy_string)
match(r"([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)",test_string=dmy_string,ans="")
