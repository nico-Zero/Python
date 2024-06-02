x = "aaaaaabbbbbccccrrrrrttttttiiiiiiisisssssss"

def encode_letter(letters):
    if len(letters) == 0:
        return ""
    result = ""
    counter = 1
    for i in range(1,len(letters)):
        if letters[i-1] == letters[i]:
            counter += 1
        else:
            result += str(counter) + letters[i-1]
            counter = 1
    result += str(counter) + letters[-1]
    return result

print(encode_letter(x))
