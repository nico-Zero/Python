import re

# \d \D \s \S \w \W \b \B

date = [
    """
hello_123
01.04.2020

2020.04.01

2020-04-01
2020-05-23
2020-06-11
2020-07-11
2020-08-11

2020/04/02

2020_04_04
2020_04_04
"""
]

dmy_string = [
    """
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
"""
]

urls = [
    """
hello
2020-05-20
http://python-engineer.com
https://www.python-engineer.com
http://www.pyeng.net
"""
]


def answer(
    pattern_to_check,
    test_string=["123abc456abc123789abc@#$%^123ABC\t\n"],
    function="match",
    sub_function="group()",
    replace="Fuck",
    compilation_flag="re.IGNORECASE",
):
    for string in test_string:
        print(
            f"{function.capitalize()}ing.:-"
            if function != "sub"
            else f"{function.capitalize()}bing.:-"
        )
        print(f"{pattern_to_check} Example:-")
        print(f"Test String:- {repr(string)}", end="\n")

        if function == "match":
            pattern = re.compile(pattern_to_check, eval(compilation_flag))
            matches = pattern.finditer(string)
            for match in matches:
                match = eval("match" if sub_function == "" else "match." + sub_function)
                print(f"\t {match}", end="\n")
            return matches
        elif function == "split":
            pattern = re.compile(pattern_to_check)
            splitted = pattern.split(string)
            print(f"\t {splitted}")
            return splitted
        elif function == "sub":
            pattern = re.compile(pattern_to_check)
            subbed = pattern.sub(replace, string)
            print(f"\t {subbed}")
            return subbed


answer(r".")
# answer(r"^123")
# answer(r"ABC$")
# answer(r"\d")
# answer(r"\D")
# answer(r"\s")
# answer(r"\S")
# answer(r"\w")
# answer(r"\W")
# answer(r"\b123")
# answer(r"\Babc")
# answer(r"[ab]")
# answer(r"[a-zA-Z]")
# answer(r"\d*", test_string=["hello_123"])
# answer(r"\d+", test_string=["hello_123"])
# answer(r"_\d", test_string=["hello_123"])
# answer(r"_?\d", test_string=["hello123"])
# answer(r"_?\d", test_string=["hello_1_2_3"])
# answer(r"\d{3}", test_string=["hello_123"])
# answer(r"\d{1,4}", test_string=["hello_12", "hello_12345", "hello_5645"])
# answer(r"\d{4}[-/]0[5-7][-/]\d{2}", test_string=date)
# answer(r"(Mr|Mrs|Ms)\.? \w+", test_string=dmy_string)
# answer(
#     r"([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)",
#     test_string=dmy_string,
#     sub_function="group(0)",
# )
# answer(r"abc", test_string=["123abc456789abc123ABC"], function="split")
# answer(
#     r"world",
#     test_string=["hello world, your are the best world."],
#     function="sub",
#     replace="Zero",
# )
# answer(
#     r"https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)",
#     test_string=urls,
#     function="match",
#     sub_function="group(2)",
# )
# answer(
#     r"https?://(www\.)?([a-zA-Z-]+)(\.[a-zA-Z]+)",
#     test_string=urls,
#     function="sub",
#     replace=r"\2\3",
# )
# answer(r"world", test_string=["Hello World"])





