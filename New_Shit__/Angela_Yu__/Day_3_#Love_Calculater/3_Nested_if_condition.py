while 1:
    height = input("Enter a height: ");
    if height == "exit" :
        print("Exiting...")
        break
    
    if int(height) < 120:
        print("Sorry, you have to grow taller before you can ride.\n")

    else:   
        age = input("Enter your age: ")

        if age == "exit":
            print("Exiting...")
            break
        print("You can ride the rollercoaster!")
        
        if int(age) < 12:
            print("Your ticket will be of $5")
        elif 12 <= int(age) < 18:
            print("Your ticket will be of $7") 
        elif int(age) >= 18:
            print("Your ticket will be of $12")
        print()
