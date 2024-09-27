enemies = 1
def increase_enemies():
    global enemies
    enemies = 2
    print(f"Enemies inside fucntion: {enemies}")

increase_enemies()
print(f"Enemies outside fucntion: {enemies}")


# player_health = 10
# def game():
#     def drink_potion():
#         potion_strenth = 2
#         print(f"player health: {player_health}")

#     drink_potion()
    
# game()
