import os

while 1:
    count = None
    def tresure(): 
        global count 
        count = 0

        os.system("cls")

        print("Welcome to Tresure Island.")
        print("Your mission is to find the tresure.")

        left = input("""You're at a cross road. Where do you want to go? Type "left" or "right"\n""").lower()
        if left =="right":
            print("You turned the wrong way.") 
            return 
        elif left == "exit":
            count += 1
            return
            
        wait = input("""You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n""").lower()
        if wait == "swim":
            print("There was crocodiles in the lake. And you're dead now!!!")
            return
        elif wait == "exit":
            count += 1
            return
        
        yellow = input("""You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?\n""").lower()
        if yellow == "red" or yellow == "blue":
            print("You entered a room of beasts.")
            return
        elif yellow =="exit":
            count += 1
            return

    tresure()
    if count == 1:
        break
    
    print("Game Over...")
    again = input("\nWould you like to try again? (y/n): ")
    if again == "n":
        break

    os.system("cls")
