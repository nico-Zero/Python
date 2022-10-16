
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(*map, sep="\n")
position = input("Where do you want to put the treasure? ")

x = int(list(position)[1]) - 1
y = int(list(position)[0]) - 1

map[x][y] = "🯀"
print(*map, sep="\n")