
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(*map, sep="\n")
position = input("Where do you want to put the treasure? ").split(",")

x = int(position[0]) - 1
y = int(position[1]) - 1

map[x][y] = "X"
print(*map, sep="\n")