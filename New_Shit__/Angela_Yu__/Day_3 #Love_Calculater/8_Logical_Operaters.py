while 1:
    print("------------------------------")
    height = input("Enter a height: ");
    if height == "exit" :
        print("Exiting...")
        break
    
    if int(height) < 120:
        print("Sorry, you have to grow taller before you can ride.\n")

    else:   
        age = input("Enter your age: ")
        photo = input("Do you want a photo taken? Y or N ? ")

        if age == "exit":
            print("Exiting...")
            break
        if photo == "Y":
            photo_price = 3
        else:
            photo_price = 0

        print("You can ride the rollercoaster!")
        
        if int(age) < 12:
            print(f"Your ticket will be of ${5 + photo_price}")
        elif 12 <= int(age) < 18:
            print(f"Your ticket will be of ${7 + photo_price}") 
        elif int(age) < 45:
            print(f"Your ticket will be of ${12 + photo_price}")
        elif int(age) >= 45 and int(age) <= 55:
            print("Everything is going to be ok. Have a free ride on us!")
