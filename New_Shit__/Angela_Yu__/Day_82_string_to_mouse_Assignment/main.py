def morse_code(string:str) -> list:
    morse_dict = {
        "a": "● —",
        "b": "— ● ● ●",
        "c": "— ● — ●",
        "d": "— ● ●",
        "e": "●",
        "f": "● ● — ●",
        "g": "— — ●",
        "h": "● ● ● ●",
        "i": "● ●",
        "j": "● — — —",
        "k": "— ● —",
        "l": "● — ● ●",
        "m": "— —",
        "n": "— ●",
        "o": "— — —",
        "p": "● — — ●",
        "q": "— — ● —",
        "r": "● — ●",
        "s": "● ● ●",
        "t": "—",
        "u": "● ● —",
        "v": "● ● ● —",
        "w": "● — —",
        "x": "— ● ● —",
        "y": "— ● — —",
        "z": "— — ● ●",
        "1": "● — — — —",
        "2": "● ● — — —",
        "3": "● ● ● — —",
        "4": "● ● ● ● —",
        "5": "● ● ● ● ●",
        "6": "— ● ● ● ●",
        "7": "— — ● ● ●",
        "8": "— — — ● ●",
        "9": "— — — — ●",
        "0": "— — — — —",
    }
    try:
        return [morse_dict[i] for i in string.lower()]
    except KeyError:
        return ["Invalid String"]
        


while True:
    s = input("Enter a string:- ")
    if s == "~":
        break
    print(*morse_code(s))
