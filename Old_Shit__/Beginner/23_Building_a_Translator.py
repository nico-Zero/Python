def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeoiu":
            if letter.isupper():
                translation += "X"
            else:
                translation += "x"
        else:
            translation += letter
    return translation


print("Translation : " + translate(input("Enter a word : ")))
 