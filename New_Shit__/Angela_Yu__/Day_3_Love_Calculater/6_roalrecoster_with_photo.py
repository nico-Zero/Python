while 1:
    print("-----------------------------")
    height = input("Enter a height: ")
    if height == "exit" :
        print("Exiting...")
        break
    
    if int(height) < 120:
        print("Sorry, you have to grow taller before you can ride.\n")

    else:   
        print("You can ride the rollercoaster!")
        age = input("Enter your age: ")
        photo = input("Do you want a photo taken? Y or N ? ")

        if age == "exit" or photo == "exit":
            print("Exiting...")
            break
        elif photo == "Y":
            photo_price = 3
        else:
            photo_price = 0

        if int(age) < 12:
            print(f"Your ticket will be of ${5 + photo_price}")
        elif 12 <= int(age) < 18:
            print(f"Your ticket will be of ${7 + photo_price}") 
        elif int(age) >= 18:
            print(f"Your ticket will be of ${12 + photo_price}")
