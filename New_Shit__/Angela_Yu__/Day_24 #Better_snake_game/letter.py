from_storage = input("From storage or input? I/S: ").lower()

# If want to input by hand
if from_storage == "i":
    sender_name = input("What's the sender's name:- ").split(",")
    receiver_name = input("What's the recipient's name:- ").split(",")
    address_of_receiver = input("What's the address of the recipient:- ").split(",")
    city_of_receiver = input("What's the city of the receiver:- ").split(",")
    date_of_letter = input("What's the date of the letter:- ").split(",")

    z = zip(
        sender_name,
        receiver_name,
        address_of_receiver,
        city_of_receiver,
        date_of_letter,
    )

    for i in z:
        with open(
            f"/media/zero/Software/Python/New_Shit__/Angela_Yu__/Day_24 #Better_snake_game/letter_to_{i[1]}.txt",
            mode="w",
        ) as f:
            letter = f"""Address: {i[2]}
City: {i[3]}
Date: {i[4]}


My Dear {i[1]},

I am fine and I hope the same from you. As you know my birthday is coming close and we have arranged a small party in the evening on that day.

I have invited my neighbors and a few close friends. I hope you will also come and join my birthday party. we shall have a lot of fun. please do come.

Yours Affectionately
{i[0]}
        """
            f.write(letter)

# If want to input from stored file
elif from_storage == "s":
    with open(
        "/media/zero/Software/Python/New_Shit__/Angela_Yu__/Day_24 #Better_snake_game/name.txt"
    ) as f:
        name = f.read().split("\n")

    for i in name:
        print(i)
        with open(
            f"/media/zero/Software/Python/New_Shit__/Angela_Yu__/Day_24 #Better_snake_game/letter_to_{i}.txt",
            mode="w",
        ) as f:
            letter = f"""My Dear {i},

I am fine and I hope the same from you. As you know my birthday is coming close and we have arranged a small party in the evening on that day.

I have invited my neighbors and a few close friends. I hope you will also come and join my birthday party. we shall have a lot of fun. please do come.

Yours Affectionately
Nico Zero
        """
            f.write(letter)
