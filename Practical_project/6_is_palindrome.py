def is_palindrome(word):
    p_word = word[::-1]
    if p_word == word:
        return True
    else:
        return False


def more():
    while True:
        more = input("Search more? (y/n): ")
        if more in ["y", "n"]:
            return more
        else:
            print("There an error in the input!!!")


def main():
    while True:
        word = input("Enter a word:- ")
        if word in ["exit", "quit", ":q", "/q"]:
            break

        print(
            f"The word '{word}' is",
            "a Palindrome." if is_palindrome(word) else "not a Palindrome.",
        )
        print()
        if more() == "y":
            continue
        else:
            break


main()
