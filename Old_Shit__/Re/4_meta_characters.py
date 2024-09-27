import re

# mete character:-  . ^ $ * + ? { } [ ] \ | ( )

# . Any character (except newline character) "he..o"
# ^ Starts with "^hello"
# $ Ends with "world$"
# * Zero or more occurrences "aix*"
# + One or more occurrences "aix+"
# { } Exactly the specified number of occurrences "al{2}"
# [] A set of characters "[a-m]"
# \ Signals a special sequence (can also be used to escape special characters) "\d"
# | Either or "falls|stays"
# ( ) Capture and group

import re

test = "123abc456789abc123ABC"

pattern = re.compile(r"ABC$")
matches = pattern.finditer(test)

for match in matches:
    print(match)
