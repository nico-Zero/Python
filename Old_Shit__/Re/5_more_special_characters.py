import re

# more special characters

# \d :Matches any decimal digit; this is equivalent to the class [0-9].
# \D : Matches any non-digit character; this is equivalent to the class [^0-9].
# \s : Matches any whitespace character;
# \S : Matches any non-whitespace character;
# \w : Matches any alphanumeric (word) character; this is equivalent to the class [a-zA-Z0-9_].
# \W : Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
# \b Returns a match where the specified characters are at the beginning or at the end of a word r"\bain" r"ain\b"
# \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word r"\Bain" r"ain\B"
# \A Returns a match if the specified characters are at the beginning of the string "\AThe"
# \Z Returns a match if the specified characters are at the end of the string "Spain\Z"

test = "hello 123_ heyho hohey"

pattern = re.compile(r"\D")
matches = pattern.finditer(test)

for match in matches:
    print(match)
