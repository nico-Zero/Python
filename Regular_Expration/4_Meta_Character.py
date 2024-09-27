import re

### All meta characters: . ^ $ * + ? { } [ ] \ | ( )


# . Any character (except newline character)
# ^ Start with "^hello"
# $ Ends with "world$"
# * Zero or more occurrences "aix*"
# + One or more occurrences "aix+"
# { } Exactly the specified number of occurrences "al{2}"
# [ ] A set of characters "[a-m]"
# \ Special sequence (or escape special characters) "\d"
# | Either of "falls|stays"
# ( ) Capture and group

