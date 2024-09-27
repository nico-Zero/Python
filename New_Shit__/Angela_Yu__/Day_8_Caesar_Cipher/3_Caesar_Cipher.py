from os import system
from time import sleep

# Some important variables.
QUIT = ["exit", "quit"]
HOLT = 5

# The main loop
while 1:
    system("clear")
    # Question encode or decode.
    print("Would you like to decode a message or encode one? ")
    q = input("Enter 'encode' for encoding and 'decode' for decoding?\n")

    # encode
    if q == "encode" or q == "en":
        system("clear")

        # encode message input
        encode_message = input("Enter a message to encode :- ")
        if encode_message in QUIT:
            break
        # encode shift input
        encode_shift = int(input("Enter a shift value :- "))
        # encode process
        encoded_message = [(ord(i) + (encode_shift % 26)) for i in encode_message]
        encoded = []
        encode_change = encode_shift % 26
        for i in encoded_message:
            if chr(i - encode_change).islower():
                if i > 122:
                    encoded.append(chr(i - 26))
                else:
                    encoded.append(chr(i))
            elif chr(i - encode_change).isupper():
                if i > 90:
                    encoded.append(chr(i - 26))
                else:
                    encoded.append(chr(i))
            elif i - encode_change == 32:
                encoded += chr(32)
        # Printing the encoded message

        print("You encoded message is :- ", *encoded, sep="")
        print()
        sleep(HOLT)
    # decode
    elif q == "decode" or q == "de":
        system("clear")

        # decode message input
        decode_message = input("Enter message to decode :- ") or encoded
        if decode_message in QUIT:
            break
        # decode shift input
        decode_shift = input("Enter a shift value :- ") or encode_shift
        decode_shift = int(decode_shift)
        # decode process
        decoded_message = [(ord(i) - (decode_shift % 26)) for i in decode_message]
        decoded = []
        decode_change = decode_shift % 26
        for i in decoded_message:
            if chr(i + decode_change).islower():
                if i < 97:
                    decoded.append(chr(i + 26))
                else:
                    decoded.append(chr(i))
            elif chr(i + decode_change).isupper():
                if i < 65:
                    decoded.append(chr(i + 26))
                else:
                    decoded.append(chr(i))
            elif i + decode_change == 32:
                decoded += chr(32)
        # Printing the decoded message

        print("Your decoded message is :- ", *decoded, sep="")
        print()
        sleep(HOLT)

    # To quit this function.
    elif q.lower() in QUIT:
        system("clear")
        break

    else:
        system("clear")
        pass
