import re

# ASCII, A : Makes several escapes like \w, \b, \s and \d match only on ASCII characters with the respective property.
# DOTALL, S : Make . match any character, including newlines.
# IGNORECASE, I : Do case-insensitive matches.
# LOCALE, L : Do a locale-aware match.
# MULTILINE, M : Multi-line matching, affecting ^ and $.
# VERBOSE, X (for ‘extended’) : Enable verbose REs, which can be organized more cleanly and understandably.


test_string = "hello world, you are the best World."
pattern = re.compile(r"world",re.I)
sub = pattern.finditer(test_string)
for i in sub:
    print(i)
